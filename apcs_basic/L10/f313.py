# f313. 2. 人口遷移

# 定義四個方向的變化量：上、右、下、左
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 讀取輸入：r 行數、c 列數、k 遷移的比例基準、m 模擬的天數
r, c, k, m = map(int, input().split())

# 讀取城市地圖，city[i][j] 表示 (i, j) 城市的人口或是 -1 表示無法居住
city = []
for _ in range(r):
    line = list(map(int, input().split()))
    city.append(line)

# 模擬 m 天的人口遷移
for _ in range(m):
    # 建立與 city 同樣大小的遷移人口紀錄陣列，初始為 0
    move = [[0] * c for _ in range(r)]

    # 遍歷每個城市
    for i in range(r):
        for j in range(c):
            if city[i][j] > 0:  # 是可居住城市，且有人口
                move_out = city[i][j] // k  # 計算每個方向要遷出的人口數
                direction = 0  # 計算有效的鄰近城市數

                # 遍歷四個方向
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < r and 0 <= nj < c and city[ni][nj] != -1:
                        move[ni][nj] += move_out  # 加到對應鄰近城市的 move
                        direction += 1  # 累計有效鄰居的數量

                # 原城市減去所有遷出的人口
                city[i][j] -= move_out * direction

    # 根據 move 陣列更新每個城市的新人口
    for i in range(r):
        for j in range(c):
            city[i][j] += move[i][j]

# 計算最小與最大人口（排除 -1 的不可居住地區）
max_population = 0
min_population = 100000

for i in range(r):
    for j in range(c):
        if city[i][j] != -1:
            max_population = max(max_population, city[i][j])
            min_population = min(min_population, city[i][j])

# 輸出最小與最大人口
print(min_population)
print(max_population)
