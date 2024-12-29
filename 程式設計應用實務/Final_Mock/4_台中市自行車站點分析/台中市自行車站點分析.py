from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.core.window import Window
import webbrowser
import requests, json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import folium

"""導入字型"""
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

class HoverButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original_color = self.background_color
        Window.bind(mouse_pos=self.on_mouse_pos)

    # 檢查游標是否在按鈕內
    def on_mouse_pos(self, window, pos):
        if self.collide_point(*pos):
            self.on_hover()
        else:
            self.on_leave()

    # 游標在按鈕上
    def on_hover(self):
        self.background_color = [c * 0.7 for c in self.original_color[:3]] + [self.original_color[3]]

    # 游標離開按鈕
    def on_leave(self):
        self.background_color = self.original_color

class YouBikeApp(App):
    def build(self):
        # 設定主佈局
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 標題標籤
        title_label = Label(
            text="台中市公共自行車站點分析",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=32,
            size_hint=(1, 0.02)
        )
        self.layout.add_widget(title_label)

        # 執行分析按鈕
        analyze_button = HoverButton(
            text="執行分析",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=28,
            size_hint=(1, 0.02),
            background_color=[0, 0, 1, 1]
        )
        analyze_button.bind(on_press=self.show_analysis)
        self.layout.add_widget(analyze_button)

        # 顯示地圖按鈕
        map_button = HoverButton(
            text="查看地圖",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=28,
            size_hint=(1, 0.02),
            background_color=[0, 1, 0, 1]
        )
        map_button.bind(on_press=self.show_map)
        self.layout.add_widget(map_button)

        # 地圖顯示狀態標籤
        self.map_status_label = Label(
            text="準備就緒",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=28,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.map_status_label)

        return self.layout

    def fetch_data(self):
        # 取得資料
        res = requests.get("https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1")
        data = json.loads(res.text)
        return pd.DataFrame(data['retVal'])

    def show_analysis(self, instance):
        # 處理資料
        df = self.fetch_data()
        df = df[['sarea']]
        station_count = df['sarea'].value_counts()

        # 繪製長條圖
        x = station_count.index
        y = station_count.values
        plt.bar(x, y)
        plt.title("台中市各行政區站點統計圖")
        plt.xlabel("行政區")
        plt.ylabel("站點數量")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def show_map(self, instance):
        # 取得資料
        df = self.fetch_data()
        xituan_stations = df[df['sarea'] == "西屯區"]

        # 轉換資料類型
        xituan_stations['lat'] = xituan_stations['lat'].astype(float)
        xituan_stations['lng'] = xituan_stations['lng'].astype(float)
        xituan_stations['sbi'] = xituan_stations['sbi'].astype(int)

        # 建立地圖
        fcu_location = [24.17912418152435, 120.6470844648072]
        map = folium.Map(location=fcu_location, zoom_start=15)

        # 添加標記
        for _, station in xituan_stations.iterrows():
            if station['sbi'] > 5:
                color = 'green'
            elif station['sbi'] > 0:
                color = 'yellow'
            else:
                color = 'red'

            folium.CircleMarker(
                location=[station['lat'], station['lng']],
                popup=f"{station['sna']}<br>可借車輛: {station['sbi']}",
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7
            ).add_to(map)

        # 儲存並開啟地圖
        map_path = "xituan_bike_map.html"
        map.save(map_path)
        webbrowser.open(map_path)

        # 更新地圖狀態標籤
        self.map_status_label.text = "地圖已在瀏覽器開啟"

if __name__ == "__main__":
    YouBikeApp().run()