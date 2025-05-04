#           (0, -1)
#             [3]
# (-1, 0)[1]  [c]  [2] (1, 0)
#             [0]
#           (0, 1)

dx = [ 0, 1,  0, -1]  # dx 與 dy 定義 BFS 四個方向：下、右、上、左（順時針）
dy = [ 1, 0, -1,  0]

#start
S = int(input())  # S 沒有被使用到，可忽略或預留未來功能
N, M = map(int, input().split())  # 地圖大小：N 行、M 列

MAP = []
for i in range(N):
    row = list(map(int, input().split()))  # 每一列的地圖資訊
    MAP.append(row)

# 建立一個同樣大小的矩陣來記錄每個位置是否走過 (0: 未拜訪)
marked = [ [0 for i in range(M)] for j in range(N) ]

#====================================================
r, c = 0, 0  # 起始位置預設從 (0, 0)
nr, nc = 0, 0  # 預備儲存下一個位置（暫時沒用到）

# 找到第一個為 1 的位置作為 BFS 起點（假設從地圖第一行開始找）
while MAP[r][c] == 0:
    c += 1

# BFS
Q = [[r, c]]  # 將起點放入隊列 (例如 (0, 3))
marked[r][c] = 1  # 標記起點為已拜訪，步數設為 1

while len(Q) > 0:
    now = Q.pop(0)  # 取出目前處理的位置
    r = now[0]
    c = now[1]

    print(r, c)  # 顯示目前處理的位置

    # 左
    if c-1 >= 0:  # 邊界判斷，避免索引錯誤
        if MAP[r][c-1] == 1 and marked[r][c-1] == 0:
            marked[r][c-1] = marked[r][c] + 1  # 記錄步數
            Q.append([r, c-1])  # 加入隊列

    # 下
    if r+1 < N:
        if MAP[r+1][c] == 1 and marked[r+1][c] == 0:
            marked[r+1][c] = marked[r][c] + 1
            Q.append([r+1, c])

    # 右
    if c+1 < M:
        if MAP[r][c+1] == 1 and marked[r][c+1] == 0:
            marked[r][c+1] = marked[r][c] + 1
            Q.append([r, c+1])

    print(Q)  # 顯示目前隊列中的位置（下一層要處理的點）

# 輸出最後標記的矩陣，顯示 BFS 拜訪順序與步數
for i in range(N):
    print(marked[i])
