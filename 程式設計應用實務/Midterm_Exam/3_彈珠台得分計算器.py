def calculate_score(area):
    """
    計算單一區域的得分
    參數 area: 區域代號 (S、D、T 或 X)
    回傳: 該區域的得分
    """
    # S 回傳 10 分
    # D 回傳 20 分
    # T 回傳 30 分
    # X 回傳 0 分
    if(area == "S"):
        return(10)
    elif(area == "D"):
        return(20)
    elif(area == "T"):
        return(30)
    elif(area == "X"):
        return 0

def get_feedback(total_score):
    """
    根據總分給出評語
    參數 total_score: 總分數
    回傳: 對應的評語
    """
    # 0 分回傳「再努力一點!」
    # 1-40 分回傳「表現不錯!」
    # 41-80 分回傳「太厲害了!」
    # 80 分以上回傳「登峰造極!」
    if(total_score == 0):
        return("再努力一點!")
    elif(1<=total_score<=40):
        return("表現不錯!")
    elif(41<total_score<=80):
        return("太厲害了!")
    elif(total_score>80):
        return("登峰造極!")


# 讀取彈珠數量
n = int(input())

# 讀取每顆彈珠打到的區域
areas = input().split()

# 計算總分
total = 0
for area in areas:
    total += calculate_score(area)

# 輸出結果
print(total)
print(get_feedback(total))