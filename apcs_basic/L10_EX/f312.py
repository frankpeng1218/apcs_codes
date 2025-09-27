# f312. 1. 人力分配

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())

# 初始化最大收益
max_benefit = -99999 # 或寫float("-inf") 因為常數有可能是負數，導致收益變成負數

# 窮舉所有可能
for i in range(0, n+1):
    x1 = i
    x2 = n - x1
    # 計算收益
    y1 = a1 * x1 * x1 + b1 * x1 + c1
    y2 = a2 * x2 * x2 + b2 * x2 + c2
    y_total = y1 + y2
    # 比較和更新最大收益
    if y_total > max_benefit:
        max_benefit = y_total

print(max_benefit)
