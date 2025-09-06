# 讀取輸入
s = input()
C, N = map(int, s.split())  # C: 需要找零的金額, N: 硬幣種類數量

# 建立硬幣面值列表
coin = []  
method = [0 for i in range(50001)]  # method[i] 表示找零 i 元所需的最少硬幣數量（最大找零金額限制為 50000）

# 讀取 N 種硬幣的面值
for i in range(N):
    coin.append(int(input()))  # 每次讀一個硬幣面值並加入 coin 清單

# 初始化 DP 陣列
method[0] = 0  # 找零 0 元時，不需要任何硬幣
for i in range(1, C + 1):
    method[i] = 100000  # 初始化為一個大數值（相當於無限大），後續用來取最小值

# 動態規劃：計算每個金額的最小找零方法數
for i in range(N):  # 遍歷所有硬幣種類
    for j in range(coin[i], C + 1):  # j 從目前硬幣面值開始，一直到總金額 C
        # 若使用這個硬幣能讓找零更有效率（需要更少的硬幣數），則更新 method[j]
        if method[j] > method[j - coin[i]] + 1:
            method[j] = method[j - coin[i]] + 1  # +1 是因為用了 coin[i] 這枚硬幣

# 輸出答案：找零 C 元所需的最少硬幣數量
print(method[C])





####第二種
# 讀取輸入：C = 需要找零的金額, N = 硬幣種類數
C, N = map(int, input().split())

# 讀取硬幣面值
coins = [int(input()) for _ in range(N)]

# dp[i] = 湊出 i 元所需的最少硬幣數量
# 先全部設成無限大 (float('inf'))，表示暫時湊不出來
dp = [float('inf')] * (C + 1)

# 找零 0 元需要 0 枚硬幣
dp[0] = 0

# 動態規劃：逐一處理每個硬幣
for coin in coins:
    for amount in range(coin, C + 1):
        dp[amount] = min(dp[amount], dp[amount - coin] + 1)

# 輸出答案
print(dp[C])

# Example
# C = 11
# N = 3
# 硬幣 = 1, 5, 7
