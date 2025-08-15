import random  # 匯入 random 模組

#start
N = int(input())  # 讀取使用者輸入的擲骰子次數
total = 0  # 初始化總和變數

for i in range(N):  # 執行 N 次擲骰子
    point = random.randint(1, 6)  # 隨機產生 1 到 6 之間的數字
    print(point, end=' ')  # 以空格分隔輸出點數
    total += point  # 將點數加到總和
    
print("\n" + str(total))  # 換行後輸出總和
