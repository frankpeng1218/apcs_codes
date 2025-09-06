# 講義寫法
while True:
    try:
        # start
        s = input()
        data = s.split()
        R = int(data[0])
        C = int(data[1])
        M = int(data[2])

        matrix = []

        for i in range(R):
            s = input()
            Ci = [int(x) for x in s.split()]
            matrix.append(Ci)

        data = input()
        op = list(map(int, data.split()))

        print(R, C, M)
        print(matrix)
        print(op)

    except:
        break




# 持續執行直到發生例外（例如輸入結束）

while True:
    try:
        # 讀取輸入的三個整數：R 行數，C 列數，M 操作次數
        R, C, M = map(int, input().split())

        # 讀取 R 行的矩陣數據
        matrix = []
        for i in range(R):
            matrix.append([int(x) for x in input().split()])

        # 讀取操作序列並反轉（因為操作需從後往前執行）
        operates = [int(x) for x in input().split()]
        operates.reverse()

        # 根據操作執行對矩陣的變換
        for i in operates:
            if i == 0:
                matrix = rotate_minus_90(matrix)  # 逆時針旋轉 90 度
            elif i == 1:
                matrix = flip(matrix)  # 上下翻轉

        # 輸出最終矩陣的尺寸
        print(len(matrix), len(matrix[0]))

        # 輸出最終矩陣內容，每行用空格分隔
        for row in matrix:
            print(*row, sep=' ')
    except:
        break

# b965
# 上下翻轉函式
def flip(matrix):
    new_matrix = []
    # 從最後一行往第一行反向加入新矩陣中
    for i in range(len(matrix) - 1, -1, -1):
        new_matrix.append(matrix[i])
    return new_matrix

# 逆時針旋轉 90 度的函式
def rotate_minus_90(matrix):
    # 建立新矩陣
    new_matrix = []

    # 原矩陣的列數與行數
    row = len(matrix)
    col = len(matrix[0])

    # 建立旋轉後的新矩陣（行列交換）
    for i in range(col):  # 新的列數
        temp_combine = []
        for j in range(row):  # 新的行數
            temp_combine.append(matrix[j][i])  # 將元素按列取出
        new_matrix.append(temp_combine)

    # 對轉置後的矩陣做上下翻轉，達成逆時針旋轉 90 度
    new_matrix = flip(new_matrix)
    return new_matrix
