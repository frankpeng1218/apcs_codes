#start

i = 0  # 初始化變數 i

while i < 100:  # 當 i 小於 100 時持續執行迴圈
    i = i + 1  # 每次迴圈 i 增加 1
    if i % 10 == 0:  # 如果 i 是 10 的倍數
        break  # 跳出迴圈

print(i)  # 輸出跳出迴圈時的 i 值
