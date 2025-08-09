import sys  # 匯入 sys 模組以讀取標準輸入 (stdin)

#start
for s in sys.stdin:  # 迴圈讀取標準輸入的每一行
    data = s.split()  # 將輸入的字串以空白分割成列表
    number = int(data[0]) + int(data[1])  # 取出列表中的兩個數字，轉換為整數後相加
    print(number)  # 輸出相加的結果
