import sys  # 匯入 sys 模組以讀取標準輸入

#start
for s in sys.stdin:  # 逐行讀取標準輸入
    data = s.split()  # 以空格分割輸入字串
    code = data[0]  # 取得加密字串
    K = int(data[1])  # 取得位移值 K

    decode = ""  # 初始化解碼後的字串
    for i in range(len(code)):  # 遍歷字串中的每個字元
        value = ord(code[i]) + K  # 取得字元的 ASCII 值並加上 K
        decode += chr(value)  # 轉換回字元並加入解碼字串中

    print(decode)  # 輸出解碼後的結果
