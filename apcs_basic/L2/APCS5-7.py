#start

# 迴圈從 1 到 9，建立九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:  # 若乘積小於 10，為了對齊輸出，在等號後加一個空格
            print(str(i) + "x" + str(j) + "= " + str(i * j), end=' ')
        else:
            print(str(i) + "x" + str(j) + "=" + str(i * j), end=' ')
    print()  # 換行，進入下一列輸出
