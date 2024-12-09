import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

print("ilearn2")
response1 = requests.get("https://ilearn2.fcu.edu.tw/", headers=headers)
print(type(response1))
print(response1.text)
print("fcu")

response2 = requests.get("https://www.fcu.edu.tw/")
print(type(response2))
print(response2.text)
print("yahoo")

response3 = requests.get("https://tw.stock.yahoo.com/")
print(type(response3))
print(response3.text)