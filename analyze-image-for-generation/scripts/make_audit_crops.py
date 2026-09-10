#!/usr/bin/env python3
"""Create non-destructive evidence crops for visual-blueprint claim audits."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create padded image crops from normalized audit regions."
    )
    parser.add_argument("--input", required=True, type=Path, help="Source raster image.")
    parser.add_argument(
        "--regions",
        required=True,
        type=Path,
        help="JSON file containing a regions array.",
    )
    parser.add_argument(
        "--out-dir", required=True, type=Path, help="Directory for PNG crops and manifest."
    )
    parser.add_argument(
        "--padding",
        type=float,
        default=0.035,
        help="Extra normalized padding around each box (default: 0.035).",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="Optional output scale using Lanczos; keep 1.0 for unaltered evidence.",
    )
    return parser.parse_args()


def load_regions(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    regions = data.get("regions") if isinstance(data, dict) else data
    if not isinstance(regions, list) or not regions:
        raise ValueError("The regions JSON must contain a non-empty regions array.")
    return regions


def safe_id(value: Any, index: int) -> str:
    raw = str(value or f"crop-{index:03d}").strip()
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", raw).strip("-._")
    return cleaned or f"crop-{index:03d}"


def normalized_box(region: dict[str, Any]) -> tuple[float, float, float, float]:
    box = region.get("box")
    if not isinstance(box, list) or len(box) != 4:
        raise ValueError(f"Region {region!r} must have box [left, top, right, bottom].")
    left, top, right, bottom = (float(value) for value in box)
    if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
        raise ValueError(f"Normalized box is outside 0..1 or has no area: {box!r}")
    return left, top, right, bottom


def padded_pixel_box(
    box: tuple[float, float, float, float],
    width: int,
    height: int,
    padding: float,
) -> tuple[int, int, int, int]:
    left, top, right, bottom = box
    return (
        max(0, round((left - padding) * width)),
        max(0, round((top - padding) * height)),
        min(width, round((right + padding) * width)),
        min(height, round((bottom + padding) * height)),
    )


def main() -> None:
    args = parse_args()
    if args.padding < 0 or args.padding >= 0.5:
        raise ValueError("--padding must be at least 0 and below 0.5.")
    if args.scale <= 0:
        raise ValueError("--scale must be greater than 0.")

    source = args.input.resolve()
    regions_path = args.regions.resolve()
    output_dir = args.out_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGBA")

    width, height = image.size
    regions = load_regions(regions_path)
    seen_ids: set[str] = set()
    manifest: dict[str, Any] = {
        "source": str(source),
        "source_size": [width, height],
        "padding": args.padding,
        "scale": args.scale,
        "crops": [],
    }

    for index, region in enumerate(regions, start=1):
        crop_id = safe_id(region.get("id"), index)
        if crop_id in seen_ids:
            raise ValueError(f"Duplicate crop id: {crop_id}")
        seen_ids.add(crop_id)

        box = normalized_box(region)
        pixel_box = padded_pixel_box(box, width, height, args.padding)
        crop = image.crop(pixel_box)
        if args.scale != 1:
            target = (
                max(1, round(crop.width * args.scale)),
                max(1, round(crop.height * args.scale)),
            )
            crop = crop.resize(target, Image.Resampling.LANCZOS)

        output_path = output_dir / f"{index:03d}-{crop_id}.png"
        crop.save(output_path)
        manifest["crops"].append(
            {
                "id": crop_id,
                "label": str(region.get("label", "")),
                "normalized_box": list(box),
                "pixel_box_with_padding": list(pixel_box),
                "output": str(output_path),
            }
        )

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(manifest_path)


if __name__ == "__main__":
    main()
