#start

x = 1  # 初始化變數 x

# 迴圈控制行數，從 1 到 5
for i in range(1, 5 + 1):
    if i % 2 == 0:  # 若 i 為偶數，則初始值設為 0
        x = 0
    else:  # 若 i 為奇數，則初始值設為 1
        x = 1

    # 內層迴圈控制每行的輸出
    for j in range(i):
        x = 1 - x  # 切換 0 和 1
        print(x, end='')  # 連續輸出數字，不換行
    print()  # 換行，進入下一列
