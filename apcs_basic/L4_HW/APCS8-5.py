import sys  # 匯入 sys 模組，用於讀取標準輸入

# 定義加法函式
def add(a, b):
    c = a + b  # 兩數相加
    return c  # 回傳結果

# 定義減法函式
def sub(a, b):
    c = a - b  # 兩數相減
    return c  # 回傳結果

# 定義乘法函式
def mul(a, b):
    c = a * b  # 兩數相乘
    return c  # 回傳結果

# 定義除法函式
def div(a, b):
    if b == 0:  # 除數為 0 時，輸出 "N/A"
        print("N/A")
        return 0
    else:
        c = a / b  # 兩數相除
        return c  # 回傳結果

#start
for s in sys.stdin:  # 逐行讀取標準輸入
    s = s.split()  # 分割輸入字串
    x = int(s[0])  # 轉換第一個數字
    op = s[1]  # 取得運算符號
    y = int(s[2])  # 轉換第二個數字

    if op == "+":  # 加法運算
        print(add(x, y))
        
    elif op == "-":  # 減法運算
        print(sub(x, y))
        
    elif op == "*":  # 乘法運算
        print(mul(x, y))

    elif op == "/":  # 除法運算
        r = div(x, y)
        if r != 0:  # 只有在結果不為 0 時才輸出
            print(r)
