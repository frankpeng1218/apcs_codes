# Frank解題影片：https://www.youtube.com/watch?v=fZV00v3-Ouw

# e357. 遞迴函數練習
# 知識點: 遞歸

import sys

# 定義遞迴函式 f(n)
def f(n):
    if n == 1:  # 遞迴終止條件
        return 1
    elif n % 2 == 0:  # 若 n 為偶數，則對 n/2 遞迴計算
        return f(n // 2)  # 使用整數除法，確保結果為整數
    else:  # 若 n 為奇數，則計算 f(n-1) + f(n+1)
        return f(n - 1) + f(n + 1)

# 讀取輸入並處理
for s in sys.stdin:
    N = int(s)  # 讀取使用者輸入的整數 N
    print(f(N))  # 輸出函式計算結果
