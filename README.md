# Stack Stream Deck

堆疊式 Stream Deck 產生器。每個手機頁面都是一個獨立 JSON 模組，可以在 `setup.html` 內拖拉排序、修改參數，最後產生手機 PWA 頁面與電腦端 Python MQTT runtime。

## 快速使用

1. 開啟 `setup.html`
2. 從左側模組庫拖拉頁面到中間的堆疊順序
3. 點選頁面後在右側修改標題、MQTT topic、頁面參數或按鍵設定
4. 按「生成手機 PWA」下載 `stream-deck-pwa.html`
5. 按「生成 Python Runtime」下載 `stream_deck_runtime.py`
6. 手機開啟 PWA 後，電腦執行 Python runtime，兩端透過 MQTT 溝通

## JSON 模組

內建模組放在 `pages/`：

- `launch_apps.json`：啟動應用程式
- `media_controls.json`：多媒體操控
- `macro_keyboard.json`：巨集鍵盤指令
- `pc_status.json`：PC 狀態顯示
- `weather_forecast.json`：天氣預報
- `flip_clock.json`：翻頁時鐘

## 轉檔系統

`setup.html` 內有「HTML 轉 JSON」區塊。可以貼上 AI 設計好的單頁 HTML，系統會盡量萃取標題、按鈕與樣式，產生 `custom-html` 型別的 JSON 模組。這個模組仍可被拖拉排序並輸出到手機 PWA。

## MQTT Topic

預設 base topic 是：

```text
jj/stack_stream_deck
```

手機會發布：

```text
{baseTopic}/action
```

電腦 runtime 會發布：

```text
{baseTopic}/layout
{baseTopic}/status
{baseTopic}/system/status
```

## Python runtime 安裝

第一次執行電腦端接收程式前，請先安裝必要套件：

```powershell
python -m pip install -r requirements.txt
```

其中 `pyautogui` 會用來執行快捷鍵與媒體控制；如果沒有安裝，runtime 仍會嘗試 Windows 原生 fallback，但建議所有使用者都安裝完整依賴。
