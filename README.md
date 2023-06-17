# E-Tracking(Shopee)
 統一超商交貨便貨態查詢(包含 OCR 自動辨識驗證碼)
 本庫使用[ThanatosDi/E-Tracking](https://github.com/ThanatosDi/E-Tracking)改版
# Install
1. 下載本包
2. 安裝必要套件
    ```python
    pip install -r requirements.txt
    ```
3. 安裝 tesseract (如需使用 OCR 自動辨識)
   [Linux 安裝 tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
   [Windows 安裝 tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
# API Reference
* ECTracker(tesseract_path='tesseract'): [class]
  * tesseract_path: [str] 設定 tesseract 路徑 (default: tesseract)
* ECTracker.tracker(txtProductNum, autoVerify=False, tesseract_path='tesseract'): [function]
    * txtProductNum: [str] 貨態號碼 詳細請至[貨態號碼查詢教學](https://eservice.7-11.com.tw/e-tracking/TeachPage.html)查看
    * autoVerify: [Boolean] 是否啟用 OCR 自動辨識驗證碼 (default: False)
# Use
先在Userdata裡輸入使用者資料
直接開啟 login.py
若想使用 etracking.py 庫:
```python
from etracking import ECTRACKER
ECTRACKER.tracker('物流碼(7或11位)', autoVerify=True)
```
輸出的資料將會在[cargo]
# Error
etracking.CodeNotFound: can't identify image.  
使用 OCR 自動判斷驗證碼錯誤時將拋出例外: `can't identify image`  
請自行進行例外處理(重新執行至正確)
