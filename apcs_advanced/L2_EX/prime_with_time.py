import time  # 匯入 time 模組，用於計算程式執行時間

# 讀取輸入的整數 N，表示要找出 1 到 N 之間的所有質數
N = int(input())

start_time = time.time()  # 記錄程式開始執行的時間

prime = []  # 用於存放所有找到的質數

# 遍歷 1 到 N 之間的所有數字，檢查它們是否為質數
for i in range(1, N+1):
    isPrime = True  # 預設 i 是質數

    # 檢查 i 是否能被 2 到 i 之間的數字整除
    for j in range(2, i+1):
        if i % j == 0 and j != i:  # 如果 i 除以 j 餘數為 0，且 j 不是 i 本身，則 i 不是質數
            isPrime = False

        elif j == i and isPrime == True:  # 當 j 遍歷到 i 本身，且仍為質數時，將 i 加入 prime 陣列
            prime.append(i)

print(prime)  # 輸出找到的所有質數

end_time = time.time()  # 記錄程式結束執行的時間

# 計算並輸出程式執行時間
print("execution time:", (end_time - start_time), "s")
