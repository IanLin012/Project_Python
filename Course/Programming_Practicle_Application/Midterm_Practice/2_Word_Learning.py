# 儲存所有單字卡的字典
vocabulary = {}


def add_word(word, meaning, difficulty):
    """
    新增單字卡到系統中

    參數:
        word: 英文單字
        meaning: 中文解釋
        difficulty: 難度等級(1-5)

    輸出範例:
        成功: "成功新增單字卡: apple"

    錯誤訊息:
        - 單字重複: "錯誤: 單字 'apple' 已存在"
        - 無效難度: "錯誤: 難度等級必須在1-5之間"
    """
    if(word in vocabulary):
        print("錯誤: 單字 '" + word + "' 已存在")
        return False
    elif(difficulty < 1 or difficulty > 5):
        print("錯誤: 難度等級必須在1-5之間")
        return False
    else:
        vocabulary[word] = {"word": word, "meaning": meaning, "difficulty": difficulty, "review": 0, "master": "學習中"}
        print("成功新增單字卡: " + word)
        return True


def mark_as_mastered(word):
    """
    將指定單字標記為已掌握

    參數:
        word: 英文單字

    輸出範例:
        成功: "已將 'apple' 標記為已掌握!"

    錯誤訊息:
        - 單字不存在: "錯誤: 找不到單字 'book'"
    """
    if(word not in vocabulary):
        print("錯誤: 找不到單字 '" + word + "'")
        return False
    else:
        vocabulary[word]["master"] = "已掌握"
        print("已將 '" + word + "' 標記為已掌握!")
        return True


def review_word(word):
    """
    更新單字的複習次數

    參數:
        word: 英文單字

    輸出範例:
        成功: "已更新 'apple' 的複習次數: 1"

    錯誤訊息:
        - 單字不存在: "錯誤: 找不到單字 'book'"
    """
    if(word not in vocabulary):
        print("錯誤: 找不到單字 '" + word + "'")
        return False
    else:
        vocabulary[word]["review"] += 1
        print("已更新 '" + word + "' 的複習次數:", vocabulary[word]["review"])
        return True


def check_word_info(word):
    """
    查詢單字的詳細資訊

    參數:
        word: 英文單字

    輸出範例:
        成功:
            "單字: apple"
            "中文解釋: 蘋果"
            "難度等級: 1"
            "複習次數: 2"
            "掌握狀態: 已掌握"

    錯誤訊息:
        - 單字不存在: "錯誤: 找不到單字 'book'"
    """
    if(word not in vocabulary):
        print("錯誤: 找不到單字 '" + word + "'")
        return False
    else:
        print("單字:", vocabulary[word]["word"])
        print("中文解釋:", vocabulary[word]["meaning"])
        print("難度等級:", vocabulary[word]["difficulty"])
        print("複習次數:", vocabulary[word]["review"])
        print("掌握狀態:", vocabulary[word]["master"])
        return True

def list_words_by_difficulty(level):
    """
    列出指定難度等級的所有單字

    參數:
        level: 難度等級(1-5)

    輸出範例:
        成功有單字:
            "難度等級 5 的單字："
            "- algorithm: 演算法"
        成功但無單字:
            "難度等級 2 的單字："
            "沒有難度等級為 2 的單字"

    錯誤訊息:
        - 無效難度: "錯誤: 難度等級必須在1-5之間"
    """
    if(level < 1 or level > 5):
        print("錯誤: 難度等級必須在1-5之間")
        return False
    else:
        print("難度等級", level, "的單字：")
        cnt = 0
        for word in vocabulary:
            if(vocabulary[word]["difficulty"] == level):
                cnt += 1
                print("-", vocabulary[word]["word"] + ":", vocabulary[word]["meaning"])
        if(cnt == 0):
            print("沒有難度等級為", level, "的單字")
        return True


def show_progress_report():
    """
    顯示整體學習進度報告

    輸出範例:
        有單字時:
            "學習進度報告:"
            "總單字數: 3"
            "已掌握單字數: 1"
            "總複習次數: 3"
            "掌握率: 33.3%" 

        無單字時:
            "目前沒有任何單字卡"
    """
    if(len(vocabulary) == 0):
        print("目前沒有任何單字卡")
        return False
    else:
        print("學習進度報告:")
        master_cnt, review_cnt = 0, 0
        for word in vocabulary:
            if(vocabulary[word]["master"] == "已掌握"):
                master_cnt += 1
            review_cnt += vocabulary[word]["review"]
        print("總單字數:", len(vocabulary))
        print("已掌握單字數:", master_cnt)
        print("總複習次數:", review_cnt)
        master_rate = master_cnt / len(vocabulary)
        print("掌握率: {:.1%}".format(master_rate))
        return True


# **************
# 以下請勿修改!
# **************

# 讀取操作數量
n = int(input())

# 執行操作
for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == "add":
        # add word meaning difficulty
        add_word(command[1], command[2], int(command[3]))
    elif operation == "master":
        # master word
        mark_as_mastered(command[1])
    elif operation == "review":
        # review word
        review_word(command[1])
    elif operation == "check":
        # check word
        check_word_info(command[1])
    elif operation == "list":
        # list difficulty_level
        list_words_by_difficulty(int(command[1]))
    elif operation == "report":
        # report
        show_progress_report()