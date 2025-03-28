import sys  # 匯入 sys 模組，用於讀取標準輸入

# 定義加法函式
def add(op, a, b):
    if op == "1":  # 若操作碼為 "1"，則執行數值相加
        c = int(a) + int(b)
        
    elif op == "2":  # 若操作碼為 "2"，則執行字串相加
        c = str(a) + str(b)

    return c  # 回傳計算結果


#start
for s in sys.stdin:  # 逐行讀取標準輸入
    data = s.split()  # 將輸入字串分割成列表

    r = add(data[0], data[1], data[2])  # 呼叫 add 函式

    print(r)  # 輸出結果
