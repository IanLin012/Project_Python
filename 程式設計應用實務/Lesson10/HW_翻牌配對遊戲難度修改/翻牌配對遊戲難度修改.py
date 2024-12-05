from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
import os

# 引用字體檔案
resource_add_path(os.path.abspath('TaipeiSansTCBeta-Regular.ttf'))
# 將kivy預設的字體替換成指定的中文字體
LabelBase.register('Roboto', 'TaipeiSansTCBeta-Regular.ttf')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import random

from kivy.clock import Clock

class MemoryGame(App):
    def build(self):
        # 主布局
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    
        # 加入資訊區域
        info_layout = BoxLayout(size_hint_y=None, height=50)
        self.score = 0
        self.score_label = Label(text='分數: 0')
        self.time_label = Label(text='時間: 0秒')
        info_layout.add_widget(self.score_label)
        info_layout.add_widget(self.time_label)
        
        self.main_layout.add_widget(info_layout)
        
        self.game_grid = GridLayout()
        self.main_layout.add_widget(self.game_grid)

        self.time = 0
        self.game_started = False
        self.timer_event = None

        # 加入難度選擇按鈕
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)

        for size, label in [(4, '重新開始 4x4'), (6, '重新開始 6x6'), (8, '重新開始 8x8')]:
            button = Button(text=label)
            button.bind(on_press=lambda instance, size=size: self.restart_game(size))
            button_layout.add_widget(button)

        self.main_layout.add_widget(button_layout)

        # 預設難度為 4x4
        self.restart_game(4)

        return self.main_layout

    def create_cards(self, size):
        self.game_grid.clear_widgets()
        self.game_grid.cols = size

        total_cards = size * size
        self.cards = []
        self.card_values = list(range(total_cards // 2)) * 2
        random.shuffle(self.card_values)

        self.current_selection = []
    
        for i in range(total_cards):
            card = Button(
                text='?',
                font_size=24,
                background_color=(1, 0.8, 0.8, 1)
            )
            card.bind(on_press=self.on_card_press)
            card.card_value = self.card_values[i]
            card.revealed = False
            self.cards.append(card)
            self.game_grid.add_widget(card)

    def on_card_press(self, instance):
        if not self.game_started:
            self.game_started = True
            self.timer_event = Clock.schedule_interval(self.update_timer, 1)

        if instance.revealed:
            return
            
        if len(self.current_selection) < 2:
            instance.text = str(instance.card_value)
            instance.revealed = True
            instance.background_color = (0.8, 0.8, 1, 1)
            self.current_selection.append(instance)

        if len(self.current_selection) == 2:
            Clock.schedule_once(self.check_cards, 1)
    
    def check_cards(self, dt):
        card1, card2 = self.current_selection
        if card1.card_value == card2.card_value:
            card1.background_color = (0.8, 1, 0.8, 1)
            card2.background_color = (0.8, 1, 0.8, 1)
            self.score += 10
            self.score_label.text = f'分數: {self.score}'
        else:
            card1.text = '?'
            card2.text = '?'
            card1.revealed = False
            card2.revealed = False
            card1.background_color = (1, 0.8, 0.8, 1)
            card2.background_color = (1, 0.8, 0.8, 1)

        self.current_selection = []
    
    def update_timer(self, dt):
        self.time += 1
        self.time_label.text = f'時間: {self.time}秒'

    def restart_game(self, size):
        self.score = 0
        self.time = 0
        self.game_started = False
        self.current_selection = []
        self.score_label.text = '分數: 0'
        self.time_label.text = '時間: 0秒'

        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None

        self.create_cards(size)

if __name__ == '__main__':
    MemoryGame().run()
