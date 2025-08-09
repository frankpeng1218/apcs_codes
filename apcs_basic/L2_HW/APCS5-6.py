#start

N = int(input())  # 讀取使用者輸入的整數 N

factorial = 1  # 初始化階乘變數 factorial 為 1

# 迴圈從 1 到 N，計算 N 的階乘
for i in range(1, N + 1):
    factorial = factorial * i  # 將當前數字 i 乘入 factorial
    
print(factorial)  # 輸出 N 的階乘結果
