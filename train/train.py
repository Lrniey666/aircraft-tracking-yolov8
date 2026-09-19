"""Train the five-class YOLOv8 aircraft detector.

Defaults follow the 2023 RTX 3070 coursework runs (ultralytics 8.0.x,
imgsz 640, mosaic/augment on). Point `--data` at a YOLO yaml whose images
actually exist — this repository does not ship the 2023 frames.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "data.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train YOLOv8 on the aircraft classes.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="Ultralytics data yaml")
    parser.add_argument("--model", default="yolov8s.pt", help="Checkpoint or official size (n/s/m/l/x)")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch", type=int, default=16, help="2023 RTX 3070 used 25–27; 16 is safer")
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--name", default="aircraft-yolov8")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--device", default="")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.data.is_file():
        raise SystemExit(f"data yaml not found: {args.data}")

    os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
    from ultralytics import YOLO

    model = YOLO(str(args.model))
    model.train(
        data=str(args.data.resolve()),
        epochs=args.epochs,
        batch=args.batch,
        imgsz=args.imgsz,
        name=args.name,
        workers=args.workers,
        resume=args.resume,
        device=args.device or None,
        cache=True,
        augment=True,
        project=str(ROOT / "runs" / "detect"),
    )


if __name__ == "__main__":
    main()
