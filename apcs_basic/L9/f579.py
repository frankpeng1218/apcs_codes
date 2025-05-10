#
# f579 購買力
#

# 讀入兩個目標商品的價格 a 和 b
a, b = map(int, input().split())

# 讀入顧客數量 n
n = int(input())

# 記錄同時買過 a 和 b 商品的顧客人數
num = 0

# 逐一處理每位顧客的購買記錄
for i in range(n):
    record = list(map(int, input().split()))  # 顧客的交易紀錄，正數為購買，負數為退貨

    buy_A = 0  # 記錄 a 商品的購買數量
    buy_B = 0  # 記錄 b 商品的購買數量

    for x in range(len(record)):
        if record[x] > 0:  # 表示購買商品
            if record[x] == a:
                buy_A += 1  # 購買商品 a 的次數加 1

            if record[x] == b:
                buy_B += 1  # 購買商品 b 的次數加 1

        elif record[x] < 0:  # 表示退貨商品
            if abs(record[x]) == a:
                buy_A -= 1  # 退貨商品 a，數量減 1

            if abs(record[x]) == b:
                buy_B -= 1  # 退貨商品 b，數量減 1

    # 如果這位顧客有買過至少一個 a 和一個 b，則計入 num
    if buy_A > 0 and buy_B > 0:
        num += 1

# 輸出符合條件的顧客總數
print(num)
