"""SIDCGT — screen-image data collection tool (showcase v1.1).

2023 coursework helper: grab numbered screenshots, rename a folder, convert
PNG/JPG, centre-crop to a square. The submitted file defined `take_screenshot`
twice and blocked Tk in a `while` loop, so Stop could not run. This copy keeps
the same buttons and hot-key (Alt+Z) and only fixes those two defects.
"""

from __future__ import annotations

import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

import keyboard
import pyautogui
from PIL import Image

file_path = ""
start_num = 0
running = False
_hotkey_armed = True


def take_screenshot(folder: str, number: int) -> None:
    dest = os.path.join(folder, f"{number}.png")
    pyautogui.screenshot().save(dest)
    print(f"截取了圖片: {dest}")


def _poll_hotkey() -> None:
    """Non-blocking Alt+Z poll so the Stop button can run."""
    global start_num, _hotkey_armed
    if not running:
        return
    if keyboard.is_pressed("alt+z"):
        if _hotkey_armed and file_path:
            take_screenshot(file_path, start_num)
            start_num += 1
            _hotkey_armed = False
    else:
        _hotkey_armed = True
    app.after(40, _poll_hotkey)


def start_screenshot() -> None:
    global running
    if not file_path:
        status_text.set("請先選擇儲存資料夾")
        return
    running = True
    status_text.set("截圖功能已啟動...")
    print("截圖功能啟動...")
    _poll_hotkey()


def stop_screenshot() -> None:
    global running
    running = False
    status_text.set("截圖功能已停止...")
    print("截圖功能停止...")


def select_folder() -> None:
    global file_path, start_num
    chosen = filedialog.askdirectory()
    if not chosen:
        return
    file_path = chosen
    textbox1.delete(0, tk.END)
    textbox1.insert(0, file_path)
    existing = [
        int(name.split(".")[0])
        for name in os.listdir(file_path)
        if name.endswith(".png") and name.split(".")[0].isdigit()
    ]
    start_num = (max(existing) if existing else 0) + 1
    status_text.set(f"選擇的儲存資料夾: {file_path}")


def rename_files() -> None:
    folder = filedialog.askdirectory()
    if not folder:
        return
    try:
        first = int(entry_start_num.get())
    except ValueError:
        status_text.set("開始數字必須是整數")
        return
    idx = 0
    for name in sorted(os.listdir(folder)):
        if name.lower().endswith((".png", ".jpg", ".jpeg")):
            src = os.path.join(folder, name)
            dest = os.path.join(folder, f"{first + idx}.jpg")
            if src != dest:
                os.rename(src, dest)
            idx += 1
    status_text.set("批量改名完成...")


def convert_to_format(folder: str, target_format: str) -> None:
    suffix = f".{target_format}"
    for name in os.listdir(folder):
        src = Path(folder) / name
        if not src.is_file():
            continue
        if src.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        if src.suffix.lower() == suffix:
            continue
        dest = src.with_suffix(suffix)
        with Image.open(src) as img:
            rgb = img.convert("RGB") if target_format == "jpg" else img
            rgb.save(dest)
        src.unlink()
        print(f"Converted {name} to {target_format} format.")
    status_text.set(f"All images converted to .{target_format} format and originals deleted.")


def crop_to_square(image_path: str) -> None:
    with Image.open(image_path) as img:
        width, height = img.size
        side = min(width, height)
        left = (width - side) / 2
        top = (height - side) / 2
        img.crop((left, top, left + side, top + side)).save(image_path)
        print(f"Cropped {image_path}")


def crop_images_to_square() -> None:
    folder = filedialog.askdirectory()
    if not folder:
        return
    for name in os.listdir(folder):
        if name.lower().endswith((".png", ".jpg", ".jpeg")):
            crop_to_square(os.path.join(folder, name))
    status_text.set("所有图片已裁剪为正方形。")


def convert_to_png() -> None:
    folder = filedialog.askdirectory()
    if folder:
        convert_to_format(folder, "png")


def convert_to_jpg() -> None:
    folder = filedialog.askdirectory()
    if folder:
        convert_to_format(folder, "jpg")


app = tk.Tk()
app.title("螢幕畫面data蒐集神器v1.1")
status_text = tk.StringVar(app)

frame_screenshot = tk.Frame(app, padx=10, pady=10)
frame_screenshot.pack(pady=10)
tk.Label(frame_screenshot, text="螢幕截功能：").pack(side=tk.LEFT)
tk.Button(frame_screenshot, text="開始截圖", command=start_screenshot).pack(side=tk.LEFT)
tk.Button(frame_screenshot, text="停止截圖", command=stop_screenshot).pack(side=tk.LEFT)
tk.Button(frame_screenshot, text="選擇儲存資料夾", command=select_folder).pack(side=tk.LEFT)
textbox1 = tk.Entry(frame_screenshot)
textbox1.pack(side=tk.LEFT)

tk.Label(app, text="開始截圖後按 Alt+Z 截一張圖").pack()

frame_rename = tk.Frame(app, padx=10, pady=10)
frame_rename.pack(pady=10)
tk.Label(frame_rename, text="批量改檔名功能：").pack(side=tk.LEFT)
entry_start_num = tk.Entry(frame_rename)
entry_start_num.insert(0, "請輸入開始數字")
entry_start_num.pack(side=tk.LEFT)
tk.Button(frame_rename, text="選擇轉換資料夾並轉檔名", command=rename_files).pack(side=tk.LEFT)

tk.Entry(app, textvariable=status_text, state="readonly", width=50).pack(pady=10)

frame_convert = tk.Frame(app, padx=10, pady=10)
frame_convert.pack(pady=10)
tk.Button(frame_convert, text="選擇資料夾轉換成png", command=convert_to_png).pack(side=tk.LEFT)
tk.Button(frame_convert, text="選擇資料夾轉換成jpg", command=convert_to_jpg).pack(side=tk.LEFT)

frame_crop = tk.Frame(app, padx=10, pady=10)
frame_crop.pack(pady=10)
tk.Button(frame_crop, text="裁剪图片为正方形", command=crop_images_to_square).pack()

if __name__ == "__main__":
    app.mainloop()
