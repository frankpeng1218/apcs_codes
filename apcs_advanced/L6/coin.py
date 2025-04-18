coins = list(map(int, input().split()))  # 讀入硬幣面額，並轉為整數列表
money = int(input())  # 讀入欲兌換的總金額

num = 0  # 紀錄所需硬幣數量

for i in range(len(coins)-1, -1, -1):  # 從最大面額開始往下找
    num = num + money // coins[i]  # 加上可使用的硬幣數量
    money = money % coins[i]  # 更新剩餘金額

print(num)  # 輸出總共使用的硬幣數量
