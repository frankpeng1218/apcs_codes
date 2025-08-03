N = int(input())  # 讀取輸入的整數 N，表示要找出 1 到 N 之間的所有質數

# 遍歷 1 到 N 之間的所有數字，檢查它們是否為質數
for i in range(1, N+1):
    isPrime = True  # 預設 i 是質數

    # 檢查 i 是否能被 2 到 i 之間的數字整除
    for j in range(2, i+1):
        if i % j == 0 and j != i:  # 如果 i 除以 j 餘數為 0，且 j 不是 i 本身，則 i 不是質數
            isPrime = False

        elif j == i and isPrime == True:  # 當 j 遍歷到 i 本身，且仍為質數時，輸出 i
            print(i)
