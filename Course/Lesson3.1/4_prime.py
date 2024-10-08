n = int(input("請輸入一個數："))
if(n == 1):
    print("1 不是質數")
elif(n == 2):
    print("2 不是質數")
else:
    for i in range(2, n):
        if(n%i == 0):
            print(str(n) + " 不是質數")
            break
        elif(i == n-1):
            print(str(n) + " 是質數")