l = input("請輸入一個列表：").split(', ')
for i in range(len(l)):
    l[i] = int(l[i])
print("Max: " + str(max(l)))
print("Min: " + str(min(l)))