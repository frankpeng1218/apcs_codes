# k205. 蝸牛的踩地雷攻略 1 (插旗)
# 二維陣列, 方向向量, 邊界檢查

# 八個方向（上→右上→右→右下→下→左下→左→左上）
# 用來掃描某一格周圍的 8 個鄰居
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
# 讀取棋盤大小
n, m = map(int, input().split()) # 9 9
# 讀取棋盤內容
board = []
for _ in range(n):
    row = list(input())
    board.append(row)

# 開始掃描整個棋盤
for r in range(n):
    for c in range(m):
        # 如果不是數字1~8就代表不用處理
        if board[r][c] not in "12345678":
            continue
        # 這格數字：代表周圍應該有多少地雷
        need = int(board[r][c])# 需要的地雷數字
        # 紀錄周圍旗子(P)數量, 以及未知(#)格子的座標
        flags = 0
        unknowns = []
        # 掃描八個方向
        for k in range(8):
            nr = r + dr[k] # 新的row
            nc = c + dc[k] # 新的column
            #超出棋盤就跳過
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            cell = board[nr][nc]

            # 若是旗子(P), 已經確定是地雷了
            if cell == "P":
                flags += 1
            elif cell == "#":
                unknowns.append((nr, nc))
        # 規則：
        # 周圍旗子數+周圍未知數=炸彈數
        # 則所有未知(#)一定都是地雷, 全部都可以插旗
        # 如果不相等：無法確定：不能插旗
        if flags + len(unknowns) != need:
            continue

        # 插旗
        for (nr, nc) in unknowns:
            board[nr][nc] = "P"
for row in board:
    print("".join(row))









            
        
