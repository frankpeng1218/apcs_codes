# n129: 鋪磁磚問題
# 動態規劃（DP）
# 三階遞推公式（Tribonacci）

n = int(input())

# ways[i] 表示：鋪滿 i 格磁磚的不同方法數
# 因為遞推公式需要用到 ways[0]、ways[1]、ways[2]
# 所以陣列長度至少要到 index = 2（因此用 max(n, 2)）
ways = [0] * (max(n, 2) + 1)

# 基本情況（Base Case）
ways[0] = 1  # 不鋪也是一種方法（DP 常見定義）
ways[1] = 1  # 長度 1，只能放 1x1 磁磚，只有 1 種
ways[2] = 2  # 長度 2：可以 (1+1) 或 (2) → 共 2 種

# 遞推公式（Tribonacci）
# ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
# 最後一塊磁磚可以選長度 1、2、3
for i in range(3, n + 1):
    ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

# 輸出鋪滿 n 格的所有方法數
print(ways[n])


####################################
n = int(input())

# 特判 n = 0, 1, 2（直接輸出結果，不跑 DP）
if n == 0:
    print(1)  # 不鋪也是 1 種方法
elif n == 1:
    print(1)  # 只能放 1x1
elif n == 2:
    print(2)  # (1+1) 或 (2)
else:
    # 進入一般 DP（n >= 3）
    # ways[i] 表示鋪滿 i 格的方法數
    ways = [0] * (n + 1)

    # Base Case
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    # 遞推：最後一塊磁磚可以是 1、2、3
    for i in range(3, n + 1):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

    # 輸出答案
    print(ways[n])
####################################
n = int(input())

if n < 3:
    print([1, 1, 2][n])
else:
    a, b, c = 1, 1, 2
    for i in range(3, n+1):
        a, b, c = b, c, a + b + c
    print(c)
