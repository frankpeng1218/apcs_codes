#start

# 迴圈控制行數，從 -4 到 4
for i in range(-4, 4 + 1):
    # 根據 i 的絕對值輸出對應數量的空格，使圖形居中
    print(abs(i) * " ", end='')

    # 內層迴圈控制每行星號的數量，計算方式為 5 - abs(i)
    for j in range(1, 5 - abs(i) + 1):
        print(" *", end='')  # 輸出星號，前面帶空格對齊
    print()  # 換行
