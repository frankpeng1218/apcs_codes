# 初始化一個 100x100 的陣列，所有元素設為 -1（方便辨識未初始化區域）
arr = []
for x in range(100):
    arr.append([-1 for i in range(100)])

# 顯示 N x N 的矩陣
def show(n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()

# 主程式：持續讀入使用者輸入
while True:
    try:
        # 讀取 N 與 M
        N = int(input())  # 矩陣大小
        M = int(input())  # 填入模式

        # 初始化 N x N 的矩陣為 0
        for i in range(N):
            for j in range(N):
                arr[i][j] = 0

        if M == 1:
            # 模式 1：順時針螺旋填入數字
            r_index = 0
            c_index = 0
            num = 1
            direction = 1
            # 1: 向右，2: 向下，3: 向左，4: 向上

            while num <= N * N:
                if direction == 1:  # 向右
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        c_index += 1

                        if c_index >= N or arr[r_index][c_index] > 0:
                            c_index -= 1
                            r_index += 1
                            direction = 2
                    else:
                        direction = 2

                elif direction == 2:  # 向下
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        r_index += 1

                        if r_index >= N or arr[r_index][c_index] > 0:
                            r_index -= 1
                            c_index -= 1
                            direction = 3
                    else:
                        direction = 3

                elif direction == 3:  # 向左
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        c_index -= 1

                        if c_index < 0 or arr[r_index][c_index] > 0:
                            c_index += 1
                            r_index -= 1
                            direction = 4
                    else:
                        direction = 4

                elif direction == 4:  # 向上
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        r_index -= 1

                        if r_index < 0 or arr[r_index][c_index] > 0:
                            r_index += 1
                            c_index += 1
                            direction = 1
                    else:
                        direction = 1

        else:
            # 模式 2：反時針螺旋填入數字
            r_index = 0
            c_index = 0
            num = 1
            direction = 1
            # 1: 向下，2: 向右，3: 向上，4: 向左

            while num <= N * N:
                if direction == 1:  # 向下
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        r_index += 1

                        if r_index >= N or arr[r_index][c_index] > 0:
                            r_index -= 1
                            c_index += 1
                            direction = 2
                    else:
                        direction = 2

                elif direction == 2:  # 向右
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        c_index += 1

                        if c_index >= N or arr[r_index][c_index] > 0:
                            c_index -= 1
                            r_index -= 1
                            direction = 3
                    else:
                        direction = 3

                elif direction == 3:  # 向上
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        r_index -= 1

                        if r_index < 0 or arr[r_index][c_index] > 0:
                            r_index += 1
                            c_index -= 1
                            direction = 4
                    else:
                        direction = 4

                elif direction == 4:  # 向左
                    if arr[r_index][c_index] == 0:
                        arr[r_index][c_index] = num
                        num += 1
                        c_index -= 1

                        if c_index < 0 or arr[r_index][c_index] > 0:
                            c_index += 1
                            r_index += 1
                            direction = 1
                    else:
                        direction = 1

        # 顯示結果矩陣
        show(N)

    except:
        # 若遇到輸入錯誤或 EOF，則結束程式
        break
