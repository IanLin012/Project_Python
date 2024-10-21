def calculate_discount(amount):
    if(0 <= amount <= 1000):
        return(amount)
    elif(1000 < amount < 5000):
        return(amount * 0.9)
    elif(amount >= 5000):
        return(amount * 0.8)

price = int(input("請輸入購物金額："))
final_price = calculate_discount(price)
print("折扣後的價格為：" + str(int(final_price)))