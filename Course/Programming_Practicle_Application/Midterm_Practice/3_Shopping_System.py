# 商品清單
products = {
    "P001": {"name": "鉛筆", "price": 30, "stock": 20},
    "P002": {"name": "橡皮擦", "price": 20, "stock": 15},
    "P003": {"name": "原子筆", "price": 25, "stock": 10},
    "P004": {"name": "筆記本", "price": 100, "stock": 5}
}

# 優惠券
coupons = {
    "SAVE20": {"discount": 0.8, "description": "所有商品8折"},
    "SAVE50": {"discount": 0.5, "description": "所有商品5折"},
}

# 購物車內容
cart = {
    "items": {},  # 儲存購買的商品
    "coupon": None  # 使用的優惠券
}

def add_to_cart(product_id, quantity):
    """
    新增商品到購物車

    參數:
        product_id: 商品編號
        quantity: 數量

    輸出範例:
        成功:
            "成功將 鉛筆 加入購物車，數量：2"

        錯誤訊息:
            - 商品不存在: "錯誤：找不到商品 P999"
            - 數量錯誤: "錯誤：數量必須為正整數"
            - 庫存不足: "錯誤：鉛筆 庫存不足，目前庫存：5"
    """
    if(product_id not in products):
        print("錯誤：找不到商品", product_id)
        return False
    elif(quantity <= 0):
        print("錯誤：數量必須為正整數")
        return False
    elif(product_id in cart["items"] and products[product_id]["stock"] < cart["items"][product_id]["quantity"] + quantity):
        print("錯誤：" + products[product_id]["name"], "庫存不足，目前庫存：" + str(products[product_id]["stock"]))
        return False
    elif(products[product_id]["stock"] < quantity):
        print("錯誤：" + products[product_id]["name"], "庫存不足，目前庫存：" + str(products[product_id]["stock"]))
        return False
    else:
        cart["items"][product_id] = {"name": products[product_id]["name"], "quantity": quantity, "price": products[product_id]["price"] * quantity}
        print("成功將", products[product_id]["name"], "加入購物車，數量：" + str(quantity))
        return True

def remove_from_cart(product_id):
    """
    從購物車移除商品

    參數:
        product_id: 商品編號

    輸出範例:
        成功: "成功將 鉛筆 從購物車移除"

        錯誤訊息:
            - 商品不在購物車: "錯誤：購物車中沒有此商品"
    """
    if(product_id not in cart["items"]):
        print("錯誤：購物車中沒有此商品")
        return False
    else:
        del cart["items"][product_id]
        print("成功將", products[product_id]["name"], "從購物車移除")
        return True

def update_cart_quantity(product_id, quantity):
    """
    更新購物車中商品的數量

    參數:
        product_id: 商品編號
        quantity: 新數量

    輸出範例:
        成功: "成功更新 鉛筆 的數量為：3"

        錯誤訊息:
            - 商品不在購物車: "錯誤：購物車中沒有此商品"
            - 數量錯誤: "錯誤：數量必須為正整數"
            - 庫存不足: "錯誤：鉛筆 庫存不足，目前庫存：5"
    """
    if(product_id not in cart["items"]):
        print("錯誤：購物車中沒有此商品")
        return False
    elif(quantity <= 0):
        print("錯誤：數量必須為正整數")
        return False
    elif(products[product_id]["stock"] < quantity):
        print("錯誤：" + products[product_id]["name"], "庫存不足，目前庫存：" + str(products[product_id]["stock"]))
        return False
    else:
        cart["items"][product_id]["quantity"] = quantity
        cart["items"][product_id]["price"] = products[product_id]["price"] * quantity
        print("成功更新", products[product_id]["name"], "的數量為：" + str(quantity))
        return True

def apply_coupon(coupon_code):
    """
    使用優惠券

    參數:
        coupon_code: 優惠券代碼

    輸出範例:
        成功: "成功使用優惠券：所有商品8折"

        錯誤訊息:
            - 優惠券不存在: "錯誤：無效的優惠券代碼"
            - 購物車為空: "錯誤：購物車是空的，無法使用優惠券"
    """
    if(len(cart["items"]) == 0):
        print("錯誤：購物車是空的，無法使用優惠券")
        return False
    elif(coupon_code not in coupons):
        print("錯誤：無效的優惠券代碼")
        return False
    else:
        cart["coupon"] = coupons[coupon_code]
        print("成功使用優惠券：" + coupons[coupon_code]["description"])
        return True

def show_cart():
    """
    顯示購物車內容

    輸出範例:
        有商品時:
            "購物車內容："
            "1. 鉛筆 x 2，小計：60元"
            "2. 橡皮擦 x 1，小計：20元"
            "原價總計：80元"
            "使用優惠券：所有商品8折"
            "折扣後總計：64元"

        空購物車:
            "購物車是空的"
    """
    if(len(cart["items"]) == 0):
        print("購物車是空的")
        return False
    else:
        print("購物車內容：")
        num, price = 1, 0
        for product in cart["items"]:
            price += cart["items"][product]["price"]
            print(str(num) + ".", cart["items"][product]["name"], "x", str(cart["items"][product]["quantity"]) + "，小計：" + str(cart["items"][product]["price"]) + "元")
            num += 1
        print("原價總計：" + str(price) + "元")
        if(cart["coupon"] == None):
            return True
        else:
            print("使用優惠券：" + cart["coupon"]["description"])
            print("折扣後總計：" + str(round(price * cart["coupon"]["discount"])) + "元")
            return True

def checkout():
    """
    結帳並更新庫存

    輸出範例:
        成功:
            "結帳成功！"
            "購買商品："
            "1. 鉛筆 x 2"
            "2. 橡皮擦 x 1"
            "總計：64元"

        錯誤訊息:
            - 購物車為空: "錯誤：購物車是空的，無法結帳"
    """
    if(len(cart["items"]) == 0):
        print("錯誤：購物車是空的，無法結帳")
        return False
    else:
        print("結帳成功！")
        print("購買商品：")
        num, price = 1, 0
        for product in cart["items"]:
            price += cart["items"][product]["price"]
            print(str(num) + ".", cart["items"][product]["name"], "x", str(cart["items"][product]["quantity"]))
            products[product]["stock"] -= cart["items"][product]["quantity"]
            num += 1
        if(cart["coupon"] == None):
            print("總計：" + str(round(price, 0)) + "元")
        else:
            print("總計：" + str(round(price * cart["coupon"]["discount"])) + "元")
        cart["items"].clear()
        return True

# **************
# 以下請勿修改!
# **************

# 讀取操作數量
n = int(input())

# 處理每一行指令
for _ in range(n):
    command = input().split()
    operation = command[0]
    
    if operation == "add":
        product_id = command[1]
        quantity = int(command[2])
        add_to_cart(product_id, quantity)
    
    elif operation == "remove":
        product_id = command[1]
        remove_from_cart(product_id)
    
    elif operation == "update":
        product_id = command[1]
        quantity = int(command[2])
        update_cart_quantity(product_id, quantity)
    
    elif operation == "coupon":
        coupon_code = command[1]
        apply_coupon(coupon_code)
    
    elif operation == "show":
        show_cart()
    
    elif operation == "checkout":
        checkout()