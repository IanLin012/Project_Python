from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
import os

from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

# 引用字體檔案
resource_add_path(os.path.abspath('TaipeiSansTCBeta-Regular.ttf'))
# 將kivy預設的字體替換成指定的中文字體
LabelBase.register('Roboto', 'TaipeiSansTCBeta-Regular.ttf')

class TaskWidget(BoxLayout):
    def __init__(self, text, parent_list, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 40
        self.spacing = 5

        # 保存對父列表的引用和文字內容
        self.parent_list = parent_list
        self.text = text

        # 待辦事項文字
        self.task_label = Label(text=text, size_hint_x=0.7)
        self.add_widget(self.task_label)

        # 修改按鈕
        delete_button = Button(text="修改", size_hint_x=0.2)
        delete_button.bind(on_press=self.on_edit)
        self.add_widget(delete_button)

        # 刪除按鈕
        delete_button = Button(text='刪除', size_hint_x=0.3)
        delete_button.bind(on_press=self.on_delete)
        self.add_widget(delete_button)

    def on_delete(self, instance):
        """當刪除按鈕被點擊時，呼叫父列表的刪除方法"""
        self.parent_list.delete_task(self)

    def on_edit(self, instance): 
        """當編輯按鈕被點擊時，呼叫父列表的編輯方法"""
        self.parent_list.edit_task(self)

class TodoList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        # 上半部分：已儲存的待辦事項區域
        self.tasks_layout = BoxLayout(orientation='vertical', size_hint_y=0.9)
        self.scroll = ScrollView()
        self.tasks_container = BoxLayout(orientation='vertical', size_hint_y=None)
        self.tasks_container.bind(minimum_height=self.tasks_container.setter('height'))

        self.scroll.add_widget(self.tasks_container)
        self.tasks_layout.add_widget(self.scroll)

        # 下半部分：新增待辦事項區域
        self.input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)
        self.task_input = TextInput(multiline=False)
        self.add_button = Button(text='新增', size_hint_x=0.3)
        self.add_button.bind(on_press=self.add_task)

        self.input_layout.add_widget(self.task_input)
        self.input_layout.add_widget(self.add_button)

        # 將所有元件加入主布局
        self.add_widget(Label(text='待辦事項', size_hint_y=0.1))
        self.add_widget(self.tasks_layout)
        self.add_widget(self.input_layout)

    def add_task(self, instance):
        text = self.task_input.text.strip()
        if text:
            task_widget = TaskWidget(text, parent_list=self)
            self.tasks_container.add_widget(task_widget)
            self.task_input.text = ''  # 清空輸入框

    def delete_task(self, task_widget):
        """刪除指定的待辦事項"""
        self.tasks_container.remove_widget(task_widget)

    def edit_task(self, task_widget):
        """開始編輯指定的待辦事項"""
        self.task_input.text = task_widget.text
        self.add_button.text = '確認修改'
        self.task_input.focus = True  # 自動聚焦到輸入框

class TodoApp(App):
    def build(self):
        return TodoList()

if __name__ == '__main__':
    TodoApp().run()
