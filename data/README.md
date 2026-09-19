# Dataset layout

This folder holds the Ultralytics config only. **Images and labels are not in git.**

The 2023 set was collected as YouTube screenshots (often with the player chrome still visible). Those frames stay in the local `original-data/` dump. To train, copy or rebuild a set into:

```text
data/
  data.yaml
  images/train/   *.png | *.jpg
  images/val/
  labels/train/   YOLO txt, same stem as the image
  labels/val/
```

Each label line is `class cx cy w h` in **normalised** coordinates (`0–1`):

```text
1 0.512 0.408 0.086 0.052
```

| id | name |
| --- | --- |
| 0 | `civil_aircraft` |
| 1 | `fighter` |
| 2 | `bomber` |
| 3 | `other_military_aircraft` |
| 4 | `missile` |

Do not write class names in the txt (the 2023 dump has a handful of those; Ultralytics will reject them). Full notes: [`docs/dataset.md`](../docs/dataset.md).
