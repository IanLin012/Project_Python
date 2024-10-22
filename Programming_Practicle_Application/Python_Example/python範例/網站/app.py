from flask import Flask, render_template


app = Flask(__name__) # 初始化時傳入的參數，讓 Flask 知道在哪裡尋找資源

@app.route("/") # 裝飾器，告訴 Flask 哪個 URL 應該觸發我們的函式 (斜線就是網站的根目錄，可疊加)
def hello():
    return "Hello, World!"
