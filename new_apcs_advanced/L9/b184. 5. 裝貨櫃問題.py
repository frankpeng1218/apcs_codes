# b184: 裝貨櫃問題
# DP 動態規劃
# 0/1 背包問題（Knapsack Problem）

# | 物品 | 重量 v | 價值 c |
# | --  | ----   | ---- |
# | 1   | 3      | 4    |
# | 2   | 4      | 5    |

# dp定義：
# dp[i][j] = 用前 i 個物品、在容量 j 之內可取得的最大價值

# 建立dp 表格 （初始都為0）
# i\j | 0 1 2 3 4 5 6 7 8 9 10 .... 100
# --------------------------------
# 0   | 0 0 0 0 0 0 0 0 0 0 0
# 1   | 0 0 0 4 4 4 4 4 4 4 4
# 2   | 0 0 0 4 5 5 5 9 9 9 9

while True:
    try:
        N = int(input())      # 物品數量（有幾個貨物）

        v = []                # 每個物品的重量 value（題目叫做重量）
        c = []                # 每個物品的價值 cost（題目叫做金額）

        # dp[i][j] = 用前 i 個物品、在重量上限 j 之內，可以得到的最大價值
        dp = []

        for i in range(N + 1):      # 要 N+1 列
            row = []                # 每一列都是新的 list
            for j in range(101):    # 每列要 101 個欄位
                row.append(0)       # 預設填 0
            dp.append(row)          # 把這一列加入 dp


        # 讀取 N 個物品（重量 a、價值 b）
        for _ in range(N):
            a, b = map(int, input().split())
            v.append(a)       # 重量
            c.append(b)       # 價值


        # 動態規劃填表
        # i = 第 i 個物品（0-based）
        # j = 重量上限從 0 到 100
        for i in range(0, N):
            for j in range(0, 100 + 1):

                # 如果重量 j 無法放下第 i 個物品（重量 v[i]）
                if j - v[i] < 0:
                    # 不能放 → 繼承不放這個物品的結果
                    dp[i + 1][j] = dp[i][j]

                else:
                    # 否則可以選擇：
                    # 1. 不放這個物品 → dp[i][j]
                    # 2. 放這個物品 → c[i] + dp[i][j - v[i]]
	            # c[i]當下物品的利潤, dp[i][j-v[i]]代表當下的重量又可以再放下當下的物品v[i]
                    # 取最大值（最大價值）
                    dp[i + 1][j] = max(dp[i][j],
                                       c[i] + dp[i][j - v[i]])

        # dp[N][100] = 用所有 N 個物品，重量上限 100 的最佳價值
        print(dp[N][100])

    except:
        break  # 輸入結束