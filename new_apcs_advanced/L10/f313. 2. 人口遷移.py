# f313. 2. 人口遷移

#定義變化量
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#定義輸入的變數
r, c, k, m = map(int, input().split())

city = []
for _ in range(r):
    line = list(map(int, input().split()))
    city.append(line)


#模擬每一天
for _ in range(m):
    move = [[0] * c for _ in range(r)]
    print(move)
    for i in range(r):
        for j in range(c):
            if city[i][j]>0: # 有效的城市
                move_out = city[i][j] // k # 遷移人口數
                direction = 0 # 有效的相鄰城市數量
                for d in range(4): #遊歷左下右上
                    ni, nj = i+dx[d], j + dy[d]
                    if 0<= ni < r and 0 <= nj < c and city[ni][nj] != -1:
                        move[ni][nj] = move[ni][nj] + move_out
                        direction = direction + 1
                city[i][j] = city[i][j] - move_out * direction # 減掉遷移的人口

    #更新人口
    for i in range(r):
        for j in range(c):
            city[i][j] = city[i][j] + move[i][j]


# 計算最大和最小人口
max_population = 0
min_population = 100000

for i in range(r):
    for j in range(c):
        if city[i][j] != -1:
            max_population = max(max_population, city[i][j])
            min_population = min(min_population, city[i][j])

print(min_population)
print(max_population)





















    
