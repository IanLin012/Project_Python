# 初始化寵物狀態
hunger = 0  # 飢餓度
mood = 0    # 心情值

# 讀取指令數量
N = int(input())

# 處理每個指令
for i in range(N):
    command = input()
    # 餵食指令
    if command == "feed":
        if(hunger == 0):
            print("寵物已經吃飽了")
        else:
            hunger-=2
            if(hunger < 0):
                hunger = 0
            print("寵物吃得很開心")
            if(hunger >= 5):
                print("寵物餓壞了")
                if(mood > -3):
                    mood-=1
            if(mood == 5):
                print("寵物超級快樂")
            elif(mood == -3):
                print("寵物不開心，需要更多關心")
    
    # 玩耍指令
    elif command == "play":
        if(mood < 5):
            mood+=1
        hunger+=1
        print("寵物玩得很開心")
        if(hunger >= 5):
            print("寵物餓壞了")
            if(mood > -3):
                mood-=1
        if(mood == 5):
            print("寵物超級快樂")
        elif(mood == -3):
            print("寵物不開心，需要更多關心")
        
    # 查看狀態指令
    elif command == "status":
        print("飢餓度：" + str(hunger) + "，心情值：" + str(mood))