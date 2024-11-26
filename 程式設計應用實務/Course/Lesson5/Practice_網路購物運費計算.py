def calculate_shipping(total_amount, use_coupon=False):
    if(total_amount >= 1000):
        shipping_fee = 0
    elif(use_coupon == True):
        shipping_fee = 100-20
    else:
        shipping_fee = 100
    print(f"最終運費: {shipping_fee} 元")

calculate_shipping(1200)
calculate_shipping(800, use_coupon=True)
calculate_shipping(600)