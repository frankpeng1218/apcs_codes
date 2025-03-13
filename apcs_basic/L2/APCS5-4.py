#start

N = int(input())  # 讀取使用者輸入的整數 N

i = 1  # 初始化變數 i 為 1

while i <= N:  # 當 i 小於或等於 N 時，執行迴圈
    if N % i == 0:  # 若 N 能被 i 整除，則 i 為 N 的因數
        print(i, end=' ')  # 輸出 i，並以空格分隔

    i = i + 1  # i 增加 1，準備下一次迴圈
