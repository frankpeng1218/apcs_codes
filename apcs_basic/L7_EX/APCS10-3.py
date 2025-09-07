while True:
    try:
        # 讀取 R, C, M
        s = input()  # 範例輸入：3 2 3
        data = s.split()  # ["3", "2", "3"]
        R = int(data[0])
        C = int(data[1])
        M = int(data[2])

        # 讀取矩陣 R 行
        matrix = []
        for i in range(R):  # 例如輸入：1 1, 3 1, 1 2
            s = input()
            Ci = [int(x) for x in s.split()]
            matrix.append(Ci)

        # 讀取操作指令
        data = input()  # 例如輸入：1 0 0
        op = list(map(int, data.split()))

        # 輸出檢查
        print(R, C, M)
        print(matrix)
        print(op)

    except:
        break


# 更快的方式：
while True:
    try:
        # 讀取 R, C, M
        R, C, M = map(int, input().split())

        # 讀取矩陣 R 行
        matrix = [list(map(int, input().split())) for _ in range(R)]

        # 讀取操作指令
        op = list(map(int, input().split()))

        # 輸出檢查
        print(R, C, M)
        print(matrix)
        print(op)

    except:
        break
