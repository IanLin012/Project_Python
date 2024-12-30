from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.core.window import Window
import webbrowser
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
import folium
import json

# Import custom font
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

class HoverButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original_color = self.background_color
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, window, pos):
        if self.collide_point(*pos):
            self.on_hover()
        else:
            self.on_leave()

    def on_hover(self):
        self.background_color = [c * 0.7 for c in self.original_color[:3]] + [self.original_color[3]]

    def on_leave(self):
        self.background_color = self.original_color

class TaichungAnalysisApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title_label = Label(
            text="台中市設備分析",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=32,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(title_label)

        analyze_button = HoverButton(
            text="繪製設備數量長條圖",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=24,
            size_hint=(1, 0.1),
            background_color=[0, 0, 1, 1]
        )
        analyze_button.bind(on_press=self.plot_bar_chart)
        self.layout.add_widget(analyze_button)

        map_button = HoverButton(
            text="生成並開啟地圖",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=24,
            size_hint=(1, 0.1),
            background_color=[0, 1, 0, 1]
        )
        map_button.bind(on_press=self.generate_map)
        self.layout.add_widget(map_button)

        self.status_label = Label(
            text="準備就緒",
            font_name="TaipeiSansTCBeta-Regular.ttf",
            font_size=24,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.status_label)

        return self.layout

    def fetch_data(self):
        movement_url = "https://datacenter.taichung.gov.tw/swagger/OpenData/a8dcd9fc-37f0-4d2e-be6f-edf59d16cec9"
        fixed_url = "https://datacenter.taichung.gov.tw/swagger/OpenData/a3a7f779-7c2e-44cd-825d-9026805e4070"

        movement_res = requests.get(movement_url)
        fixed_res = requests.get(fixed_url)

        movement_data = json.loads(movement_res.text)
        fixed_data = json.loads(fixed_res.text)

        def extract_data(json_data, is_fixed):
            records = []
            for item in json_data:
                records.append({
                    "行政區": item.get("行政區", ""),
                    "速限speed": item.get("速限Speed", item.get("速限speed", "")),
                    "緯度": float(item.get("緯度", 0)),
                    "經度": float(item.get("經度", 0)),
                    "固定式": "是" if is_fixed else "否"
                })
            return records

        movement_records = extract_data(movement_data, is_fixed=False)
        fixed_records = extract_data(fixed_data, is_fixed=True)

        return pd.DataFrame(movement_records + fixed_records)

    def plot_bar_chart(self, instance):
        df = self.fetch_data()
        count_data = df.groupby(["行政區", "固定式"]).size().unstack(fill_value=0)
        count_data.plot(kind="bar", stacked=False, figsize=(12, 6), color=["orange", "blue"])
        plt.title("台中市各行政區設備數量統計")
        plt.xlabel("行政區")
        plt.ylabel("設備數量")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_map(self, instance):
        df = self.fetch_data()
        fcu_location = [24.17912418152435, 120.6470844648072]
        map_ = folium.Map(location=fcu_location, zoom_start=12)

        for _, row in df.iterrows():
            speed = int(row["速限speed"] or 0)
            if speed <= 50:
                color = "green"
            elif 60 <= speed <= 70:
                color = "yellow"
            else:
                color = "red"

            folium.CircleMarker(
                location=[row["緯度"], row["經度"]],
                popup=f"速限: {speed} km/h\n固定式: {row['固定式']}",
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7
            ).add_to(map_)

        map_path = "taichung_speed_map.html"
        map_.save(map_path)
        webbrowser.open(map_path)

        self.status_label.text = "地圖已生成並在瀏覽器中開啟"

if __name__ == "__main__":
    TaichungAnalysisApp().run()
