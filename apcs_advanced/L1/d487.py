# Frank解題影片：https://www.youtube.com/watch?v=NTceUiGJEeo

# d487. Order's computation process
# 知識點: 遞歸
import sys

# 遞迴函式計算階乘並輸出計算過程
def func(n):
    if n == 1:  # 遞迴終止條件
        print(" 1", end="")  # 輸出 1，表示階乘計算的最後一項
        return 1  # 回傳 1 作為基礎值
    else:
        print(f" {n} *", end="")  # 輸出當前數字及乘號
        return n * func(n - 1)  # 遞迴計算 n * (n-1)!

# 讀取輸入並處理
for s in sys.stdin:
    n = int(s)  # 讀取輸入的整數
    if n == 0:  # 特殊處理 0! 的情況
        print("0! = 1 = 1")
    else:
        print(f"{n}! =", end="")  # 輸出階乘的標題
        ans = func(n)  # 呼叫遞迴函式計算階乘
        print(f" = {ans}")  # 輸出最終結果
