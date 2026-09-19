# Contributing

Languages: [繁體中文](../CONTRIBUTING.md) · [English](CONTRIBUTING.en.md)

This repository is archived 2023 coursework. Documentation fixes, environment notes and showcase-script defects that stop a fresh clone from running are welcome. Treat the 2023 notebooks as artefacts first.

## Before you start

1. Read [`../README.md`](../README.md) and [`README.md`](README.md).
2. Class-name or default-hyperparameter changes must land in [`../data/data.yaml`](../data/data.yaml), [`dataset.md`](dataset.md) and [`training.md`](training.md) together.
3. When they disagree: **2023 submitted behaviour wins**. Fix the docs. Showcase scripts may only repair defects that made the original file unusable, and the drift belongs in `docs/`.

## Conventions

| Item | Rule |
| --- | --- |
| Public copy | Traditional Chinese in `README.md`; English in `README.en.md` — edit both |
| Dates | `YYYY-MM-DD`, Taipei |
| Changelog | `## [Unreleased]` in `CHANGELOG.md` (Keep a Changelog 2.0.0) |
| Line endings | LF (`.gitattributes`) |

## Please do not

- Commit `original-data/`, YouTube frames, test mp4s, `*.pt`, the FDDB zip, or `labelImg.exe`
- Hard-code absolute machine paths or accounts
- Describe the leftover face-detection dataset as this project’s training set
- Call mAP50 0.28 state of the art, or omit the near-zero missile val
- Modernise SIDCGT / tracking for taste and present it as the 2023 hand-in

Ask first before irreversible git history changes.

## After a change

1. Note it under `## [Unreleased]` in `CHANGELOG.md`
2. Keep the two README tours in step if you touch the hero, install steps or tree
3. If `tools/sidcgt.py`, `train/train.py` or `infer/track.py` change, record the drift from the 2023 files in the matching `docs/` note
