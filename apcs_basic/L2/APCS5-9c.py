#start

# 外層迴圈控制行數 (i 表示行索引)
for i in range(5):
    # 內層迴圈控制列數 (j 表示列索引)
    for j in range(5):
        if i == j:  # 如果行索引等於列索引，則輸出 0
            print(0, end='')
        else:  # 否則輸出當前行數的值 (i+1)
            print(i + 1, end='')
    print()  # 換行，進入下一列
