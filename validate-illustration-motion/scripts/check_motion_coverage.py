#!/usr/bin/env python3
"""Check effective alpha coverage at explicit affine motion samples; never edit assets."""
import argparse
import json
import math
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ImportError:
    print("Missing Pillow; use a Python environment with Pillow before coverage checks.", file=sys.stderr)
    raise SystemExit(1)

MAX_SOURCE_PIXELS = 16_000_000
MAX_TOTAL_SOURCE_PIXELS = 64_000_000
MAX_RASTER_PIXELS = 8_000_000
MAX_TOTAL_RASTER_SAMPLES = 200_000_000
MAX_GROUP_FRAME_SAMPLES = 10_000
MAX_VIEWPORTS = 16
MAX_LAYERS = 64
MAX_GROUPS = 32
MAX_FRAMES = 256


def number(value, label, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: expected a finite number")
    result = float(value)
    if not math.isfinite(result) or (positive and result <= 0):
        raise ValueError(f"{label}: expected a {'positive ' if positive else ''}finite number")
    return result


def vector(value, size, label):
    if not isinstance(value, list) or len(value) != size:
        raise ValueError(f"{label}: expected {size} numbers")
    return [number(v, label) for v in value]


def identifier(value, label):
    if not isinstance(value, str) or not value.strip() or len(value) > 128:
        raise ValueError(f"{label}: expected a nonempty string, up to 128 characters")
    return value


def sequence(value, label, limit):
    if not isinstance(value, list) or not value or len(value) > limit:
        raise ValueError(f"{label}: expected 1..{limit} items")
    return value


def matrix(value, label):
    result = vector(value, 6, label)
    if abs(result[0] * result[3] - result[1] * result[2]) < 1e-12:
        raise ValueError(f"{label}: matrix must be invertible")
    return result


def multiply(left, right):
    a, b, c, d, e, f = left
    g, h, i, j, k, l = right
    return [a*g+c*h, b*g+d*h, a*i+c*j, b*i+d*j, a*k+c*l+e, b*k+d*l+f]


def inverse(value):
    a, b, c, d, e, f = value
    determinant = a*d-b*c
    if not math.isfinite(determinant) or abs(determinant) < 1e-12:
        raise ValueError("composed matrix is singular or nonfinite")
    result = [d/determinant, -b/determinant, -c/determinant, a/determinant,
              (c*f-d*e)/determinant, (b*e-a*f)/determinant]
    if not all(math.isfinite(v) for v in result):
        raise ValueError("composed matrix is nonfinite")
    return result


def prepare(config, config_path):
    if not isinstance(config, dict) or config.get("version") != 1:
        raise ValueError("version must be 1")
    threshold = config.get("alpha_threshold", 250)
    if isinstance(threshold, bool) or not isinstance(threshold, int) or not 1 <= threshold <= 255:
        raise ValueError("alpha_threshold must be an integer in 1..255")
    density = number(config.get("sample_density", 1), "sample_density", positive=True)
    if density > 8:
        raise ValueError("sample_density exceeds safety limit of 8")
    viewports = sequence(config.get("viewports"), "viewports", MAX_VIEWPORTS)
    paths, source_sizes, prepared, viewport_ids = set(), {}, [], set()
    total_raster_samples = 0
    group_frame_samples = 0
    for vi, viewport in enumerate(viewports):
        if not isinstance(viewport, dict):
            raise ValueError(f"viewport {vi}: expected an object")
        vid = identifier(viewport.get("id"), "viewport id")
        if vid in viewport_ids:
            raise ValueError(f"duplicate viewport id: {vid}")
        viewport_ids.add(vid)
        vw = number(viewport.get("width"), f"{vid}.width", positive=True)
        vh = number(viewport.get("height"), f"{vid}.height", positive=True)
        rx, ry, rw, rh = vector(viewport.get("required_rect"), 4, f"{vid}.required_rect")
        if rw <= 0 or rh <= 0 or rx < 0 or ry < 0 or rx+rw > vw+1e-9 or ry+rh > vh+1e-9:
            raise ValueError(f"{vid}.required_rect must be positive and inside viewport")
        if rw*density > MAX_RASTER_PIXELS or rh*density > MAX_RASTER_PIXELS:
            raise ValueError(f"{vid}: raster exceeds safety limit")
        raster_size = (math.ceil(rw*density), math.ceil(rh*density))
        if raster_size[0]*raster_size[1] > MAX_RASTER_PIXELS:
            raise ValueError(f"{vid}: raster exceeds {MAX_RASTER_PIXELS} pixels")
        layers = {}
        for layer in sequence(viewport.get("layers"), f"{vid}.layers", MAX_LAYERS):
            lid = identifier(layer.get("id"), "layer id")
            if lid in layers:
                raise ValueError(f"{vid}: duplicate layer id {lid}")
            file_value = layer.get("file")
            if not isinstance(file_value, str) or not file_value:
                raise ValueError(f"{vid}.{lid}: file is required")
            path = (config_path.parent / file_value).resolve()
            if not path.is_file():
                raise ValueError(f"{vid}.{lid}: source file does not exist: {path}")
            lw, lh = vector(layer.get("logical_size"), 2, f"{vid}.{lid}.logical_size")
            bx, by = vector(layer.get("base_position"), 2, f"{vid}.{lid}.base_position")
            if lw <= 0 or lh <= 0:
                raise ValueError(f"{vid}.{lid}: logical_size must be positive")
            if path not in source_sizes:
                with Image.open(path) as source:
                    if source.mode != "RGBA" or getattr(source, "n_frames", 1) != 1:
                        raise ValueError(f"{path}: expected a static RGBA image with effective alpha")
                    sw, sh = source.size
                    if sw*sh > MAX_SOURCE_PIXELS:
                        raise ValueError(f"{path}: source exceeds {MAX_SOURCE_PIXELS} pixels")
                    source_sizes[path] = (sw, sh)
                if sum(w*h for w, h in source_sizes.values()) > MAX_TOTAL_SOURCE_PIXELS:
                    raise ValueError("total source pixels exceed safety limit")
            paths.add(path)
            sw, sh = source_sizes[path]
            layers[lid] = {"path": path, "base": [lw/sw, 0, 0, lh/sh, bx, by],
                           "logical_size": [lw, lh], "base_position": [bx, by]}
        groups, group_ids = [], set()
        for group in sequence(viewport.get("groups"), f"{vid}.groups", MAX_GROUPS):
            gid = identifier(group.get("id"), "group id")
            ids = sequence(group.get("layer_ids"), f"{vid}.{gid}.layer_ids", MAX_LAYERS)
            if gid in group_ids or len(set(ids)) != len(ids) or any(lid not in layers for lid in ids):
                raise ValueError(f"{vid}.{gid}: duplicate group or unknown/duplicate layer ids")
            group_ids.add(gid)
            groups.append({"id": gid, "layer_ids": ids})
        frames, frame_ids = [], set()
        for frame in sequence(viewport.get("frames"), f"{vid}.frames", MAX_FRAMES):
            fid = identifier(frame.get("id"), "frame id")
            if fid in frame_ids:
                raise ValueError(f"{vid}: duplicate frame id {fid}")
            frame_ids.add(fid)
            time = number(frame.get("time_ms"), f"{vid}.{fid}.time_ms")
            scene = matrix(frame.get("scene_to_viewport"), f"{vid}.{fid}.scene_to_viewport")
            transforms = frame.get("layer_transforms")
            if not isinstance(transforms, dict) or set(transforms) != set(layers):
                raise ValueError(f"{vid}.{fid}: layer_transforms must explicitly contain exactly all layer ids")
            transforms = {lid: matrix(transforms[lid], f"{vid}.{fid}.{lid}") for lid in layers}
            frames.append({"id": fid, "time_ms": time, "scene_to_viewport": scene,
                           "layer_transforms": transforms})
        total_raster_samples += raster_size[0]*raster_size[1]*len(frames)*len(groups)
        group_frame_samples += len(frames)*len(groups)
        if total_raster_samples > MAX_TOTAL_RASTER_SAMPLES:
            raise ValueError("total raster samples exceed safety limit; split input into smaller trials")
        if group_frame_samples > MAX_GROUP_FRAME_SAMPLES:
            raise ValueError("group/frame sample count exceeds safety limit; split input into smaller trials")
        prepared.append({"id": vid, "width": vw, "height": vh,
                         "rect": [rx, ry, rw, rh], "size": raster_size,
                         "layers": layers, "groups": groups, "frames": frames})
    return threshold, density, prepared, paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="JSON input; asset paths are relative to this file")
    parser.add_argument("--report", type=Path, help="new JSON report path; defaults to stdout")
    parser.add_argument("--mask-dir", type=Path, help="write new alpha diagnostic PNGs into this directory")
    args = parser.parse_args()
    alpha_sources = {}
    try:
        config_path = args.config.resolve()
        if config_path.stat().st_size > 4_000_000:
            raise ValueError("config exceeds 4 MB safety limit")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        threshold, density, viewports, sources = prepare(config, config_path)
        input_paths = sources | {config_path}
        report_path = args.report.resolve() if args.report else None
        mask_dir = args.mask_dir.resolve() if args.mask_dir else None
        output_paths = []
        if report_path:
            output_paths.append(report_path)
        if mask_dir:
            for vi, viewport in enumerate(viewports):
                for gi, _ in enumerate(viewport["groups"]):
                    for fi, _ in enumerate(viewport["frames"]):
                        output_paths.append(mask_dir / f"coverage-v{vi:02d}-g{gi:02d}-f{fi:04d}.png")
        if len(output_paths) != len(set(output_paths)):
            raise ValueError("output paths collide")
        for path in output_paths:
            if path in input_paths or path.exists():
                raise ValueError(f"refusing to overwrite input or existing output: {path}")
        # Validate all inputs and output names before decoding; retain alpha channels only.
        for path in sources:
            with Image.open(path) as source:
                alpha_sources[path] = source.getchannel("A")
        results, total_failures = [], 0
        for vi, viewport in enumerate(viewports):
            rx, ry, rw, rh = viewport["rect"]
            w, h = viewport["size"]
            pixel_to_viewport = [rw/w, 0, 0, rh/h, rx, ry]
            groups = []
            for gi, group in enumerate(viewport["groups"]):
                samples = []
                for fi, frame in enumerate(viewport["frames"]):
                    combined = Image.new("L", (w, h), 0)
                    for lid in group["layer_ids"]:
                        layer = viewport["layers"][lid]
                        total = multiply(frame["scene_to_viewport"],
                                         multiply(frame["layer_transforms"][lid], layer["base"]))
                        sampling = multiply(inverse(total), pixel_to_viewport)
                        a, b, c, d, e, f = sampling
                        mapped = alpha_sources[layer["path"]].transform(
                            (w, h), Image.Transform.AFFINE, (a, c, e, b, d, f),
                            resample=Image.Resampling.BILINEAR, fillcolor=0)
                        updated = ImageChops.screen(combined, mapped)
                        mapped.close()
                        combined.close()
                        combined = updated
                    histogram = combined.histogram()
                    valid = sum(histogram[threshold:])
                    missing = w*h-valid
                    failed = combined.point([255 if a < threshold else 0 for a in range(256)])
                    bbox = failed.getbbox()
                    failed.close()
                    logical_bounds = None
                    if bbox:
                        logical_bounds = [rx+bbox[0]*rw/w, ry+bbox[1]*rh/h,
                                          (bbox[2]-bbox[0])*rw/w, (bbox[3]-bbox[1])*rh/h]
                    entry = {"frame_id": frame["id"], "time_ms": frame["time_ms"],
                             "status": "passed_sample" if not missing else "failed_sample",
                             "covered_fraction": valid/(w*h), "uncovered_pixels": missing,
                             "raster_pixels": w*h, "uncovered_bounds_viewport": logical_bounds,
                             "uncovered_touches_required_edge": bool(bbox and
                                 (bbox[0] == 0 or bbox[1] == 0 or bbox[2] == w or bbox[3] == h))}
                    if mask_dir:
                        mask_dir.mkdir(parents=True, exist_ok=True)
                        path = mask_dir / f"coverage-v{vi:02d}-g{gi:02d}-f{fi:04d}.png"
                        with path.open("xb") as output:
                            combined.save(output, format="PNG")
                        entry["alpha_diagnostic_path"] = str(path)
                    combined.close()
                    samples.append(entry)
                    total_failures += bool(missing)
                worst = min(samples, key=lambda row: row["covered_fraction"])
                groups.append({"id": group["id"], "layer_ids": group["layer_ids"],
                               "worst_sample": worst, "samples": samples})
            times = sorted(frame["time_ms"] for frame in viewport["frames"])
            results.append({"id": viewport["id"], "viewport_logical_size": [viewport["width"], viewport["height"]],
                            "required_rect": viewport["rect"], "raster_size": [w, h],
                            "sampled_time_range_ms": [times[0], times[-1]],
                            "sampled_times_ms": times, "groups": groups})
        report = {"version": 1, "status": "all_samples_passed" if not total_failures else "sample_coverage_failed",
                  "scope": "Explicit sampled affine states at the reported raster precision only",
                  "alpha_threshold": threshold, "sample_density": density,
                  "resampling": "Pillow bilinear alpha; source-over alpha compositing",
                  "failed_group_frame_samples": total_failures,
                  "unverified": ["Continuous time between samples and extrema not explicitly sampled",
                                 "Future or omitted frames, viewport sizes and device conditions",
                                 "Nonlinear deformation, perspective, shader effects, masks and clipping not baked into input",
                                 "Actual renderer filtering, postprocessing and visual quality",
                                 "Sub-grid holes and details smaller than the declared sampling precision"],
                  "viewports": results}
        payload = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if report_path:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            with report_path.open("x", encoding="utf-8") as output:
                output.write(payload)
        else:
            sys.stdout.write(payload)
        return 2 if total_failures else 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError, Image.DecompressionBombError) as error:
        sys.stderr.write(f"coverage check failed: {error}\n")
        return 1
    finally:
        for alpha in alpha_sources.values():
            alpha.close()


if __name__ == "__main__":
    sys.exit(main())
