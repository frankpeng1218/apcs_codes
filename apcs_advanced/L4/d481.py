

while True:
    try:
        # 讀取輸入，獲取矩陣 A 和 B 的行列數
        conf = input()
        data = list(map(int, conf.split()))

        a, b, c, d = data[0], data[1], data[2], data[3]  # a: A 的行數, b: A 的列數, c: B 的行數, d: B 的列數

        # 如果 A 的列數不等於 B 的行數，則無法進行矩陣乘法，輸出錯誤訊息
        if b != c:
            print("Error")
            continue
        else:
            # 讀取矩陣 A 的元素
            A = []
            for i in range(a):
                row = input()
                row = list(map(int, row.split()))  # 將每行數據轉換為整數列表
                A.append(row)

            # 讀取矩陣 B 的元素
            B = []
            for i in range(c):
                row = input()
                row = list(map(int, row.split()))  # 將每行數據轉換為整數列表
                B.append(row)

            # 初始化結果矩陣 C，其大小為 a 行 d 列，初始值為 0
            C = []
            for i in range(a):
                row = [0 for column in range(d)]  # 每列初始化為 0
                C.append(row)

            # 矩陣乘法計算 C = A x B
            for i in range(a):  # 遍歷矩陣 C 的每一行
                for j in range(d):  # 遍歷矩陣 C 的每一列
                    for k in range(c):  # 計算 A 的行與 B 的列的內積
                        C[i][j] += A[i][k] * B[k][j]  # 將對應元素相乘後累加

            # 輸出結果矩陣 C
            for i in range(a):
                for j in range(d):
                    print(C[i][j], end=' ')  # 同一行的數字用空格分隔
                print()  # 換行輸出下一行
    except:
        break  # 捕捉例外情況（如 EOF），結束程式
