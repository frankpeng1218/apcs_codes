import random

# 建立 8x8 的迷宮，邊緣全部設為牆壁 '#'
maze = [['#' for _ in range(8)] for _ in range(8)]

# 隨機填入牆壁或通道，限制在中間區域 (1~6)
for i in range(1, 7):
    for j in range(1, 7):
        maze[i][j] = '#' if random.random() < 0.3 else '.'

# 強制起點和終點為通道
maze[1][1] = '.'
maze[6][6] = '.'


visit = [[False for _ in range(8)] for _ in range(8)]

# 遞迴函式
def walk(x, y):
    if (x, y) == (6, 6):
        visit[x][y] = True
        return True

    visit[x][y] = True

    # 上
    if x > 0 and maze[x-1][y] == '.' and not visit[x-1][y]:
        if walk(x-1, y):
            return True

    # 右
    if y < 7 and maze[x][y+1] == '.' and not visit[x][y+1]:
        if walk(x, y+1):
            return True

    # 下
    if x < 7 and maze[x+1][y] == '.' and not visit[x+1][y]:
        if walk(x+1, y):
            return True

    # 左
    if y > 0 and maze[x][y-1] == '.' and not visit[x][y-1]:
        if walk(x, y-1):
            return True

    # 回溯
    visit[x][y] = False
    return False

# start
found_result = walk(1, 1)

# 印出迷宮
print("迷宮:")
for row in maze:
    print(''.join(row))

# 印出走過的路徑
print("\n走過的路徑 (O 表示路徑):")
for i in range(8):
    line = ''
    for j in range(8):
        if visit[i][j]:
            line += 'O'
        else:
            line += maze[i][j]
    print(line)

# 印出結果(是否能到終點)
print("\n結果:", "成功走到終點！" if found_result else "無法走到終點")
