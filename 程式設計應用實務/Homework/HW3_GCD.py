# # recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = input("請輸入第一個數：")
num2 = input("請輸入第二個數：")
result = gcd(int(num1), int(num2))

print(num1 + " 和 " + num2 + " 的最大公因數是 " + str(result))