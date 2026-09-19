# 推論與追蹤

語言：[繁體中文](../README.md) · [English](README.en.md)

展示入口：[`infer/track.py`](../infer/track.py)、[`notebooks/track.ipynb`](../notebooks/track.ipynb)。文件依據：[Ultralytics Track mode](https://docs.ultralytics.com/modes/track/)。

## 課堂在做什麼

```python
results = model.track(frame, persist=True, conf=0.20)
annotated = results[0].plot()
cv2.imshow("YOLOv8 Tracking", resize_with_aspect_ratio(annotated, 1000))
```

- `persist=True`：同一支 `YOLO` 實例把上一幀的 track 接到這一幀。**重新 `YOLO(...)` 就會重編號。**
- `conf=0.20`：遠距小目標用的課堂值。要乾淨一點再往上加。
- 顯示寬度 1000 px，比例不變——影片比螢幕大時才看得完。
- 按 `q` 離開。

可選的「時間軌跡」來自官方範例：每個 id 留 30 個中心點，灰色折線粗度 10。2023 notebook 在某一幀 `boxes.id is None` 時炸了（`AttributeError`）。展示腳本遇到這種幀就跳過折線，框仍畫。

```powershell
python infer/track.py --weights path\to\best.pt --source path\to\video.mp4 --conf 0.20 --trail
python infer/track.py --weights path\to\best.pt --source 0 --no-show --save runs/out.mp4
```

`--source` 可以是檔案、攝影機編號或 URL。課堂 notebook 留過 `https://youtu.be/LNwODJXcvt4`，實際跑的是本機 `fighter1.mp4` / `all1.mp4`。

## 權重

課堂追蹤示範載入 `./pt/ats4.pt`。本機對應：

```text
original-data/aircraft_tracking_use/pt/ats4.pt
```

那是 YOLOv8s、接續訓練到 `my-yolov8s19` 的 best。`ats3.pt` 是較早的 s15。m 系列（`atm2` / `atm3`）比較重，課堂主要展示仍用 s。

## 測試片（本機 only）

| 檔名 | 約略 |
| --- | --- |
| `fighter1.mp4` | 110 MB，課堂主示範 |
| `all1.mp4` | 51 MB，綜合；軌跡範例在這支上炸掉 |
| `civil_aircraft1.mp4` | 5 MB |
| B-52 / AGM-86B 片 | 第三方標題還在檔名裡 |
| Army Ranger fast rope | 與五類關係薄弱 |

全部是 YouTube 下載，**不要提交**。要公開示範請改連你自己的結果片，或只放 QR（[`assets/demo-qr.png`](assets/demo-qr.png)）。
