# start

N = int(input())  # 讀入一個整數 N，代表要檢查 1 到 N 之間的數

# 依序檢查每一個數 i（從 1 到 N）
for i in range(1, N + 1):
    isPrime = True  # 假設 i 是質數，之後再檢查是否被推翻

    # 檢查 i 是否能被 2 到 i 整除
    for j in range(2, i + 1):

        # 如果 i 可以被 j 整除，且 j 不是 i 本身
        # 表示 i 有其他因數，不是質數
        if i % j == 0 and j != i:
            isPrime = False  # 標記為非質數

        # 如果 j 已經走到 i，而且之前都沒有被判定為非質數
        # 表示 i 只有 1 和自己兩個因數，是質數
        elif j == i and isPrime == True:
            print(i)  # 輸出質數 i
