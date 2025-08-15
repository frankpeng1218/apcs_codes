import sys  # 匯入 sys 模組，用於讀取標準輸入

# 定義數值相加函式
def addvalue(a, b):
    c = int(a) + int(b)  # 轉換為整數後相加
    return c  # 回傳相加結果

# 定義字串相加函式
def addstring(a, b):
    c = str(a) + str(b)  # 轉換為字串後串接
    return c  # 回傳串接結果

#start
for s in sys.stdin:  # 逐行讀取標準輸入
    data = s.split()  # 將輸入字串分割成列表

    if data[0] == "1":  # 若第一個值為 "1"，則執行數值相加
        r = addvalue(data[1], data[2])

    elif data[0] == "2":  # 若第一個值為 "2"，則執行字串相加
        r = addstring(data[1], data[2])

    print(r)  # 輸出結果
