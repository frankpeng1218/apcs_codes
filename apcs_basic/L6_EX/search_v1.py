import random

#start
# number = random.randint(1, 100)  # 隨機產生1到100之間的整數（此行被註解）
number = 100  # 直接指定目標數字為 100

count = 0  # 猜測次數計數器

for i in range(1, 100+1):  # 從1到100逐一猜測
    if i == number:  # 若猜中目標數字
        print("Computer's number is", i)  # 輸出猜中的數字
        break  # 結束迴圈
    else:
        count += 1  # 若沒猜中，計數器加一

print("count:", count)  # 輸出猜測次數
