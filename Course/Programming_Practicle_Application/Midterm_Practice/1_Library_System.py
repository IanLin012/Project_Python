# 建立一個空的字典來儲存所有書籍
library = {}
library_status = {}

def add_book(title, author, year):
    """
    新增書籍到圖書館
    參數:
    title: 書名
    author: 作者
    year: 出版年份

    輸出範例:
        成功: "成功新增書籍: Python入門"

    錯誤訊息:
        - 書籍重複: "錯誤: Python入門 已存在圖書館"
    """
    if(title in library):
        print("錯誤: " + title + " 已存在圖書館")
    else:
        library[title] = {"author": author, "year": year, "is_borrowed": False}
        library_status[title] = {"title": title, "author": author, "year": year, "status": '可借閱'}
        print("成功新增書籍: " + title)
    return True

def borrow_book(title):
    """
    借出書籍
    參數:
    title: 書名
    
    輸出範例:
        成功: "成功借出: 程式設計"

    錯誤訊息:
        - 找不到: "錯誤: 找不到書籍 資料結構"
        - 已被借出: "錯誤: 程式設計 已被借出"
    """
    if(title not in library):
        print("錯誤: 找不到書籍 " + title)
        return False
    elif(library[title]["is_borrowed"] == False):
        library[title]["is_borrowed"] = True
        library_status[title]["status"] = '已借出'
        print("成功借出: " + title)
    elif(library[title]["is_borrowed"] == True):
        print("錯誤: " + title + " 已被借出")
    return True

def return_book(title):
    """
    歸還書籍
    參數:
    title: 書名

    輸出範例:
        成功: "成功歸還: Python入門"

    錯誤訊息:
        - 找不到: "錯誤: 找不到書籍 資料結構"
        - 未被借出: "錯誤: 網頁設計 未被借出"
    """
    if(title not in library):
        print("錯誤: 找不到書籍 " + title)
        return False
    elif(library[title]['is_borrowed'] == True):
        library[title]["is_borrowed"] = False
        library_status[title]["status"] = '可借閱'
        print("成功歸還: " + title)
        return True
    elif(library[title]['is_borrowed'] == False):
        print("錯誤: " + title + " 未被借出")
        return True

def check_book_status(title):
    """
    查詢特定書籍狀態
    參數:
    title: 書名

    可設計新的 dict 來顯示狀態

    輸出範例:
        成功: "網頁設計 狀態: {'title': '網頁設計', 'author': '王五', 'year': 2023, 'status': '可借閱'}"

    錯誤訊息:
        - 找不到: "錯誤: 找不到書籍 演算法"
        - 未被借出: "錯誤: 網頁設計 未被借出"
    """
    if(title not in library):
        print("錯誤: 找不到書籍 " + title)
        return False
    else:
        print(title + " 狀態:", library_status[title])
    return True

def list_borrowed_books():
    """
    列出所有已借出的書籍

    輸出範例:
        成功: "{title}: {借閱狀態}"
                網頁設計: {'author': '王五', 'year': 2023, 'is_borrowed': True}

    錯誤訊息:
        - 沒有已借出: "目前沒有已借出的書籍"

    """
    cnt = 0
    for title in library:
        if(library[title]["is_borrowed"] == True):
            cnt += 1
            print(title + ":", library[title])
    if(cnt == 0):
        print("目前沒有已借出的書籍")
    return

def list_author_books(author):
    """
    列出特定作者的所有書籍
    參數:
    author: 作者名稱

    輸出範例:
        成功: "{'author': '王五', 'year': 2023, 'is_borrowed': False}
                {'author': '王五', 'year': 2023, 'is_borrowed': False}"

    錯誤訊息:
        - 未知作者: "找不到 李四 的書"
    """
    cnt = 0
    for title in library:
        if(library[title]["author"] == author):
            cnt += 1
            print(library[title])
    if(cnt == 0):
        print("找不到 " + author + " 的書")
    return 

# **************
# 以下請勿修改!
# **************

# 讀取操作數量
n = int(input())
# 處理每個操作
for _ in range(n):
    # 讀取並分割指令
    operation = input()
    parts = operation.split()
    command = parts[0]

    if command == "add":
        # 格式: add 書名 作者 年份
        title, author, year = parts[1], parts[2], int(parts[3])
        add_book(title, author, year)

    elif command == "borrow":
        # 格式: borrow 書名
        title = parts[1]
        borrow_book(title)

    elif command == "return":
        # 格式: return 書名
        title = parts[1]
        return_book(title)

    elif command == "check":
        # 格式: check 書名
        title = parts[1]
        check_book_status(title)

    elif command == "list_borrowed":
        # 格式: list_borrowed
        list_borrowed_books()

    elif command == "list_author":
        # 格式: list_author 作者
        author = parts[1]
        list_author_books(author)