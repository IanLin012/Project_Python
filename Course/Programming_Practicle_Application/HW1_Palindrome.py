s = input("請輸入檢查回文的字串：")
rev_s = s[::-1]
if(s == rev_s):
    print(s + " 是迴文")
else:
    print(s + " 不是迴文")