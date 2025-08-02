def g(a):
    # 當 a > 1 時，進行遞迴計算
    if a > 1:
        # g(a) 的計算方式是 g(a-1) + 2
        # 這表示 g(a) 會呼叫自身函式 g(a-1)，並在其結果上加 2
        return g(a - 1) + 2
    else:
        # 當 a == 1 時，根據定義直接回傳 2
        # 這是遞迴的基礎條件 (base case)，確保遞迴可以終止
        return 2

# 程式開始執行
N = int(input())  # 讀取使用者輸入的整數 N
print(g(N))  # 呼叫函式 g(N) 並輸出結果
