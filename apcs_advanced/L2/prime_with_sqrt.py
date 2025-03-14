import time  # 匯入 time 模組，用於計算程式執行時間
import math  # 匯入 math 模組，用於計算平方根

# 找質數的方法：籃子法（篩選法的一種）
# 讀取輸入的整數 N，表示要找出 2 到 N 之間的所有質數
N = int(input())

start_time = time.time()  # 記錄程式開始執行的時間

prime = []  # 用於存放所有找到的質數

# 遍歷 2 到 N 之間的所有數字，檢查它們是否為質數
for i in range(2, N+1):
    isPrime = True  # 預設 i 是質數

    end = int(math.sqrt(i))  # 只需檢查到 i 的平方根，減少運算量
    # print(end)  # 可選擇印出 end 來觀察計算範圍

    # 從 2 到 sqrt(i) 檢查是否有因數
    for j in range(2, end+1):
        if i % j == 0 and j != i:  # 如果 i 能被 j 整除，則 i 不是質數
            isPrime = False

    # 若 isPrime 仍為 True，表示 i 是質數，加入質數列表
    if isPrime == True:
        prime.append(i)

end_time = time.time()  # 記錄程式結束執行的時間

print(prime)  # 輸出所有找到的質數
print("execution time:", (end_time - start_time), "s")  # 計算並輸出程式執行時間
