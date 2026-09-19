# 資料集

語言：[繁體中文](../README.md) · [English](README.en.md)

本倉**不包含**影像。這裡只記錄 2023 集長什麼樣子，以及你要自備一組時該對齊什麼。

## 五類

| id | 名稱 | 訓練框 | 驗證框 |
| --- | --- | ---: | ---: |
| 0 | `civil_aircraft` | 135 | 38 |
| 1 | `fighter` | 176 | 30 |
| 2 | `bomber` | 166 | 27 |
| 3 | `other_military_aircraft` | 128 | 30 |
| 4 | `missile` | 144 | 71 |

訓練 803 張圖、732 份標註（約 71 張沒有對應 txt，可當背景）。驗證 131 張、132 份標註。驗證集 **missile 偏多**，看全體 mAP 時不要當成均勻抽樣。

YOLO 列格式：`class cx cy w h`，四個幾何值都是相對影像寬高的 `0–1`。

```text
1 0.512 0.408 0.086 0.052
```

## 2023 集怎麼來的

幀是 `SIDCGTv1.1.py` 從螢幕抓的，來源幾乎都是 YouTube。抽查可見：

- 播放器進度條、標題、頻道浮水印還在畫面上（例如 B-1B、熱氣球節）
- 有些幀根本不是五類之一（熱氣球被收進資料夾）
- 少數 txt 寫了 `fighter` 這種英文類名，或驗證集出現 `?`——Ultralytics 要的是整數 id
- `data.yaml` / `data-config.yaml` 仍貼著 Roboflow「face-detection-mik1i」區塊，那是課程模板，**與這五類無關**

因此：本機可以拿來復現訓練，不適合公開再散布。請改用自己有權使用的影像，或只在文件裡引用結果數字。

## 目錄

```text
data/
  data.yaml
  images/train/
  images/val/
  labels/train/   檔名主體與圖相同
  labels/val/
```

`path` 寫在 `data.yaml`，訓練腳本從倉庫根目錄解析。不要再寫 `C:/Users/...`。

標框工具用上游 [LabelImg](https://github.com/HumanSignal/labelImg)。類別順序必須與上表一致；原料庫的 `windows_v1.8.1/data/predefined_classes.txt` 就是這五個名字。
