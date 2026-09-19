# 訓練

語言：[繁體中文](../README.md) · [English](README.en.md)

展示入口：[`train/train.py`](../train/train.py)、[`notebooks/train.ipynb`](../notebooks/train.ipynb)。

## 2023 機器

| 項目 | 值 |
| --- | --- |
| GPU | NVIDIA GeForce RTX 3070 8 GB（WDDM） |
| 軟體 | Python 3.10.13、PyTorch 2.1.1、CUDA 12.1、ultralytics 8.0.218 |
| 系統 | Windows，工作目錄曾在 `C:/Users/admin/Desktop/aircraft_tracking/` |
| notebook 標題 | 仍是課程「人臉偵測」；實際 `names` 已改成五類飛機 |

課堂把 `KMP_DUPLICATE_LIB_OK=TRUE` 寫進每個 notebook，避開 Intel MKL 在 Windows 上的重複載入警告。展示腳本也設了同一個變數。

## 超參（繳交時常用）

| 參數 | 典型值 | 備註 |
| --- | --- | --- |
| 骨幹 | `yolov8s.pt`、`yolov8m.pt` | 也試過 n/l/x；x 的 `last.pt` 單檔 297 MB |
| `imgsz` | 640 或 720 | s19 用 720 |
| `epochs` | 10 / 25 / 50 | 多數完整 run 是 50 |
| `batch` | 25–27 | 展示預設 16，避免別人 8 GB 卡直接 OOM |
| `cache` | True | 第二次以後明顯比較快 |
| `augment` | True | mosaic 等到 `close_mosaic=10` |
| `workers` | 8 或 24 |  |
| 接續 | `resume=True` 或餵 `last.pt` | s19 從 `my-yolov8s14/weights/last.pt` 接著訓 |

指令：

```powershell
python train/train.py --model yolov8s.pt --data data/data.yaml --epochs 50 --batch 16 --imgsz 640 --name aircraft-yolov8
```

## 留下來的數字

原料庫裡還讀得到的 `results.csv` 以 **`my-yolov8s19`** 最完整。最好一輪是 epoch 47：

| 指標 | 值 |
| --- | ---: |
| precision | 0.285 |
| recall | 0.344 |
| mAP50 | **0.283** |
| mAP50-95 | 0.194 |

原始表：[`assets/metrics/my-yolov8s19-results.csv`](assets/metrics/my-yolov8s19-results.csv)。

`my-yolov8s15`（從官方 `yolov8s.pt`、640、50 epoch）最後一輪約 mAP50 0.244。`my-yolov8m9` 只跑到 epoch 16 就不完整。notebook 另一次 `model.val()`（run 名 `my-yolov8s162`，圖已刪）全體 mAP50 0.13，各類：

| 類 | mAP50 |
| --- | ---: |
| civil_aircraft | 0.244 |
| fighter | 0.103 |
| bomber | 0.096 |
| other_military_aircraft | 0.202 |
| missile | 0.0026 |

missile 幾乎沒學會。遠距細長目標、驗證分布又偏 missile，兩者疊在一起。不要把 0.28 講成「已經很好」。

## 權重怎麼叫

課堂把自訓檔另存短名：`ats*` = YOLOv8**s** 飛機、`atm*` = YOLOv8**m**。

| 短名 | 約略來源 | 大小 |
| --- | --- | ---: |
| `ats4.pt` | `my-yolov8s19` / best | 21.5 MB |
| `ats3.pt` | `my-yolov8s15` | 21.5 MB |
| `atm2.pt` | `my-yolov8m3` | 49.6 MB |
| `atm3.pt` | `my-yolov8m9` | 297 MB |

它們只在 `original-data/`。公開倉請自己訓，或把單一 `best.pt` 放到 GitHub Releases，不要塞進 git 歷史。
