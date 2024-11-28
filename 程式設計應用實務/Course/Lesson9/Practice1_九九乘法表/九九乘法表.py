file = open(r"Project_Python\程式設計應用實務\Course\Lesson9\Practice1_九九乘法表\output.txt", "w", encoding='utf-8') # 以寫入模式打開檔案

for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            file.write(f"{i} x {j} = {i*j},\n")
        else:
            file.write(f"{i} x {j} = {i*j}, ")
            
file.close() # 關閉檔案