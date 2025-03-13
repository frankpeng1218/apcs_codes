#start

N = int(input())  # 讀取使用者輸入的整數 N

sum = 0  # 初始化總和變數 sum 為 0

# 迴圈從 1 到 N，計算總和
for i in range(1, N + 1):
    sum = sum + i  # 將當前數字 i 加到 sum 中
    
print(sum)  # 輸出總和
