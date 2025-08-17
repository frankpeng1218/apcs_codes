# (-1, -1) (-1, 0) (-1, 1)
# ( 0, -1) ( 0, 0) ( 0, 1)
# ( 1, -1) ( 1, 0) ( 1, 1)

# 定義方向陣列，用於遍歷周圍的八個方向
dx = [1, -1, 0, 0, -1, 1, -1, 1]  # x 方向 (上下左右與對角線)
dy = [0, 0, 1, -1, 1, 1, -1, -1]  # y 方向 (上下左右與對角線)

TC = 1  # 測試案例編號 (Field #1, Field #2, ...)

while True:  # 無限迴圈，持續處理測試案例，直到輸入結束
    try:
        # 讀取輸入，獲取矩陣的行數 (n) 和列數 (m)
        s = input()
        n, m = map(int, s.split())  # 解析 n (行數) 和 m (列數)

        # 如果 n 和 m 都為 0，則輸入結束，跳出迴圈
        if n == 0 and m == 0:
            break

        # 讀取地圖資訊，存入 field
        field = []
        for i in range(n):  # 讀取 n 行
            s = input()  # 讀取一行字串
            field.append(list(s))  # 轉換為字元列表並存入 field

        # 初始化結果矩陣 result，預設值為 0
        result = [[0 for j in range(m)] for i in range(n)]

        # 遍歷地圖中的每個位置
        for i in range(n):
            for j in range(m):
                if field[i][j] == '*':  # 如果當前位置是地雷
                    result[i][j] = -1  # 在結果矩陣中標記為 -1
                else:
                    # 檢查周圍 8 個方向
                    for k in range(8):  # 遍歷 dx, dy 陣列
                        x = i + dx[k]  # 計算新 x 座標
                        y = j + dy[k]  # 計算新 y 座標
                        # 確保不越界，且鄰近位置有地雷
                        if 0 <= x < n and 0 <= y < m and field[x][y] == "*":
                            result[i][j] += 1  # 計算鄰近地雷數量

        # 如果不是第一個測試案例，輸出空行以分隔
        if TC > 1:
            print()
        print(f"Field #{TC}:")
        # print("Field #" + str(TC) + ":")

        TC += 1  # 測試案例編號遞增

        # 輸出結果矩陣
        for i in range(n):
            for j in range(m):
                if result[i][j] == -1:  # 地雷位置輸出 '*'
                    print("*", end='')
                else:  # 其他位置輸出地雷數量
                    print(result[i][j], end='')
            print()  # 換行

    except:
        break  # 捕捉輸入錯誤或例外情況，結束程式
