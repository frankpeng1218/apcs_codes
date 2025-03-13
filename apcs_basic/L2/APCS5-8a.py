#start

M = int(input())  # 讀取使用者輸入的整數 M，代表列數
N = int(input())  # 讀取使用者輸入的整數 N，代表行數

# 迴圈控制行數
for i in range(N):
    # 迴圈控制列數，每行輸出 M 個星號
    for j in range(M):
        print("*", end='')  # 不換行輸出星號
    print()  # 換行，進入下一列
