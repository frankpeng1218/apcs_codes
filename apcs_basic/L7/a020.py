import sys  # 匯入 sys 模組，用於讀取標準輸入（stdin）

# 定義將字母轉換為對應的數字代碼的函式
def translateCode(ch):
    # 定義字母到數字的對應字典
    CODE = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34,
            'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'O':35, 'P':23, 'Q':24, 'R':25,
            'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33}
    
    # 返回對應字母的數字代碼
    return CODE[ch]

#start

# 使用 sys.stdin 逐行讀取輸入
for s in sys.stdin:
    # 將每行的字串轉換為字元列表
    testID = list(s)

    # 取得首字母對應的區域碼
    areaCode = translateCode(testID[0])

    # 計算 x1 和 x2
    x1 = int(areaCode / 10)  # 取區域碼的十位數
    x2 = (areaCode % 10) * 9  # 取區域碼的個位數，並乘以9

    # 初始化 x_3_10，計算位於第3到第10位的數字的加權和
    x_3_10 = 0
    for i in range(1, 8 + 1):  # 從第2個字元（index 1）到第9個字元（index 8）
        x_3_10 += (int(testID[i])) * (9 - i)  # 乘以加權係數 9-i

    # 取得第10位數字
    x9 = int(testID[9])

    # 計算驗證碼，並檢查是否為 0
    verify_code = (x1 + x2 + x_3_10 + x9) % 10

    # 如果驗證碼為 0，則判斷為 "real"，否則為 "fake"
    if verify_code == 0:
        print("real")
    else:
        print("fake")
