def find_change(price, paid):
    change = paid-price
    fifty = change // 50
    ten = (change - 50*fifty) // 10
    five = (change - 50*fifty - 10*ten) // 5
    one = change - 50*fifty - 10*ten - 5*five
    return("50元：" + str(fifty) + ", 10元：" + str(ten) + ", 5元：" + str(five) + ", 1元：" + str(one))

price = int(input("請輸入應付金額："))
paid = int(input("請輸入支付金額："))
result = find_change(price, paid)
print(result)