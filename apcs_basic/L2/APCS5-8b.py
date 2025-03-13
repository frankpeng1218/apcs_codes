#start

# 外層迴圈控制行數，從 0 到 5（共 6 行）
for i in range(5 + 1):
    # 內層迴圈控制每行的星號數量
    for j in range(1, i + 1):
        print("*", end='')  # 連續輸出星號，不換行
    print()  # 換行，進入下一列
