#!/usr/bin/env python3
"""Extract native video frames with traceable PTS and paginated contact sheets."""
import argparse
import bisect
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import statistics
import subprocess
import sys


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def rate(value):
    try:
        numerator, denominator = str(value).split("/")
        result = float(numerator) / float(denominator)
        return result if math.isfinite(result) and result > 0 else None
    except (ValueError, ZeroDivisionError):
        return None


def run(argv):
    result = subprocess.run(argv, capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError(f"{Path(argv[0]).name} failed ({result.returncode}): {result.stderr[-2500:]}")
    return result.stdout


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def select_filter(indices):
    groups = []
    start = previous = indices[0]
    for index in indices[1:] + [None]:
        if index is not None and index == previous + 1:
            previous = index
            continue
        groups.append(f"eq(n\\,{start})" if start == previous else f"between(n\\,{start}\\,{previous})")
        start = previous = index
    return "select=" + "+".join(groups)


def contacts(out_dir, records, image_module, draw_module):
    sheets = []
    columns, page_size, cell_width, image_height, label_height = 5, 30, 240, 170, 34
    for offset in range(0, len(records), page_size):
        page = records[offset:offset + page_size]
        rows = math.ceil(len(page) / columns)
        sheet = image_module.new("RGB", (columns * cell_width, rows * (image_height + label_height)), "#e8e8e8")
        draw = draw_module.Draw(sheet)
        for slot, record in enumerate(page):
            x, y = (slot % columns) * cell_width, (slot // columns) * (image_height + label_height)
            with image_module.open(out_dir / record["path"]) as source:
                thumb = source.convert("RGB")
                thumb.thumbnail((cell_width - 8, image_height - 8))
                sheet.paste(thumb, (x + (cell_width - thumb.width) // 2, y + (image_height - thumb.height) // 2))
            label = f"frame {record['source_frame_index']}  t={record['source_time_seconds']:.6f}s"
            draw.text((x + 4, y + image_height + 3), label, fill="black")
        name = f"contact-sheet-{offset // page_size + 1:03d}.jpg"
        sheet.save(out_dir / name, quality=92)
        sheets.append(name)
    return sheets


def execute(args):
    try:
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise RuntimeError("Missing Pillow; install it in the chosen Python environment before extraction.") from exc
    for dependency in ("ffprobe", "ffmpeg"):
        if shutil.which(dependency) is None:
            raise RuntimeError(f"Missing {dependency}; provide it on PATH before extraction.")
    if not math.isfinite(args.start) or args.start < 0:
        raise ValueError("--start must be finite and >= 0.")
    if args.end is not None and (not math.isfinite(args.end) or args.end <= args.start):
        raise ValueError("--end must be finite and greater than --start.")
    if args.fps is not None and (not math.isfinite(args.fps) or args.fps <= 0):
        raise ValueError("--fps must be finite and positive.")
    if args.max_frames < 1:
        raise ValueError("--max-frames must be positive.")
    video = Path(args.video).expanduser().resolve(strict=True)
    if not video.is_file():
        raise ValueError("--video must identify an existing regular file.")
    out_dir = Path(args.out_dir).expanduser().resolve()
    if out_dir == video or (out_dir.exists() and (not out_dir.is_dir() or any(out_dir.iterdir()))):
        raise ValueError("Output directory must be absent or empty; refusing to overwrite existing content or input.")
    before = video.stat()
    source_hash = digest(video)
    metadata = json.loads(run([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_streams", "-show_frames", "-show_format",
        "-show_entries", "stream=index,codec_name,width,height,avg_frame_rate,r_frame_rate,time_base,sample_aspect_ratio,color_space,color_transfer,color_range:stream_side_data=rotation:format=duration,size:frame=pts,pts_time,best_effort_timestamp_time,pkt_duration_time,duration_time",
        "-of", "json", str(video)
    ]))
    if not metadata.get("streams") or not metadata.get("frames"):
        raise ValueError("No decodable frames in the first video stream.")
    raw_stream = metadata["streams"][0]
    stream = {key: raw_stream.get(key) for key in (
        "index", "codec_name", "width", "height", "avg_frame_rate", "r_frame_rate", "time_base",
        "sample_aspect_ratio", "color_space", "color_transfer", "color_range"
    )}
    stream["rotation_degrees"] = [item["rotation"] for item in raw_stream.get("side_data_list", []) if "rotation" in item]
    frames = []
    for index, raw in enumerate(metadata["frames"]):
        original_pts = number(raw.get("pts_time"))
        best_effort_pts = number(raw.get("best_effort_timestamp_time"))
        chosen = original_pts if original_pts is not None else best_effort_pts
        if chosen is None:
            raise ValueError(f"Frame {index} lacks a usable timestamp; cannot produce traceable timing.")
        if frames and chosen < frames[-1]["timestamp"]:
            raise ValueError("Source timestamps are not monotonic; cannot safely map frames.")
        frames.append({"index": index, "timestamp": chosen, "raw": raw,
                       "original_pts": original_pts, "best_effort_pts": best_effort_pts})
    origin = frames[0]["timestamp"]
    times = [frame["timestamp"] - origin for frame in frames]
    intervals = [right - left for left, right in zip(times, times[1:])]
    positive_intervals = [value for value in intervals if value > 0]
    last_duration = number(frames[-1]["raw"].get("duration_time")) or number(frames[-1]["raw"].get("pkt_duration_time"))
    duration_basis = "last_frame_duration"
    if last_duration is None or last_duration <= 0:
        last_duration = statistics.median(positive_intervals) if positive_intervals else None
        duration_basis = "median_pts_interval_estimate"
    if last_duration is None:
        source_rate = rate(stream.get("avg_frame_rate")) or rate(stream.get("r_frame_rate"))
        last_duration = 1 / source_rate if source_rate else None
        duration_basis = "metadata_frame_rate_estimate"
    if last_duration is None:
        raise ValueError("Cannot determine the final frame interval; source has no duration or usable frame rate.")
    source_end = times[-1] + last_duration
    end = min(args.end, source_end) if args.end is not None else source_end
    if args.start >= end:
        raise ValueError("Requested interval does not intersect the video's frame timeline.")
    eligible = [index for index, time in enumerate(times) if args.start <= time < end]
    if not eligible:
        raise ValueError("No native frame timestamps in requested interval; choose a wider interval.")
    selected = {}
    sample_count = None
    warnings = []
    if args.end is not None and args.end > source_end:
        warnings.append("Requested end exceeds source end; effective range is clipped and recorded below.")
    if args.all_frames:
        selected = {index: None for index in eligible}
    else:
        requested_slots = (end - args.start) * args.fps
        if not math.isfinite(requested_slots):
            raise ValueError("Requested sampling count is too large; lower --fps or narrow the interval.")
        sample_count = max(1, math.ceil(requested_slots - 1e-10))
        if sample_count > args.max_frames:
            raise ValueError(f"Requested {sample_count} sampling slots exceed --max-frames {args.max_frames}; narrow the interval, lower --fps or explicitly raise the limit.")
        eligible_times = [times[index] for index in eligible]
        for slot in range(sample_count):
            target = args.start + slot / args.fps
            position = bisect.bisect_left(eligible_times, target)
            candidates = [candidate for candidate in (position - 1, position) if 0 <= candidate < len(eligible)]
            nearest = min(candidates, key=lambda candidate: (abs(eligible_times[candidate] - target), candidate))
            selected.setdefault(eligible[nearest], []).append(target)
        if len(selected) < sample_count:
            warnings.append("Multiple requested sampling times mapped to the same native frame; all targets remain recorded, no frames synthesized.")
    if len(selected) > args.max_frames:
        raise ValueError(f"Requested {len(selected)} native frames exceed --max-frames {args.max_frames}; narrow the interval or explicitly raise the limit.")
    indices = sorted(selected)
    out_dir.mkdir(parents=True, exist_ok=True)
    frames_dir = out_dir / "frames"
    frames_dir.mkdir()
    run(["ffmpeg", "-nostdin", "-v", "error", "-n", "-noautorotate", "-i", str(video), "-map", "0:v:0",
         "-vf", select_filter(indices), "-fps_mode", "passthrough", "-frames:v", str(len(indices)),
         "-threads", "1", str(frames_dir / "frame-%06d.png")])
    extracted = sorted(frames_dir.glob("frame-*.png"))
    if len(extracted) != len(indices):
        raise RuntimeError(f"Extraction mismatch: requested {len(indices)} native frames, got {len(extracted)}; no valid manifest written.")
    records = []
    for path, index in zip(extracted, indices):
        frame = frames[index]
        with Image.open(path) as extracted_image:
            extracted_image.load()
            size = list(extracted_image.size)
        records.append({"path": path.relative_to(out_dir).as_posix(), "source_frame_index": index,
                        "source_pts": frame["raw"].get("pts"), "source_pts_time_seconds": frame["original_pts"],
                        "source_best_effort_pts_time_seconds": frame["best_effort_pts"],
                        "timestamp_kind": "original_pts" if frame["original_pts"] is not None else "best_effort_pts",
                        "source_time_seconds": times[index], "sampling_target_times_seconds": selected[index],
                        "dimensions_px": size})
    after = video.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise RuntimeError("Source changed during extraction; no valid manifest written.")
    sheets = contacts(out_dir, records, Image, ImageDraw)
    manifest = {
        "schema_version": "1.0", "source": {"path": os.path.relpath(video, out_dir), "sha256": source_hash,
        "size_bytes": before.st_size, "stream": stream, "frame_count": len(frames),
        "first_frame_timestamp_seconds": origin, "timeline_end_seconds": source_end,
        "timeline_end_basis": duration_basis, "pts_intervals": {
            "min_seconds": min(intervals) if intervals else None, "max_seconds": max(intervals) if intervals else None,
            "median_seconds": statistics.median(intervals) if intervals else None,
            "variable": max(intervals) - min(intervals) > 1e-5 if intervals else None}},
        "sampling": {"mode": "all-native-frames" if args.all_frames else "nearest-native-frame",
                     "requested_fps": args.fps, "requested_start_seconds": args.start, "requested_end_seconds": args.end,
                     "effective_start_seconds": args.start, "effective_end_seconds": end, "end_exclusive": True,
                     "requested_sample_count": sample_count, "native_output_count": len(records), "max_frames": args.max_frames},
        "warnings": warnings, "contact_sheets": sheets, "frames": records
    }
    with (out_dir / "manifest.json").open("x", encoding="utf-8") as output:
        json.dump(manifest, output, indent=2, ensure_ascii=False, allow_nan=False)
    print(json.dumps({"output_directory": str(out_dir), "native_frames": len(records), "warnings": warnings}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--video", required=True, help="Input local video path.")
    parser.add_argument("--out-dir", required=True, help="New or empty output directory.")
    parser.add_argument("--start", type=float, default=0.0, help="Inclusive seconds relative to first video frame.")
    parser.add_argument("--end", type=float, help="Exclusive seconds relative to first video frame.")
    sampling = parser.add_mutually_exclusive_group(required=True)
    sampling.add_argument("--fps", type=float, help="Sample targets per second; choose nearest native frames.")
    sampling.add_argument("--all-frames", action="store_true", help="Extract all native frames in interval.")
    parser.add_argument("--max-frames", type=int, default=1000, help="Limit native output frames and requested sampling slots.")
    args = parser.parse_args()
    try:
        execute(args)
    except (ValueError, RuntimeError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
