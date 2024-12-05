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
        
        self.game_grid = GridLayout(cols=4)
        
        self.main_layout.add_widget(info_layout)
        self.main_layout.add_widget(self.game_grid)

        # 建立卡片
        self.cards = []
        self.card_values = list(range(8)) * 2
        random.shuffle(self.card_values)

        self.current_selection = []
    
        for i in range(16):
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

        self.time = 0
        self.game_started = False
        self.timer_event = None

        restart_button = Button(
            text='重新開始',
            size_hint_y=None,
            height=50
        )
        restart_button.bind(on_press=self.restart_game)
        self.main_layout.add_widget(restart_button)

        return self.main_layout
    
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

    def restart_game(self, size=4):
        self.score = 0
        self.time = 0
        self.game_started = False
        self.game_finished = False
        self.current_selection = []
        self.score_label.text = '分數: 0'
        self.time_label.text = '時間: 0秒'
        self.difficulty = size
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None

        random.shuffle(self.card_values)
        for i, card in enumerate(self.cards):
            card.text = '?'
            card.revealed = False
            card.matched = False  # 重置配對狀態
            card.background_color = (1, 0.8, 0.8, 1)  # 重置為初始顏色
            card.card_value = self.card_values[i]

if __name__ == '__main__':
    MemoryGame().run()
