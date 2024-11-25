class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} ({self.weight}kg)"

class Backpack:
    # 初始化
    def __init__(self, max_weight=10.0):
        self.max_weight = max_weight
        # 物品列表
        self.items = []
        self.current_weight = 0.0

    # 在背包中放入物品
    def add_item(self, item):
        # 判斷是否超過背包最大重量
        if self.current_weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.current_weight += item.weight
            print(f"成功添加物品: {item}")
        else:
            print("背包已達重量上限，無法添加更多物品！")

    # 移除背包中的物品
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.current_weight -= item.weight
                print(f"成功移除物品: {item}")
                return
        print(f"背包中沒有找到物品: {item_name}")

    # 顯示背包中的物品
    def show_status(self):
        # 判斷背包是否有物品
        if not self.items:
            print("背包是空的！")
        else:
            print("背包中的物品：")
            for item in self.items:
                print(item)
        print(f"當前重量: {self.current_weight}kg / {self.max_weight}kg")

# 創建背包
backpack = Backpack()

# 物品欄
items = [
    Item("繩子", 2.0),
    Item("水壺", 1.0),
    Item("手電筒", 0.5),
    Item("地圖", 0.1),
    Item("急救包", 1.0),
    Item("指南針", 0.2),
    Item("帳篷", 3.0),
    Item("睡袋", 1.5)
]

# 互動式程式
while True:
    print("\n請選擇操作：")
    print("1. 在背包中放入物品")
    print("2. 移除背包中的物品")
    print("3. 顯示背包中的物品")
    print("4. 結束程式")
    choice = input("選擇 (1-4): ")
    
    if choice == '1':
        print("可用的物品：")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")
        
        item_choice = int(input("請選擇物品 (1-8): ")) - 1
        if 0 <= item_choice < len(items):
            backpack.add_item(items[item_choice])
        else:
            print("選擇無效！")
    
    elif choice == '2':
        item_name = input("請輸入要移除的物品名稱：")
        backpack.remove_item(item_name)
    
    elif choice == '3':
        backpack.show_status()
    
    elif choice == '4':
        print("結束程式。")
        break
    else:
        print("選擇無效，請重新選擇。")
