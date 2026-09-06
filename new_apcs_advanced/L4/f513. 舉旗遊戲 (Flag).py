# f513. 舉旗遊戲 (Flag)
# 二維陣列, 方向向量, 邊界檢查

# 方向向量, 八方向位移（左上、上、右上、右、右下、下、左下、左）
dR = [-1, -1, -1, 0, 1, 1, 1, 0]
dC = [-1,  0,  1, 1, 1, 0,-1,-1]

# 讀取棋盤大小
rows, cols = map(int, input().split()) # 3, 4
# 讀取棋盤
# board = []
# for _ in range(rows):
#    rows_input = input().split() # 2 2 2 2/2 1 2 1/2 2 2 2
#    row = list(map(int, row_input))
#    board.append(row)

board = [list(map(int, input().split())) for _ in range(rows)]

eliminated = 0 # 被淘汰的人數
# eliminated_positions = []

for r in range(rows):
    for c in range(cols):
        me = board[r][c]
        total_neighbors = 0 # 實際存在的鄰居數
        different_neighbors = 0 # 與自己不同的鄰居數
        # 檢查8方向
        for k in range(8):
            nr, nc = r + dR[k], c + dC[k] # nr, nc: neighbor row/column
            # 邊界檢查
            if 0 <= nr < rows and 0 <= nc < cols:
                total_neighbors += 1
                if board[nr][nc] != me:
                    different_neighbors += 1
        # 若所有鄰居都和自己不同->淘汰
        # 並且避免單格棋盤(沒有鄰居的情況下)
        if total_neighbors > 0 and different_neighbors == total_neighbors:
            eliminated += 1
            # eliminated_positions.append((r,c))

print(eliminated)
# print(eliminated_positions)









            
