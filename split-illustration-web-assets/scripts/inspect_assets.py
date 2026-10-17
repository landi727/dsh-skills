#!/usr/bin/env python3
"""Inspect and statically reassemble an illustration asset manifest.

Requires Pillow. Run: inspect_assets.py --manifest scene.json --out-dir checks
Inputs are read only. A nonzero exit code indicates an automated check failed;
an exit code of zero does not replace visual review or verify original-art fidelity.
All file paths in a manifest are relative to that manifest's directory.
"""

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path, PureWindowsPath
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


OUTPUT_NAMES = (
    "composite.png", "reference-diff.png", "edge-contact-sheet.png", "report.json"
)
LAYER_KINDS = {"background", "structure", "subject", "prop", "foreground"}
SOURCE_METHODS = {"native", "extract", "extract-and-complete", "regenerated"}
PROCESSING_METHODS = {"native", "vector-export", "resampled", "super-resolution",
                      "generated-completion", "mixed"}
VISUAL_QUALITY_STATUSES = {"passed", "failed", "unverified"}
RESOLUTION_FIELDS = {"max_display_width_px", "max_display_height_px", "pixel_ratio",
                     "source_effective_width_px", "source_effective_height_px",
                     "processing_method", "visual_quality_status"}


def number(value, label, errors, positive=False, integer=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        errors.append(f"{label}: expected a finite number")
        return None
    if not math.isfinite(value) or (positive and value <= 0):
        errors.append(f"{label}: expected a finite{' positive' if positive else ''} number")
        return None
    if integer and value != int(value):
        errors.append(f"{label}: expected an integer")
        return None
    return int(value) if integer else value


def dimensions(item, label, errors):
    if not isinstance(item, dict):
        errors.append(f"{label}: expected an object")
        return None
    width = number(item.get("width"), f"{label}.width", errors, True, True)
    height = number(item.get("height"), f"{label}.height", errors, True, True)
    return (width, height) if width is not None and height is not None else None


def resolve_file(value, base, label, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: expected a nonempty file path")
        return None
    relative = Path(value)
    if relative.is_absolute() or PureWindowsPath(value).is_absolute():
        errors.append(f"{label}: use a relative path inside the manifest package")
        return None
    path = (base / relative).resolve()
    try:
        path.relative_to(base.resolve())
    except ValueError:
        errors.append(f"{label}: resolved path escapes the manifest package")
        return None
    if not path.is_file():
        errors.append(f"{label}: file does not exist: {path}")
        return None
    return path


def read_image(path, label, errors):
    try:
        with Image.open(path) as opened:
            opened.load()
            image = opened.copy()
            return image, opened.format
    except (OSError, ValueError, Image.DecompressionBombError) as exc:
        errors.append(f"{label}: cannot read image: {exc}")
        return None, None


def inspect_resolution(layer, image, result, errors, warnings, label):
    """Measure painted pixels, while keeping pixel sufficiency and quality distinct."""
    # Alpha > 0 includes antialiasing pixels but excludes transparent padding.
    bbox = image.getchannel("A").getbbox()
    effective = [bbox[2] - bbox[0], bbox[3] - bbox[1]] if bbox else [0, 0]
    info = {"full_file_pixel_size": list(image.size),
            "effective_pixel_size": effective,
            "effective_bbox_px": list(bbox) if bbox else None,
            "effective_bbox_rule": "alpha > 0; [left, top, right, bottom), in file pixels",
            "required_pixel_size": None, "size_status": "unverified",
            "source_effective_pixel_size": None,
            "source_measurement_status": "not-declared",
            "source_sufficiency": "unverified",
            "source_sufficiency_basis": "Declared pre-processing effective dimensions compared with target pixels; original pixel provenance and visual detail are not auto-verified",
            "required_source_upscale_factor": None,
            "visual_quality_status": "not-auto-verified",
            "declared_visual_quality_status": "unverified"}
    result["resolution"] = info
    if bbox is None:
        errors.append(f"{label}: asset has no painted pixels (all alpha values are zero)")
        info["size_status"] = "failed"
    if "resolution" not in layer:
        info["schema_status"] = "not-declared"
        warnings.append(f"{label}.resolution: maximum display size and pixel_ratio are not declared; target pixel sufficiency is unverified")
        return

    resolution = layer["resolution"]
    resolution_label = f"{label}.resolution"
    error_start = len(errors)
    if not isinstance(resolution, dict):
        errors.append(f"{resolution_label}: expected an object")
        info.update({"schema_status": "failed", "size_status": "failed"})
        return
    unknown = set(resolution) - RESOLUTION_FIELDS
    if unknown:
        errors.append(f"{resolution_label}: unknown field(s): {', '.join(sorted(unknown))}")
    display = [number(resolution.get(key), f"{resolution_label}.{key}", errors,
                      positive=True)
               for key in ("max_display_width_px", "max_display_height_px")]
    ratio = number(resolution.get("pixel_ratio"), f"{resolution_label}.pixel_ratio",
                   errors, positive=True)
    info.update({"max_display_pixel_size": display, "pixel_ratio": ratio,
                 "display_size_units": "CSS px of the effective painted region; transparent padding excluded"})
    source_keys = ("source_effective_width_px", "source_effective_height_px")
    source_present = [key in resolution for key in source_keys]
    source_size = None
    if any(source_present):
        info["source_measurement_status"] = "declaration-only-not-verified"
        if not all(source_present):
            errors.append(f"{resolution_label}: source_effective_width_px and source_effective_height_px must be supplied together")
        source_size = [number(resolution.get(key), f"{resolution_label}.{key}", errors,
                              positive=True, integer=True) for key in source_keys]
        info["source_effective_pixel_size"] = source_size
    else:
        info["source_effective_pixel_size"] = None
    for key, choices in (("processing_method", PROCESSING_METHODS),
                         ("visual_quality_status", VISUAL_QUALITY_STATUSES)):
        if key not in resolution:
            continue
        value = resolution[key]
        if not isinstance(value, str) or value not in choices:
            errors.append(f"{resolution_label}.{key}: expected one of {', '.join(sorted(choices))}")
        elif key == "processing_method":
            info["processing_method"] = value
        else:
            info["declared_visual_quality_status"] = value
            if value == "failed":
                warnings.append(f"{resolution_label}: visual quality is declared failed; this declaration is not an automated image-quality measurement")
    info["processing_method_status"] = "declaration-only-not-verified"
    required = None
    if all(value is not None for value in display) and ratio is not None:
        products = [value * ratio for value in display]
        if not all(math.isfinite(value) for value in products):
            errors.append(f"{resolution_label}: display size times pixel_ratio must be finite")
        else:
            required = [math.ceil(value) for value in products]
            info["required_pixel_size"] = required
    info["schema_status"] = "failed" if len(errors) > error_start else "passed"
    if info["schema_status"] == "failed":
        info["size_status"] = "failed"
        return
    sufficient = bbox is not None and all(actual >= target for actual, target
                                          in zip(effective, required))
    info["size_status"] = "passed" if sufficient else "failed"
    if not sufficient:
        errors.append(f"{resolution_label}: effective pixel size {effective} is below required {required}; transparent padding does not count")
    if source_size is not None:
        source_sufficient = all(actual >= target for actual, target
                                in zip(source_size, required))
        factor = max(1.0, *(target / actual for actual, target
                           in zip(source_size, required)))
        info["source_sufficiency"] = "passed" if source_sufficient else "insufficient"
        info["required_source_upscale_factor"] = factor
        if not source_sufficient:
            warnings.append(f"{resolution_label}: original effective pixels {source_size} are below target {required}; required source upscale factor is {factor:.6g}. Export dimensions may still pass; visual quality requires review")
    else:
        warnings.append(f"{resolution_label}: original effective pixels are not declared; source pixel sufficiency is unverified")


def inspect_coverage(layer, image, result, errors):
    coverage = layer.get("coverage")
    if coverage is None:
        result["coverage"] = {"status": "not-declared"}
        return
    label = f"layer {result['id']}.coverage"
    if not isinstance(coverage, dict) or coverage.get("mode") != "opaque-rect":
        errors.append(f"{label}: expected mode 'opaque-rect'")
        result["coverage"] = {"status": "failed"}
        return
    rect = coverage.get("required_rect")
    if not isinstance(rect, dict):
        errors.append(f"{label}.required_rect: expected an object")
        result["coverage"] = {"status": "failed"}
        return
    vals = {}
    for key in ("x", "y", "width", "height"):
        vals[key] = number(rect.get(key), f"{label}.required_rect.{key}", errors,
                           positive=key in ("width", "height"))
    if any(value is None for value in vals.values()):
        result["coverage"] = {"status": "failed"}
        return
    scale = layer["export_scale"]
    left = (vals["x"] - layer["x"]) * scale
    top = (vals["y"] - layer["y"]) * scale
    right = left + vals["width"] * scale
    bottom = top + vals["height"] * scale
    # Include every source pixel touched by the required rectangle. Transparent
    # padding and holes are checked, rather than only its nontransparent bbox.
    bounds = (math.floor(left), math.floor(top), math.ceil(right), math.ceil(bottom))
    inside = left >= 0 and top >= 0 and right <= image.width and bottom <= image.height
    info = {"required_rect": vals, "sample_pixel_rect": list(bounds),
            "alpha_threshold": 254, "inside_file": inside}
    if not inside:
        info["status"] = "failed"
        errors.append(f"{label}: required rectangle extends outside the asset file")
    else:
        hist = image.getchannel("A").crop(bounds).histogram()
        low = sum(hist[:254])
        info.update({"sampled_pixels": sum(hist), "low_alpha_pixels": low,
                     "minimum_alpha": next(i for i, count in enumerate(hist) if count),
                     "status": "passed" if low == 0 else "failed"})
        if low:
            errors.append(f"{label}: {low} required pixels have alpha below 254")
    result["coverage"] = info


def render_layer(image, layer, canvas_size):
    width, height = layer["width"], layer["height"]
    x, y = layer["x"], layer["y"]
    if all(value == int(value) for value in (width, height, x, y)):
        logical = image.resize((int(width), int(height)), Image.Resampling.LANCZOS)
        placed = Image.new("RGBA", canvas_size)
        placed.alpha_composite(logical, (int(x), int(y)))
        return placed, "lanczos-resize-and-integer-placement"
    scale = layer["export_scale"]
    placed = image.transform(
        canvas_size, Image.Transform.AFFINE,
        (scale, 0, -x * scale, 0, scale, -y * scale),
        resample=Image.Resampling.BICUBIC, fillcolor=(0, 0, 0, 0))
    return placed, "bicubic-affine-fractional-placement"


def compare_reference(composite, source, out_path):
    actual = composite.crop((0, 0, source.width, source.height))
    difference = ImageChops.difference(actual, source)
    bands = difference.split()
    per_channel = {}
    count = source.width * source.height
    pixel_max = bands[0]
    for channel, band in zip("RGBA", bands):
        hist = band.histogram()
        per_channel[channel] = {
            "mean_absolute_difference": sum(i * n for i, n in enumerate(hist)) / count,
            "maximum_absolute_difference": max(i for i, n in enumerate(hist) if n),
        }
        pixel_max = ImageChops.lighter(pixel_max, band)
    histogram = pixel_max.histogram()
    differing = sum(histogram[1:])
    # Alpha differences appear white; RGB differences use their actual absolute
    # magnitudes. This visible RGB export does not affect RGBA comparison metrics.
    Image.merge("RGB", tuple(ImageChops.lighter(band, bands[3])
                              for band in bands[:3])).save(out_path)
    return {
        "status": "exact" if differing == 0 else "needs-visual-review",
        "comparison": "RGBA pixels in the original source rectangle",
        "source_rectangle": [0, 0, source.width, source.height],
        "differing_pixels": differing, "total_pixels": count,
        "differing_pixel_fraction": differing / count,
        "channels": per_channel,
        "diff_display": "absolute RGB differences; alpha differences shown white",
    }


def contact_sheet(items, out_path):
    row_height, pane_width, pane_height = 278, 380, 220
    sheet = Image.new("RGB", (800, max(60, 40 + row_height * len(items))), "#d4d4d4")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    draw.text((12, 10), "Full asset thumbnails: WHITE / BLACK (manual edge review)",
              fill="black", font=font)
    for index, (layer, image) in enumerate(items):
        top = 40 + index * row_height
        label = f"{layer['id']}  file {image.width}x{image.height} px"
        draw.text((12, top + 3), label.encode("ascii", "replace").decode("ascii"),
                  fill="black", font=font)
        thumbnail = ImageOps.contain(image, (pane_width, pane_height),
                                     method=Image.Resampling.LANCZOS)
        for left, color in ((12, "white"), (408, "black")):
            pane = Image.new("RGBA", (pane_width, pane_height), color)
            pane.alpha_composite(thumbnail, ((pane_width - thumbnail.width) // 2,
                                             (pane_height - thumbnail.height) // 2))
            sheet.paste(pane.convert("RGB"), (left, top + 25))
    sheet.save(out_path)


def inspect(manifest_path, out_dir):
    errors, warnings, layer_results, loaded_layers = [], [], [], []
    inputs = {manifest_path.resolve()}
    source_image = None
    canvas_size = None
    report = {
        "manifest": str(manifest_path), "layers": layer_results,
        "errors": errors, "warnings": warnings,
        "visual_review": {
            "status": "required",
            "checks": ["transparent edges on both backgrounds", "structure and occlusion",
                       "color and drawing fidelity", "completed and extended regions"],
            "limitations": [
                "White fringes and drawing style are not detected automatically.",
                "visible_source_preserved is a declaration, not verified pixel provenance.",
                "A completion mask specifies permitted regions; it does not prove paint stayed there.",
                "Only declared opaque rectangles are checked for complete coverage.",
                "Effective export pixels are checked only against declared maximum display size and pixel_ratio.",
                "Source pixel sizes, processing_method and visual_quality_status are declarations; sharpness, recovered detail and fidelity are not auto-verified.",
                "Target views are schema-checked; this script does not render their viewport crops.",
            ],
        },
        "outputs": {},
    }
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"manifest: cannot load JSON: {exc}")
        manifest = {}
    if not isinstance(manifest, dict):
        errors.append("manifest: expected an object")
        manifest = {}
    if type(manifest.get("schema_version")) is not int or manifest.get("schema_version") != 1:
        errors.append("schema_version: expected integer 1")
    base = manifest_path.parent
    source = manifest.get("source")
    source_size = dimensions(source, "source", errors)
    source_path = resolve_file(source.get("file") if isinstance(source, dict) else None,
                               base, "source.file", errors)
    if source_path:
        inputs.add(source_path)
        opened, _ = read_image(source_path, "source.file", errors)
        if opened is not None:
            source_image = opened.convert("RGBA")
            if source_size and opened.size != source_size:
                errors.append(f"source: declared size {source_size} differs from file {opened.size}")
        if isinstance(source, dict) and "sha256" in source:
            expected = source["sha256"]
            if not isinstance(expected, str) or len(expected) != 64 or any(
                    char not in "0123456789abcdefABCDEF" for char in expected):
                errors.append("source.sha256: expected a 64-character hexadecimal digest")
            elif hashlib.sha256(source_path.read_bytes()).hexdigest() != expected.lower():
                errors.append("source.sha256: digest mismatch")
    canvas_size = dimensions(manifest.get("canvas"), "canvas", errors)
    if canvas_size and source_size and (canvas_size[0] < source_size[0] or
                                       canvas_size[1] < source_size[1]):
        errors.append("canvas: must contain the source rectangle at origin (0, 0)")
        canvas_size = None
    report["canvas"] = {"size": canvas_size, "origin": [0, 0]}
    target_views = manifest.get("target_views", [])
    report["target_views"] = []
    if not isinstance(target_views, list):
        errors.append("target_views: expected a list")
        target_views = []
    seen_view_ids = set()
    for index, view in enumerate(target_views):
        label = f"target_views[{index}]"
        error_start = len(errors)
        if not isinstance(view, dict):
            errors.append(f"{label}: expected an object")
            continue
        view_id = view.get("id")
        if not isinstance(view_id, str) or not view_id.strip():
            errors.append(f"{label}.id: expected a nonempty string")
            view_id = f"invalid-view-{index}"
        elif view_id in seen_view_ids:
            errors.append(f"{label}.id: duplicate id {view_id}")
        seen_view_ids.add(view_id)
        width_px = number(view.get("width_px"), f"{label}.width_px", errors, True, True)
        height_px = number(view.get("height_px"), f"{label}.height_px", errors, True, True)
        source_rect = view.get("source_rect")
        rectangle = None
        if not isinstance(source_rect, dict):
            errors.append(f"{label}.source_rect: expected an object")
        else:
            rectangle = {key: number(source_rect.get(key), f"{label}.source_rect.{key}",
                                     errors, positive=key in ("width", "height"))
                         for key in ("x", "y", "width", "height")}
        report["target_views"].append({
            "id": view_id, "width_px": width_px, "height_px": height_px,
            "source_rect": rectangle,
            "schema_status": "failed" if len(errors) > error_start else "passed",
            "visual_status": "not-rendered-requires-visual-review"})
    layers = manifest.get("layers")
    if not isinstance(layers, list) or not layers:
        errors.append("layers: expected a nonempty list")
        layers = []
    seen_ids, valid_z = set(), []
    for index, layer in enumerate(layers):
        error_start = len(errors)
        label = f"layers[{index}]"
        if not isinstance(layer, dict):
            errors.append(f"{label}: expected an object")
            continue
        layer_id = layer.get("id")
        display_id = layer_id if isinstance(layer_id, str) and layer_id.strip() else f"invalid-layer-{index}"
        result = {"input_index": index, "id": display_id}
        layer_results.append(result)
        if not isinstance(layer_id, str) or not layer_id.strip():
            errors.append(f"{label}.id: expected a nonempty string")
        elif layer_id in seen_ids:
            errors.append(f"{label}.id: duplicate id {layer_id}")
        else:
            seen_ids.add(layer_id)
        for key, choices in (("kind", LAYER_KINDS), ("source_method", SOURCE_METHODS)):
            if not isinstance(layer.get(key), str) or not layer[key].strip():
                errors.append(f"{label}.{key}: expected a nonempty string")
            elif layer[key] not in choices:
                errors.append(f"{label}.{key}: expected one of {', '.join(sorted(choices))}")
        if "opaque_allowed" in layer and type(layer["opaque_allowed"]) is not bool:
            errors.append(f"{label}.opaque_allowed: expected a boolean")
        if "visible_source_preserved" in layer and not (
                type(layer["visible_source_preserved"]) is bool or
                layer["visible_source_preserved"] == "unknown"):
            errors.append(f"{label}.visible_source_preserved: expected a boolean or 'unknown'")
        if "visible_source_preserved" in layer:
            result["visible_source_preserved"] = {
                "declared": layer["visible_source_preserved"] if (
                    type(layer["visible_source_preserved"]) is bool or
                    layer["visible_source_preserved"] == "unknown") else None,
                "status": "not-verified"}
        values = {}
        for key in ("z", "x", "y", "width", "height", "export_scale"):
            values[key] = number(layer.get(key), f"{label}.{key}", errors,
                                 positive=key in ("width", "height", "export_scale"),
                                 integer=key in ("z", "width", "height"))
        if values["z"] is not None:
            valid_z.append(values["z"])
        asset_path = resolve_file(layer.get("file"), base, f"{label}.file", errors)
        if asset_path:
            inputs.add(asset_path)
        mask_path = None
        if "completion_mask" in layer:
            mask_path = resolve_file(layer["completion_mask"], base,
                                     f"{label}.completion_mask", errors)
            if mask_path:
                inputs.add(mask_path)
        if asset_path is None or any(value is None for value in values.values()):
            result["status"] = "failed"
            continue
        image, file_format = read_image(asset_path, f"{label}.file", errors)
        if image is None:
            result["status"] = "failed"
            continue
        if file_format not in ("PNG", "WEBP"):
            errors.append(f"{label}.file: exported layers must be PNG or WebP")
        expected_size = (values["width"] * values["export_scale"],
                         values["height"] * values["export_scale"])
        if any(abs(v - round(v)) > 1e-7 for v in expected_size):
            errors.append(f"{label}: logical size times export_scale must give integer pixels")
        elif image.size != tuple(round(value) for value in expected_size):
            errors.append(f"{label}: file size {image.size} differs from expected {expected_size}")
        has_alpha_channel = "A" in image.getbands()
        rgba = image.convert("RGBA")
        hist = rgba.getchannel("A").histogram()
        transparent_required = layer.get("kind") != "background" and layer.get("opaque_allowed") is not True
        if transparent_required and not has_alpha_channel:
            errors.append(f"{label}: nonbackground asset requires a real alpha channel")
        if transparent_required and sum(hist[:255]) == 0:
            errors.append(f"{label}: no transparent or partial-alpha pixels; declare opaque_allowed only for intended opaque rectangles")
        result.update({"file": str(asset_path), "file_size": list(image.size),
                       "logical_rectangle": [values[key] for key in ("x", "y", "width", "height")],
                       "export_scale": values["export_scale"], "z": values["z"],
                       "alpha": {"channel_present": has_alpha_channel,
                                 "transparent_pixels": hist[0],
                                 "transparent_pixel_fraction": hist[0] / (image.width * image.height),
                                 "partial_alpha_pixels": sum(hist[1:255]),
                                 "opaque_pixels": hist[255],
                                 "minimum_alpha": next(i for i, count in enumerate(hist) if count),
                                 "transparency_required": transparent_required}})
        inspect_resolution(layer, rgba, result, errors, warnings, label)
        if mask_path:
            mask, _ = read_image(mask_path, f"{label}.completion_mask", errors)
            if mask is not None:
                mask_ok = mask.size == image.size and mask.mode in ("1", "L")
                if mask.size != image.size:
                    errors.append(f"{label}.completion_mask: size must match the asset file")
                if mask.mode not in ("1", "L"):
                    errors.append(f"{label}.completion_mask: expected one-channel grayscale mode 1 or L")
                mhist = mask.convert("L").histogram()
                gray_transition_pixels = sum(mhist[1:255])
                if gray_transition_pixels:
                    warnings.append(f"{label}.completion_mask: {gray_transition_pixels} gray transition pixels require manual feathering review")
                result["completion_mask"] = {
                    "status": "passed" if mask_ok else "failed",
                    "permitted_white_pixels": mhist[255], "protected_black_pixels": mhist[0],
                    "gray_transition_pixels": gray_transition_pixels,
                    "meaning": "white permits completion; black protects original pixels; gray feathering requires manual review; fidelity not verified"}
        normalized = dict(layer, **values)
        normalized["id"] = display_id
        inspect_coverage(normalized, rgba, result, errors)
        result["status"] = "failed" if len(errors) > error_start else "passed"
        loaded_layers.append((values["z"], index, normalized, rgba, result))
    duplicates = sorted(z for z, count in Counter(valid_z).items() if count > 1)
    if duplicates:
        warnings.append(f"Repeated z values {duplicates}; order resolves by z then input index")
    loaded_layers.sort(key=lambda item: (item[0], item[1]))
    report["assembly_order"] = [item[2]["id"] for item in loaded_layers]

    # Resolve all output targets before writing even the report, including symlinks.
    targets = {name: (out_dir / name).resolve() for name in OUTPUT_NAMES}
    conflicts = [name for name, target in targets.items() if target in inputs]
    if conflicts:
        print("Refusing to overwrite input file(s): " + ", ".join(conflicts), file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    if canvas_size and source_image is not None:
        composite = Image.new("RGBA", canvas_size)
        for _, _, layer, image, result in loaded_layers:
            placed, method = render_layer(image, layer, canvas_size)
            composite = Image.alpha_composite(composite, placed)
            result["render_method"] = method
        composite.save(targets["composite.png"])
        report["outputs"]["composite"] = str(targets["composite.png"])
        report["source_comparison"] = compare_reference(
            composite, source_image, targets["reference-diff.png"])
        report["outputs"]["reference_diff"] = str(targets["reference-diff.png"])
    else:
        report["source_comparison"] = {"status": "not-available"}
    contact_sheet([(item[2], item[3]) for item in loaded_layers],
                  targets["edge-contact-sheet.png"])
    report["outputs"]["edge_contact_sheet"] = str(targets["edge-contact-sheet.png"])
    report["automated_status"] = "failed" if errors else "passed"
    report["outputs"]["report"] = str(targets["report.json"])
    targets["report.json"].write_text(json.dumps(report, ensure_ascii=False, indent=2,
                                               allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"automated_status": report["automated_status"],
                      "source_comparison": report["source_comparison"]["status"],
                      "errors": len(errors), "report": str(targets["report.json"])},
                     ensure_ascii=False))
    return 1 if errors else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        return inspect(args.manifest.resolve(), args.out_dir.resolve())
    except (OSError, ValueError, OverflowError, MemoryError) as exc:
        print(f"Inspection failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
