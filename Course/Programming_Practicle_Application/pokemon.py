import random

moves = {
    "電擊": {
        "type": "電",
        "power": 40,
        "accuracy": 100,
        "description": "發射電流攻擊對手"
    },
    "十萬伏特": {
        "type": "電",
        "power": 90,
        "accuracy": 85,
        "description": "釋放強大的電流"
    },
    "鐵尾": {
        "type": "一般",
        "power": 50,
        "accuracy": 95,
        "description": "用堅硬的尾巴攻擊"
    },
    "水槍": {
        "type": "水",
        "power": 40,
        "accuracy": 100,
        "description": "噴射水流攻擊"
    },
    "高壓水柱": {
        "type": "水",
        "power": 85,
        "accuracy": 90,
        "description": "噴射高壓水流"
    },
    "火花": {
        "type": "火",
        "power": 40,
        "accuracy": 100,
        "description": "噴射火花攻擊"
    },
    "噴射火焰": {
        "type": "火",
        "power": 90,
        "accuracy": 85,
        "description": "噴射猛烈火焰"
    },
    "藤鞭": {
        "type": "草",
        "power": 40,
        "accuracy": 100,
        "description": "用藤蔓鞭打對手"
    },
    "飛葉快刀": {
        "type": "草",
        "power": 85,
        "accuracy": 90,
        "description": "發射葉片攻擊"
    },
    "光合作用": {
        "type": "草",
        "power": 0,
        "accuracy": 100,
        "description": "回復HP",
        "healing": 50
    }
}

pokemons = {
    "皮卡丘": {
        "type": "電",
        "hp": 100,
        "attack": 75,
        "defense": 60,
        "moves": ["電擊", "鐵尾", "十萬伏特"]
    },
    "傑尼龜": {
        "type": "水",
        "hp": 110,
        "attack": 65,
        "defense": 80,
        "moves": ["水槍", "鐵尾", "高壓水柱"]
    },
    "小火龍": {
        "type": "火",
        "hp": 95,
        "attack": 85,
        "defense": 55,
        "moves": ["火花", "鐵尾", "噴射火焰"]
    },
    "妙蛙種子": {
        "type": "草",
        "hp": 105,
        "attack": 70,
        "defense": 75,
        "moves": ["藤鞭", "飛葉快刀", "光合作用"]
    }
}

type_chart = {
    "火": {
        "草": 2.0,
        "水": 0.5,
        "電": 1.0,
        "一般": 1.0
    },
    "水": {
        "火": 2.0,
        "草": 0.5,
        "電": 0.5,
        "一般": 1.0
    },
    "草": {
        "水": 2.0,
        "火": 0.5,
        "電": 1.0,
        "一般": 1.0
    },
    "電": {
        "水": 2.0,
        "火": 1.0,
        "草": 1.0,
        "一般": 1.0
    },
    "一般": {
        "水": 1.0,
        "火": 1.0,
        "草": 1.0,
        "電": 1.0
    }
}

def display_available_pokemons():
    print("=== 寶可夢對戰模擬器 ===")
    print("可選擇的寶可夢：")
    for i, pokemon in enumerate(pokemons.keys(), 1):
        print(f"{i}. {pokemon}")
    print()

def select_pokemon():
    # TODO: 實作選擇寶可夢的邏輯
    pass

def select_computer_pokemon(player_pokemon):
    # TODO: 實作電腦選擇寶可夢的邏輯
    pass

def display_moves(pokemon_name):
    print(f"{pokemon_name}的可用招式：")
    pokemon = pokemons[pokemon_name]
    for i, move in enumerate(pokemon["moves"], 1):
        move_info = moves[move]
        print(f"{i}. {move}（{move_info['type']}屬性 威力:{move_info['power']} 命中:{move_info['accuracy']}%）")
    print()

def select_move(pokemon_name):
    # TODO: 實作選擇招式的邏輯
    pass

def calculate_damage(attacker, defender, move):
    # TODO: 實作傷害計算邏輯
    pass

def is_hit(accuracy):
    # TODO: 實作命中判定邏輯
    pass

def is_critical():
    # TODO: 實作爆擊判定邏輯
    pass

def display_battle_stats(pokemon_name, stats):
    # TODO: 實作戰鬥統計顯示
    pass

def battle_round(player_pokemon, computer_pokemon, player_hp, computer_hp):
    # TODO: 實作戰鬥回合邏輯
    pass

def main():
    print("歡迎來到寶可夢對戰模擬器！")
    
    # 選擇寶可夢
    display_available_pokemons()
    player_pokemon = select_pokemon()
    computer_pokemon = select_computer_pokemon(player_pokemon)
    
    print(f"\n你選擇了{player_pokemon}！")
    print(f"電腦選擇了{computer_pokemon}！")
    
    # 初始化HP和戰鬥統計
    player_hp = pokemons[player_pokemon]["hp"]
    computer_hp = pokemons[computer_pokemon]["hp"]
    
    battle_stats = {
        'player': {
            'max_hp': player_hp,
            'current_hp': player_hp,
            'damage_dealt': 0,
            'moves_used': []
        },
        'computer': {
            'max_hp': computer_hp,
            'current_hp': computer_hp,
            'damage_dealt': 0,
            'moves_used': []
        }
    }
    
    # 戰鬥迴圈
    round_num = 1
    while player_hp > 0 and computer_hp > 0:
        print(f"\n=== 第{round_num}回合 ===")
        player_hp, computer_hp = battle_round(player_pokemon, computer_pokemon, player_hp, computer_hp)
        round_num += 1
    
    # 顯示戰鬥結果和統計
    print("\n戰鬥結束！")
    display_battle_stats(player_pokemon, battle_stats['player'])
    display_battle_stats(computer_pokemon, battle_stats['computer'])
    
    if player_hp > 0:
        print(f"\n{player_pokemon}獲勝！")
    else:
        print(f"\n{computer_pokemon}獲勝！")

if __name__ == "__main__":
    main()