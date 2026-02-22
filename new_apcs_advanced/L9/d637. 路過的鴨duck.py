# d637: 路過的鴨 duck
# 0/1 背包問題

# 讀入鴨飼料顆數
pellet_count = int(input())

# 每顆鴨飼料的重量與價值
pellet_weights = []
pellet_values = []

# 讀入每顆飼料的 (重量, 價值)
for _ in range(pellet_count):
    a, b = map(int, input().split())
    pellet_weights.append(a)
    pellet_values.append(b)

# 背包最大容量（固定 100）
max_capacity = 100

# dp[i][j] 表示：
# 前 i 顆鴨飼料
# 在容量 j 的情況下
# 可以得到的最大價值
dp = [[0 for _ in range(max_capacity + 1)] for _ in range(pellet_count + 1)]

# 動態規劃
for i in range(pellet_count):                  # 第 i 顆飼料
    for capacity in range(max_capacity + 1):   # 容量 0~100
        
        # 容量不足，不能放這顆
        if capacity < pellet_weights[i]:
            dp[i+1][capacity] = dp[i][capacity]
        else:
            dp[i+1][capacity] = max(
                dp[i][capacity],  # 不放當前鴨飼料
                pellet_values[i] + dp[i][capacity - pellet_weights[i]]  # 放當前鴨飼料
            )

# 輸出最大價值
print(dp[pellet_count][max_capacity])