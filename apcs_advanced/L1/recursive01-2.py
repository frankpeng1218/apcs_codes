a = int(input())  # 讀取使用者輸入的整數 a

r = 0  # 初始化變數 r，存儲計算結果
while a > 1:  # 當 a 大於 1 時，執行迴圈
    r = r + 2  # 每次迴圈將 r 增加 2
    a = a - 1  # 將 a 減少 1，逐步逼近終止條件

print(r + 2)  # 最後輸出 r + 2，對應 g(a) 的結果
