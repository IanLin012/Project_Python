from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
import os

from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton

# 引用字體檔案
resource_add_path(os.path.abspath('TaipeiSansTCBeta-Regular.ttf'))
# 將kivy預設的字體替換成指定的中文字體
LabelBase.register('Roboto', 'TaipeiSansTCBeta-Regular.ttf')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Example2App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 建立滑動條
        slider = Slider(
            min=0,
            max=100,
            value=50,
            size_hint_y=None,
            height=50
        )
        slider.bind(value=self.on_slider_change)

        # 建立進度條
        self.progress = ProgressBar(
            max=100,
            value=50,
            size_hint_y=None,
            height=30
        )

        self.label = Label(
            text="50"
        )

        self.img = Image(
            source="images/dog.jpg",
            size_hint = (None, None),
            size = (200, 200),
            pos_hint = {'center_x': 0.5}
        )

        layout.add_widget(slider)
        layout.add_widget(self.progress)
        layout.add_widget(self.label)
        layout.add_widget(self.img)
        return layout

    def on_slider_change(self, instance, value):
        self.progress.value = value
        self.label.text = str(int(value))
        if value > 50:
            self.img.source = "images/dog.jpg"
        else:
            self.img.source = "images/orange.jpg"



if __name__ == "__main__":
    Example2App().run()