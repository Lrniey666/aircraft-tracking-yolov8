# 貢獻指南

語言：[繁體中文](CONTRIBUTING.md) · [English](docs/CONTRIBUTING.en.md)

這是 2023 課程作業的封存展示倉。歡迎修文件、補環境註記、修展示腳本裡會害人跑不起來的缺陷。請先當歷史文物看，再動手。

## 動工前

1. 讀根目錄 [`README.md`](README.md) 與 [`docs/README.md`](docs/README.md)。
2. 改類別或預設超參時，同步 [`data/data.yaml`](data/data.yaml)、[`docs/dataset.md`](docs/dataset.md)、[`docs/training.md`](docs/training.md)。
3. 衝突時：**2023 繳交行為 > 展示倉文件**。文件寫錯就改文件。展示腳本只允許修「原檔明顯不能跑」的缺陷，並寫進 [`docs/`](docs/)。

## 慣例

| 項目 | 約定 |
| --- | --- |
| 對外說明 | 繁中在 `README.md`；英文在 `docs/README.en.md`，兩邊一起改 |
| 日期 | `YYYY-MM-DD`，台北時間 |
| 變更紀錄 | `CHANGELOG.md` 的 `## [Unreleased]`（Keep a Changelog 2.0.0） |
| 換行 | LF（`.gitattributes`） |

## 請不要

- 提交 `original-data/`、YouTube 幀、測試 mp4、`*.pt`、`datasets_fddb_2854.zip`、`labelImg.exe`
- 在程式裡硬寫本機絕對路徑或帳號
- 把課程殘留的人臉資料集說成是本專案的訓練集
- 把 mAP50 0.28 寫成 SOTA，或略過 missile 幾乎為 0 的 val
- 為了「比較現代」重寫 SIDCGT／追蹤流程卻聲稱這是 2023 原貌

不可逆的動作（force push、把原料庫打進歷史）請先問。

## 改完必做

1. Notable 變更寫進 `CHANGELOG.md` → `## [Unreleased]`
2. 動到 Hero／安裝／結構 → 繁中與英文 README 一起改
3. 若改了 `tools/sidcgt.py`、`train/train.py` 或 `infer/track.py`，在對應 `docs/` 註明與 2023 檔的偏離
