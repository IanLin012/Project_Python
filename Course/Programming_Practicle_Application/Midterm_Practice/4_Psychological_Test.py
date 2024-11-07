# 題目資料庫：題目內容、選項分數、分類、權重
questions = {
    "Q1": {
        "scores": {
            "A": {"social": 5, "energy": 4, "stress": 3},
            "B": {"social": 1, "energy": 1, "stress": 1},
            "C": {"social": 3, "energy": 3, "stress": 2},
            "D": {"social": 2, "energy": 2, "stress": 1}
        },
        "weight": 1.0
    },
    "Q2": {
        "scores": {
            "A": {"social": 5, "energy": 3, "stress": 4},
            "B": {"social": 1, "energy": 2, "stress": 2},
            "C": {"social": 3, "energy": 3, "stress": 3},
            "D": {"social": 3, "energy": 4, "stress": 3}
        },
        "weight": 1.2
    },
    "Q3": {
        "scores": {
            "A": {"social": 5, "energy": 4, "stress": 4},
            "B": {"social": 1, "energy": 2, "stress": 2},
            "C": {"social": 2, "energy": 2, "stress": 3},
            "D": {"social": 3, "energy": 3, "stress": 3}
        },
        "weight": 1.5
    }
}

# 分析結果的描述
analysis_descriptions = {
    "social": {
        "high": "你是個非常外向的人，喜歡社交活動和團體互動。",
        "medium": "你在社交方面保持平衡，既能享受群體活動，也能獨處。",
        "low": "你偏好獨處，在獨自工作或活動時表現最佳。"
    },
    "energy": {
        "high": "你充滿活力，經常能夠帶動氣氛。",
        "medium": "你的精力分配平均，知道何時該活躍何時該休息。",
        "low": "你較為保守地使用精力，喜歡平靜的環境。"
    },
    "stress": {
        "high": "你在壓力處理上可能需要多加注意。",
        "medium": "你對壓力有一定的耐受度，但仍需注意調節。",
        "low": "你善於管理壓力，能夠保持良好的心理狀態。"
    }
}

# 建議內容
suggestion_descriptions = {
    "social": {
        "high": "善用你的社交能力，但也要注意留出獨處的時間",
        "medium": "保持目前的社交節奏，在需要時尋求社交支持",
        "low": "可以嘗試逐步增加社交活動，培養人際關係"
    },
    "energy": {
        "high": "注意分配精力，避免過度消耗",
        "medium": "維持當前的活動節奏，適時調整步調",
        "low": "可以嘗試增加一些有趣的活動來提升活力"
    },
    "stress": {
        "high": "學習壓力管理技巧，注意放鬆和休息",
        "medium": "保持正向心態，適時尋求支持",
        "low": "繼續保持良好的壓力管理方式"
    }
}


def check_length(answers_input):
    """
    檢查輸入長度是否正確

    參數：
        answers_input: 使用者輸入的字串

    返回：
        如果長度正確返回True，否則返回False
    """
    if(len(answers_input) == 3):
        return True
    else:
        return False
    pass


def check_options(answers_input):
    """
    檢查選項是否都是ABCD

    參數：
        answers_input: 使用者輸入的字串

    返回：
        如果選項都合法返回True，否則返回False
    """
    cnt = 0
    for choice in answers_input:
        if(choice == "A" or choice == "B" or choice == "C" or choice == "D"):
            cnt+=1
    if(cnt == 3):
        return True
    else:
        return False
    pass


def validate_input(answers_input):
    """
    驗證輸入是否合法

    參數：
        answers_input: 使用者輸入的字串

    返回：
        如果輸入合法返回True，否則返回False
    """
    if(check_length(answers_input) == False):
        print("輸入錯誤:請輸入3個選項")
        return False
    elif(check_options(answers_input) == False):
        print("輸入錯誤:選項必須是A、B、C或D")
        return False
    else:
        return True
    pass


def calculate_scores(answers):
    """
    計算測驗得分
    """
    social = questions["Q1"]["scores"][answers["Q1"]]["social"] * questions["Q1"]["weight"] + questions["Q2"]["scores"][answers["Q2"]]["social"] * questions["Q2"]["weight"] + questions["Q3"]["scores"][answers["Q3"]]["social"] * questions["Q3"]["weight"]
    energy = questions["Q1"]["scores"][answers["Q1"]]["energy"] * questions["Q1"]["weight"] + questions["Q2"]["scores"][answers["Q2"]]["energy"] * questions["Q2"]["weight"] + questions["Q3"]["scores"][answers["Q3"]]["energy"] * questions["Q3"]["weight"]
    stress = questions["Q1"]["scores"][answers["Q1"]]["stress"] * questions["Q1"]["weight"] + questions["Q2"]["scores"][answers["Q2"]]["stress"] * questions["Q2"]["weight"] + questions["Q3"]["scores"][answers["Q3"]]["stress"] * questions["Q3"]["weight"]
    score = {"social": social, "energy": energy, "stress": stress}
    return(score)
    pass


def get_level(score):
    """
    根據分數判斷等級
    """
    if(score >= 15):
        return("high")
    elif(score >= 10):
        return("medium")
    else:
        return("low")
    pass


def get_analysis(scores):
    """
    根據得分給出分析結果
    """
    print("測驗結果分析:")
    print("社交傾向:" + analysis_descriptions["social"][get_level(scores["social"])])
    print("能量特質:" + analysis_descriptions["energy"][get_level(scores["energy"])])
    print("壓力管理:" + analysis_descriptions["stress"][get_level(scores["stress"])])
    pass


def generate_suggestions(scores):
    """
    根據分析結果給出建議
    """
    print("\n給你的建議:")
    print("1. 社交方面:" + suggestion_descriptions["social"][get_level(scores["social"])])
    print("2. 能量管理:" + suggestion_descriptions["energy"][get_level(scores["energy"])])
    print("3. 壓力調適:" + suggestion_descriptions["stress"][get_level(scores["stress"])])
    pass


# **************
# 以下請勿修改!
# **************

answers_input = input().strip()

# 驗證輸入
if validate_input(answers_input):
    answers = {
        f"Q{j + 1}": answer
        for j, answer in enumerate(answers_input)
    }

    scores = calculate_scores(answers)
    get_analysis(scores)
    generate_suggestions(scores)