# 讀取第一行輸入：金額 C 和 硬幣種類數 N
C, N = map(int, input().split())

# 讀取 N 種硬幣面額
coin = [int(input()) for _ in range(N)]

# 對硬幣進行降序排序（從大到小），確保貪心策略從最大面額開始
coin.sort(reverse=True)

# 嘗試使用不同的硬幣組合，找出最少的硬幣數量
min_nums = float('inf')  # 初始化最少硬幣數量為無限大

# 嘗試從最大面額開始兌換
for i in range(N):
    num = 0      # 計算當前策略下的硬幣總數
    now_C = C    # 記錄當前剩餘金額

    # 貪心策略：優先使用最大面額的硬幣
    for j in range(i, N):  # 從當前面額往下選擇
        num += now_C // coin[j]  # 計算當前面額可以使用幾個硬幣
        now_C %= coin[j]         # 計算剩餘金額

    # 更新最少硬幣數量
    if now_C == 0 and num < min_nums:
        min_nums = num

# 輸出最少的硬幣數
print(min_nums)


# 讀取輸入
C, N = map(int, input().split())

# 讀取 N 種硬幣面額
coin = [int(input()) for _ in range(N)]

# 初始化 DP 陣列，設為無限大（表示該金額目前無法達成）
dp = [float('inf')] * (C + 1)
dp[0] = 0  # 金額 0 時不需要任何硬幣

# 動態規劃求解最少硬幣數
for c in coin:  # 遍歷每個硬幣面額
    for i in range(c, C + 1):  # 嘗試湊出金額 i
        dp[i] = min(dp[i], dp[i - c] + 1)  # 選擇最優解

# 如果無法湊出金額 C，輸出 -1（保險處理）
print(dp[C] if dp[C] != float('inf') else -1)
