"""Run Ultralytics ByteTrack / BoT-SORT on a video or webcam.

The 2023 notebook called `model.track(..., persist=True, conf=0.20)` and
drew a 30-point trail. It crashed when a frame had boxes but no track id
(`boxes.id` is None). This script keeps that pipeline and skips the trail
on those frames.
"""

from __future__ import annotations

import argparse
import os
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    if width is None and height is None:
        return image
    h, w = image.shape[:2]
    if width is None:
        scale = height / float(h)
        dim = (int(w * scale), height)
    else:
        scale = width / float(w)
        dim = (width, int(h * scale))
    return cv2.resize(image, dim, interpolation=inter)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Track aircraft in a video with a trained YOLOv8 weight.")
    parser.add_argument("--weights", required=True, help="Path to a .pt (e.g. original-data/.../ats4.pt)")
    parser.add_argument("--source", required=True, help="Video path, webcam index, or URL")
    parser.add_argument("--conf", type=float, default=0.20, help="2023 demo used 0.20 for distant targets")
    parser.add_argument("--display-width", type=int, default=1000)
    parser.add_argument("--trail", action="store_true", help="Draw the 30-point centre trail")
    parser.add_argument("--save", type=Path, default=None, help="Optional annotated mp4 path")
    parser.add_argument("--no-show", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
    from ultralytics import YOLO

    model = YOLO(args.weights)
    source = int(args.source) if str(args.source).isdigit() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise SystemExit(f"cannot open source: {args.source}")

    writer = None
    track_history: dict[int, list] = defaultdict(list)

    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break

        results = model.track(frame, persist=True, conf=args.conf)
        annotated = results[0].plot()

        if args.trail:
            boxes = results[0].boxes
            if boxes is not None and boxes.id is not None and len(boxes):
                xywh = boxes.xywh.cpu()
                ids = boxes.id.int().cpu().tolist()
                for box, track_id in zip(xywh, ids):
                    x, y, _, _ = box.tolist()
                    hist = track_history[track_id]
                    hist.append((float(x), float(y)))
                    if len(hist) > 30:
                        hist.pop(0)
                    points = np.hstack(hist).astype(np.int32).reshape((-1, 1, 2))
                    cv2.polylines(annotated, [points], isClosed=False, color=(230, 230, 230), thickness=10)

        if args.save:
            if writer is None:
                h, w = annotated.shape[:2]
                fps = cap.get(cv2.CAP_PROP_FPS) or 25
                args.save.parent.mkdir(parents=True, exist_ok=True)
                writer = cv2.VideoWriter(
                    str(args.save),
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    fps,
                    (w, h),
                )
            writer.write(annotated)

        if not args.no_show:
            cv2.imshow("YOLOv8 Tracking", resize_with_aspect_ratio(annotated, args.display_width))
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    if writer is not None:
        writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
