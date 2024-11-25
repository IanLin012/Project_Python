from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
import os

# 引用字體檔案
resource_add_path(os.path.abspath('TaipeiSansTCBeta-Regular.ttf'))
# 將kivy預設的字體替換成指定的中文字體
LabelBase.register('Roboto', 'TaipeiSansTCBeta-Regular.ttf')

class TodoApp(App):
    def build(self):
        return TodoList()

class TodoList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        # 上半部分：已儲存的待辦事項區域
        self.tasks_layout = BoxLayout(orientation='vertical', size_hint_y=0.7)
        self.scroll = ScrollView()
        self.tasks_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.tasks_container.bind(minimum_height=self.tasks_container.setter('height'))

        self.scroll.add_widget(self.tasks_container)
        self.tasks_layout.add_widget(self.scroll)

        # 下半部分：新增待辦事項區域
        self.input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.3, spacing=10)
        self.task_input = TextInput(multiline=False)
        self.add_button = Button(text='新增', size_hint_x=0.3)

        self.input_layout.add_widget(self.task_input)
        self.input_layout.add_widget(self.add_button)

        # 將所有元件加入主佈局
        self.add_widget(Label(text='待辦事項', size_hint_y=0.1))
        self.add_widget(self.tasks_layout)
        self.add_widget(self.input_layout)

if __name__ == '__main__':
    TodoApp().run()