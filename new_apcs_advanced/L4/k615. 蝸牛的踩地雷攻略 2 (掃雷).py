# k615 蝸牛的踩地雷攻略2 (掃雷)
# 可參考k205. 蝸牛的踩地雷攻略 1 (插旗)
# 二維陣列, 方向向量, 邊界檢查

# 八個方向：上、右上、右、右下、下、左下、左、左上
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 讀取n, m
n, m = map(int, input().split())

# 讀取棋盤
board = []
for _ in range(n):
    row = list(input())
    board.append(row)

# 掃描全棋盤
for r in range(n):
    for c in range(m):
        # 只處理1~8
        if board[r][c] not in "12345678":
            continue
        need = int(board[r][c]) # 地雷數量
        flags = 0 # 周圍旗子數量
        unknowns = 0 # 周圍 # 的數量

        # 掃描周圍8個方向
        for k in range(8):
            nr = r + dr[k] # new row
            nc = c + dc[k] # new column
            # 邊界檢查
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            cell = board[nr][nc]
            if cell == "P":
                flags += 1
            elif cell == "#":
                unknowns += 1

        # 如果旗子數 == 地雷數(need): 可掃雷
        if flags == need and unknowns > 0:
            board[r][c] = "O"

for row in board:
    print("".join(row))




                
