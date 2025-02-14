# Python
## Kivy
### 函式庫
```py
from kivy.app import App # Kivy 應用程式的基礎類別（覆寫 build() 方法來定義應用程式的圖形介面）

from kivy.uix.boxlayout import BoxLayout # 版面配置管理器（在水平方向或垂直方向排列子元件）
from kivy.uix.button import Button # Kivy 的按鈕元件（用戶與應用程式進行交互）
from kivy.uix.label import Label # 顯示文字的元件（展示靜態文本）
from kivy.uix.scrollview import ScrollView # 可捲動的視圖（支持垂直或水平捲動）
from kivy.uix.textinput import TextInput # 用戶輸入文字的元件（用於輸入框多行文字和複製、貼上等基本文字操作）

from kivy.core.text import LabelBase # 核心文字處理模組（註冊自定義字型供應用程式使用）

from kivy.resources import resource_add_path # 將新的資源目錄添加到 Kivy 的資源路徑中
```
### 函數
orientation：排列方式  
spacing：元件之間的間距  
size_hint：尺寸佔比 (x水平, y垂直)  
add_widget：加入元件  
bind(on_press)：綁定按下按鈕事件

Youtube to m4a
```bash
yt-dlp --ffmpeg-location C:\Users\drlin\Downloads\ffmpeg-7.1-essentials_build\ffmpeg-7.1-essentials_build\bin -f bestaudio --extract-audio --audio-format alac "link"
```