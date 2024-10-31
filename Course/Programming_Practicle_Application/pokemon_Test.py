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
    # 顯示所有寶可夢資訊
    print("可選擇的寶可夢：")
    for i, pokemon in enumerate(pokemons.keys(), 1):
        pokemon_data = pokemons[pokemon]
        print(f"{i}. {pokemon}（HP：{pokemon_data['hp']}　攻擊：{pokemon_data['attack']}　防禦：{pokemon_data['defense']}　屬性：{pokemon_data['type']}）")
    print()

def select_pokemon():
    # TODO: 實作選擇寶可夢的邏輯
    while True:
        try:
            choice = int(input("請選擇你的寶可夢（輸入數字）："))
            if 1 <= choice <= len(pokemons):
                return list(pokemons.keys())[choice - 1]
            else:
                print("請輸入有效的數字！")
        except ValueError:
            print("請輸入數字！")

def select_computer_pokemon(player_pokemon):
    # TODO: 實作電腦選擇寶可夢的邏輯
    import random
    all_pokemons = list(pokemons.keys())
    all_pokemons.remove(player_pokemon)
    return random.choice(all_pokemons)

def display_moves(pokemon_name):
    # 顯示所有招式資訊
    print(f"{pokemon_name}的可用招式：")
    pokemon = pokemons[pokemon_name]
    for i, move in enumerate(pokemon["moves"], 1):
        move_info = moves[move]
        if 'healing' in move_info:
            print(f"{i}. {move}（{move_info['type']}屬性　治療：{move_info['healing']}　命中：{move_info['accuracy']}%）\n   效果：{move_info['description']}")
        else:
            print(f"{i}. {move}（{move_info['type']}屬性　威力：{move_info['power']}　命中：{move_info['accuracy']}%）\n   效果：{move_info['description']}")
    print()

def select_move(pokemon_name):
    # TODO: 實作選擇招式的邏輯
    display_moves(pokemon_name)
    while True:
        try:
            choice = int(input("請選擇招式（輸入數字）："))
            pokemon = pokemons[pokemon_name]
            if 1 <= choice <= len(pokemon["moves"]):
                return pokemon["moves"][choice - 1]
            else:
                print("請輸入有效的數字！")
        except ValueError:
            print("請輸入數字！")

def calculate_damage(attacker, defender, move):
    # TODO: 實作傷害計算邏輯
    attacker_data = pokemons[attacker]
    defender_data = pokemons[defender]
    move_data = moves[move]
    
    # 傷害計算
    type_effectiveness = type_chart[move_data['type']][defender_data['type']]
    base_damage = (attacker_data['attack'] * move_data['power'] * type_effectiveness / 100) * (defender_data['defense'] / 100)
    base_healing = (move_data['healing'])
    # 顯示屬性剋制狀態
    if(type_effectiveness == 2.0):
        print("招式屬性剋制敵方，傷害增加100%！")
    elif(type_effectiveness == 0.5):
        print("招式被敵方屬性剋制，傷害減少50%！")
    else:
        print("招式不受屬性剋制影響，傷害不變！")

    return int(base_damage)

def is_hit(accuracy):
    # TODO: 實作命中判定邏輯
    return random.randint(1, 100) <= accuracy

def is_critical():
    # TODO: 實作爆擊判定邏輯
    return random.randint(1, 10) == 1 # 爆擊機率10%

def display_battle_stats(pokemon_name, stats):
    # TODO: 實作戰鬥統計顯示
    if(stats['current_hp'] < 0):
        stats['current_hp'] = 0
    print(f"{pokemon_name}：")
    print(f"－剩餘HP：{stats['current_hp']}/{stats['max_hp']}")
    print(f"－造成總傷害：{stats['damage_dealt']}")
    print(f"－使用招式：{', '.join(stats['moves_used'])}")

def battle_round(player_pokemon, computer_pokemon, player_hp, computer_hp, battle_stats):
    # TODO: 實作戰鬥回合邏輯
    # 選擇招式
    player_move = select_move(player_pokemon)
    computer_move = random.choice(pokemons[computer_pokemon]["moves"])

    # 計算玩家對電腦傷害
    print(f"\n{player_pokemon}使用了{player_move}！")
    player_damage = calculate_damage(player_pokemon, computer_pokemon, player_move)
    if is_hit(moves[player_move]['accuracy']):
        if is_critical():
            player_damage *= 1.5
            print("爆擊！傷害增加50%！")
        computer_hp -= player_damage
        print(f"命中！{computer_pokemon}受到了{player_damage}點傷害！")
    else:
        player_damage = 0
        print(f"沒有命中！{computer_pokemon}無受到傷害！")
    if(computer_hp < 0):
        computer_hp = 0
    print(f"{computer_pokemon}剩餘HP：{computer_hp}\n")
    
    # 計算電腦對玩家傷害
    print(f"{computer_pokemon}使用了{computer_move}！")
    computer_damage = calculate_damage(computer_pokemon, player_pokemon, computer_move)
    if is_hit(moves[computer_move]['accuracy']):
        if is_critical():
            computer_damage *= 1.5
            print("爆擊！傷害增加50%！")
        player_hp -= computer_damage
        print(f"命中！{player_pokemon}受到了{computer_damage}點傷害！")
    else:
        computer_damage = 0
        print(f"沒有命中！{player_pokemon}無受到傷害")
    if(player_hp < 0):
        player_hp = 0
    print(f"{player_pokemon}剩餘HP：{player_hp}")
    
    # 更新戰鬥統計
    battle_stats['player']['current_hp'] -= computer_damage
    battle_stats['player']['damage_dealt'] += player_damage
    battle_stats['player']['moves_used'].append(player_move)

    battle_stats['computer']['current_hp'] -= player_damage
    battle_stats['computer']['damage_dealt'] += computer_damage
    battle_stats['computer']['moves_used'].append(computer_move)
    
    return player_hp, computer_hp

def main():
    print("歡迎來到寶可夢對戰模擬器！")
    
    # 選擇寶可夢
    display_available_pokemons()
    player_pokemon = select_pokemon()
    computer_pokemon = select_computer_pokemon(player_pokemon)
    print(f"\n你選擇了{player_pokemon}！\n")
    print(f"電腦選擇了{computer_pokemon}！")
    
    # 初始化戰鬥統計
    max_player_hp = pokemons[player_pokemon]["hp"]
    max_computer_hp = pokemons[computer_pokemon]["hp"]
    player_hp = pokemons[player_pokemon]["hp"]
    computer_hp = pokemons[computer_pokemon]["hp"]
    battle_stats = {
        'player': {
            'max_hp': max_player_hp,
            'current_hp': player_hp,
            'damage_dealt': 0,
            'moves_used': []
        },
        'computer': {
            'max_hp': max_computer_hp,
            'current_hp': computer_hp,
            'damage_dealt': 0,
            'moves_used': []
        }
    }

    # 戰鬥迴圈
    round_num = 1
    while(player_hp > 0 and computer_hp > 0):
        print(f"\n=== 第{round_num}回合 ===")
        player_hp, computer_hp = battle_round(player_pokemon, computer_pokemon, player_hp, computer_hp, battle_stats)
        round_num += 1
    
    # 顯示戰鬥結果
    print("\n戰鬥結束！")
    if(player_hp > 0 and computer_hp <= 0):
        print(f"{player_pokemon}獲勝！\n")
    elif(player_hp <= 0 and computer_hp > 0):
        print(f"{computer_pokemon}獲勝！\n")
    else:
        print(f"{player_pokemon}與{computer_pokemon}平手！\n")

    # 顯示對戰統計
    print("對戰統計：")
    display_battle_stats(player_pokemon, battle_stats['player'])
    print()
    display_battle_stats(computer_pokemon, battle_stats['computer'])

if __name__ == "__main__":
    main()