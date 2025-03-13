import sys

#start
for s in sys.stdin:  # 透過 sys.stdin 逐行讀取輸入（適用於批量輸入或檔案重定向）
    date = s.split()  # 使用 split() 以空格拆分輸入，轉換為串列
    number = (int(date[0]) + int(date[1])) % 10  # 計算兩數相加後取 10 的餘數
    print(number)  # 輸出結果
