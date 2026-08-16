# d487. Order's computation process
# 1. 遞迴計算階乘

import sys

def func(n):
    # 遞迴函式：計算 n! 並同時輸出過程
    if n == 1:
        print(" 1", end="")   # 當 n 為 1 時，印出最後的 1（不再加乘號）
        return 1              # 回傳 1 作為遞迴終止條件
    else:
        print(f" {n} *", end="")  # 印出目前的 n 及乘號
        return n * func(n - 1)    # 遞迴呼叫 func(n-1)，累乘結果

# 從標準輸入讀取多筆數字
for s in sys.stdin:
    n = int(s)
    if n == 0:
        # 特例處理：0! 定義為 1
        print("0! = 1 = 1")
    else:
        # 印出階乘計算過程與結果
        print(f"{n}! =", end="")  # 先印出 "n! ="
        ans = func(n)             # 呼叫遞迴函式計算 n!
        print(f" = {ans}")        # 印出最終結果



###因為範圍很小可以這樣做，但不建議
import sys

for s in sys.stdin:
    n = int(s)
    
    if n == 0:
        print("0! = 1 = 1")
    elif n == 1:
        print("1! = 1 = 1")
    elif n == 2:
        print("2! = 2 * 1 = 2")
    elif n == 3:
        print("3! = 3 * 2 * 1 = 6")
    elif n == 4:
        print("4! = 4 * 3 * 2 * 1 = 24")
    elif n == 5:
        print("5! = 5 * 4 * 3 * 2 * 1 = 120")
    elif n == 6:
        print("6! = 6 * 5 * 4 * 3 * 2 * 1 = 720")
    elif n == 7:
        print("7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040")
    elif n == 8:
        print("8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320")
    elif n == 9:
        print("9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362880")
    elif n == 10:
        print("10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800")
