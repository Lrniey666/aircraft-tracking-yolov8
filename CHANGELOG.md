# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- GitHub showcase tree: `tools/sidcgt.py`, `train/train.py`, `infer/track.py`, `data/data.yaml`, thin notebooks, bilingual README (zh-Hant / en), dataset / training / inference notes.
- MIT licence, contributing guide, hero artwork, classroom result QR, and the `my-yolov8s19` results CSV.

### Changed

- SIDCGT: removed the first duplicate `take_screenshot`; Alt+Z is polled with `after()` so Stop can run. Buttons and the hot-key match the 2023 file.
- Tracking: skip the centre trail when `boxes.id` is `None` (the 2023 notebook raised `AttributeError` on `all1.mp4`).
- Data yaml uses relative paths and drops the leftover Roboflow face-detection block.

### Removed

- Working dump (`original-data/`, ~3.2 GB) is gitignored: YouTube frames, test films, `.pt` weights, LabelImg.exe, the FDDB zip, and failed-run plots stay on disk only.

## [1.0.0] - 2023-12-01

### Added

- Coursework hand-in for master’s deep learning, academic year ROC 112.
- Five-class detector (`civil_aircraft`, `fighter`, `bomber`, `other_military_aircraft`, `missile`) trained with Ultralytics YOLOv8 on an RTX 3070.
- SIDCGT v1.1 screenshot utility and LabelImg class list.
- Tracking notebook using `model.track(persist=True, conf=0.20)` and `ats4.pt`.
