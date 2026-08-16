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


visit = []

# 遞迴函式
def walk(x, y):
    
    return 

# start
found = walk()

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
print()
