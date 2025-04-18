import random

#start
number = random.randint(1, 100)  # 隨機產生1到100之間的整數作為目標數字

lower = 0  # 搜尋下界
upper = 100  # 搜尋上界

i = 50  # 初始猜測值
count = 0  # 猜測次數計數器

while True:
    if i == number:  # 若猜中目標數字
        print("Computer's number is", i)  # 輸出猜中的數字
        print("count:", count)  # 輸出猜測次數
        break  # 結束迴圈

    count += 1  # 每猜一次就加一

    if i < number:
        lower = i  # 更新下界
        i = int((lower + upper) / 2)  # 使用二分搜尋策略更新猜測值
    elif i > number:
        upper = i  # 更新上界
        i = int((lower + upper) / 2)  # 使用二分搜尋策略更新猜測值

    print("i=%d, lower=%d, upper=%d" % (i, lower, upper))  # 輸出每次猜測的狀態
