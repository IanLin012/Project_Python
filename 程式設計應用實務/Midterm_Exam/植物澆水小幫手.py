# 儲存植物資料的字典，key是植物名稱，value是[澆水週期, 剩餘天數]
plants = {}

# 讀取指令數量
try:
    n = int(input())
except ValueError:
    n = 0

# 處理每一個指令
for _ in range(n):

    command = input().split()
    
    # 檢查指令格式
    if not command:
        print('查無此植物')
        continue
        
    # 新增植物指令
    if command[0] == 'A':
        # 檢查參數數量
        if len(command) != 3:
            print('查無此植物')
            continue
            
        plant_name = command[1]
        # 檢查植物名稱是否為空
        if plant_name == "":
            print('查無此植物')
            continue
            
        # 檢查澆水週期是否為正整數
        try:
            period = command[2]
            if (period.isdigit() == False) or (int(period) < 1):
                print('查無此植物')
                continue
        except ValueError:
            print('查無此植物')
            continue
            
        if plant_name in plants:
            print('植物已存在')
        else:
            plants[plant_name] = {"plant name": plant_name, "period": command[2]}
            print('新增成功')
    
    # 查詢植物指令
    elif command[0] == 'Q':
        # 檢查參數數量
        if len(command) != 2:
            print('查無此植物')
            continue

        if command[1] == "":
            print('查無此植物')
            continue
            
        plant_name = command[1]
        if command[1] in plants:
            print(f'還有 {plants[plant_name]["period"]} 天需要澆水')
        else:
            print('查無此植物')
    
    # 澆水指令
    elif command[0] == 'W':
        # 檢查參數數量
        if len(command) != 2:
            print('查無此植物')
            continue

        if command[1] == "":
            print('查無此植物')
            continue
            
        plant_name = command[1]
        if plant_name in plants:
            # 重置澆水時間
            print('澆水成功')
        else:
            print('查無此植物')
    
    # 結束程式
    elif command[0] == '0':
        break
    
    else:
        print('查無此植物')