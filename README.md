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
* OCR自動辨識  
  * `Verify identify image error.` : 驗證碼判斷錯誤  
  * `can't identify image` : 無法判斷驗證碼
* Login  
  * `需手機驗證 驗證後請關閉本程式` : 手機驗證後到 `CMD` ctrl+c關閉
* Exception  
  * 錯誤為 `Exception` 需自行處理或到[issues](https://github.com/XiaXia009/E-Tracking/issues)中發出問題  
OCR自動辨識 / Login 類錯誤只需至需重新啟動Login.py即可
# Contributors
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/XiaXia009"><img src="https://avatars.githubusercontent.com/u/107758517?v=4" width="100px;" alt="Ray"/><br /><sub><b>Ray</b></sub></a><br /><a title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ThanatosDi"><img src="https://avatars.githubusercontent.com/u/12424898?v=4" width="100px;" alt="ThanatosDi"/><br /><sub><b>ThanatosDi</b></sub></a><br /><a title="Code">💻</a></td>
    </tr>
  </tbody>
</table>
