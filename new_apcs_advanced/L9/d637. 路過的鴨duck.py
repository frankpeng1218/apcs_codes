# d637: 路過的鴨 duck
# 這是一題 0/1 背包問題

# 讀入鴨子數量
n = int(input())

# w = 每隻鴨子的重量
# v = 每隻鴨子的價值
v = []
w = []

# 讀入每隻鴨子的 (重量, 價值)
for _ in range(n):
    wa, vb = map(int, input().split())
    w.append(wa)   # 重量
    v.append(vb)   # 價值


# 建立 dp 表
# dp[i][j] 表示：
#   前 i 隻鴨子
#   在容量 j 的情況下
#   可以得到的最大價值

dp = [ [0 for j in range(100+1)] for i in range(n+1) ]


# 開始做動態規劃
for i in range(0, n):         # 處理第 i 隻鴨子
    for j in range(0, 101):   # 背包容量從 0~100
        
        # 如果容量不足放第 i 隻鴨子
        if j - w[i] < 0:
            # 那只能選擇不放
            dp[i+1][j] = dp[i][j]
        
        else:
            # 兩種選擇：
            # 不放第 i 隻鴨子
            # 放第 i 隻鴨子
            dp[i+1][j] = max(
                dp[i][j],                    # 不放
                v[i] + dp[i][j - w[i]]       # 放
            )

# 輸出答案
# 前 n 隻鴨子，容量 100 時的最大價值
print(dp[n][100])
