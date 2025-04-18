import sys

for s in sys.stdin:  # 從標準輸入讀取每一行
    data = list(s)  # 將輸入字串轉為字元列表
    data.pop()  # 移除最後的換行字元 '\n'

    for i in range(len(data)):
        t = ord(data[i])  # 將字元轉為對應的 ASCII 數值
        print(chr(t - 7), end='')  # 將 ASCII 減去 7 後轉回字元輸出（解碼）

    print()  # 每一行結束換行
