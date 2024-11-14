# 定義常數
ENERGY_UNITS = {
    'N': 1000,  # 核能反應爐
    'S': 200,   # 太陽能板
    'B': 50     # 備用電池
}

ROOM_ENERGY = {
    'C': 100,   # 控制艙
    'L': 200,   # 居住艙
    'G': 150,   # 貨物艙
    'R': 300    # 研究艙
}

MISSION_REQUIREMENTS = {
    'E': {  # 探索任務
        'energy': 1000,
        'rooms': {'C': 1, 'L': 2, 'R': 1, 'G': 0}
    },
    'T': {  # 運輸任務
        'energy': 800,
        'rooms': {'C': 1, 'L': 1, 'G': 3, 'R': 0}
    },
    'S': {  # 研究任務
        'energy': 1500,
        'rooms': {'C': 1, 'L': 2, 'R': 2, 'G': 0}
    }
}

def parse_config(config_str):
    """
    解析配置字串，返回字典形式的配置
    """
    result = {}

    # 如果單字後是數字，單字為key，數字為value
    for i in range(len(config_str) - 1):
        if 'A' <= config_str[i] <= 'Z':
            if config_str[i+1].isdigit():
                result[config_str[i]] = config_str[i+1]
    
    return result

def calculate_energy_supply(energy_config):
    """
    計算能源供應總量
    """
    total_supply = 0
    energy_dict = parse_config(energy_config)

    for energy in energy_dict:
        if energy in ENERGY_UNITS:
            total_supply += int(ENERGY_UNITS[energy]) * int(energy_dict[energy])
    
    return total_supply

def calculate_energy_consumption(room_config):
    """
    計算能源消耗總量
    """
    total_consumption = 0
    room_dict = parse_config(room_config)

    for room in room_dict:
        if room in ROOM_ENERGY:
            total_consumption += int(ROOM_ENERGY[room]) * int(room_dict[room])
    
    return total_consumption

def check_room_requirements(room_config, mission_type):
    """
    檢查艙室配置是否符合任務要求
    """
    if mission_type not in MISSION_REQUIREMENTS:
        return
        
    room_dict = parse_config(room_config)
    required_rooms = MISSION_REQUIREMENTS[mission_type]['rooms']
    
    for room in required_rooms:
        if room not in room_dict:
            return False
        elif int(room_dict[room]) < int(required_rooms[room]):
            return False
    
    return True

def check_energy_requirements(total_supply, total_consumption, mission_type):
    """
    檢查能源是否符合任務要求
    """
    if mission_type not in MISSION_REQUIREMENTS:
        return 
        
    # 檢查能源是否足夠支付消耗
    if total_supply < total_consumption:
        return False
    
    # 檢查是否滿足任務最低能源要求
    if total_supply < MISSION_REQUIREMENTS[mission_type]['energy']:
        return False

    return True

def evaluate_spaceship_config(ship_id, energy_config, room_config, mission_type):
    """
    評估太空船配置
    """
    # 基本驗證
    if not all([ship_id, energy_config, room_config, mission_type]):
        print(f"{ship_id}\n{ship_id} 警告：輸入資料不完整")
        return
    
    if mission_type not in MISSION_REQUIREMENTS:
        print(f"{ship_id}\n{ship_id} 警告：無效的任務類型")
        return
    
    # 計算能源供應和消耗
    total_supply = calculate_energy_supply(energy_config)
    total_consumption = calculate_energy_consumption(room_config)
    remaining_energy = total_supply - total_consumption
    
    # 輸出基本資訊
    print(ship_id)
    print(f"總能源供應：{total_supply}")
    print(f"總能源消耗：{total_consumption}")
    print(f"剩餘能源：{remaining_energy}")
    
    # 檢查能源要求
    if not check_energy_requirements(total_supply, total_consumption, mission_type):
        print(f"{ship_id} 警告：能源供應不足，無法供應任務進行")
        return
    
    # 檢查艙室要求
    if not check_room_requirements(room_config, mission_type):
        print(f"{ship_id} 警告：艙室配置不符合任務要求")
        return
    
    # 所有檢查都通過
    print(f"{ship_id} 配置檢查通過，可以執行任務")
    
    # 計算剩餘能源可以支持的天數
    daily_consumption = 100  # 每日基本消耗
    if check_energy_requirements(total_supply, total_consumption, mission_type) and check_room_requirements(room_config, mission_type):
        days = remaining_energy / daily_consumption
        print(f"剩餘能源可以足夠運行 {int(days)} 天")

# 讀取輸入
ship_id = input()
energy_config = input()
room_config = input()
mission_type = input()

# 執行配置評估
evaluate_spaceship_config(ship_id, energy_config, room_config, mission_type)