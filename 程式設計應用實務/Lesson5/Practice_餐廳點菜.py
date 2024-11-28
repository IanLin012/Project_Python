def calculate_total_price(menu, order):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
    return(total)


total_price = calculate_total_price({"漢堡": 50, "薯條": 30, "可樂": 20}, ["漢堡", "薯條", "可樂"])
print("餐點總價格：" + str(total_price))