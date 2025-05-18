# 讀取 n（商品數量）和 d（波動條件）
n, d = map(int, input().split())

total, buy = 0, 0  # total: 符合條件的商品數量, buy: 總購買費用

for _ in range(n):
    prices = list(map(int, input().split()))  # 讀取該商品的 3 天價格
    if max(prices) - min(prices) >= d:  # 若價格波動 >= d
        total += 1
        buy += sum(prices) // 3  # 計算該商品的平均價格並累加

print(total, buy)  # 輸出結果
