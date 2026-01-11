#
# o712: 蒐集寶石
#

M, N, k, r, c = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

stone = 0
score = 0

dirs4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 上 右 下 左
now_dir = 1  # 初始向右

while True:
    # step1: 當前格沒有寶石就結束
    if arr[r][c] == 0:
        break

    # step2: 收集寶石
    score += arr[r][c]
    stone += 1
    arr[r][c] -= 1

    # step3: 判斷是否右轉
    if score % k == 0:
        now_dir = (now_dir + 1) % 4

    # step4: 嘗試移動（最多四個方向）
    moved = False
    for _ in range(4):
        nr = r + dirs4[now_dir][0]
        nc = c + dirs4[now_dir][1]

        # 邊界或障礙物
        if nr < 0 or nr >= M or nc < 0 or nc >= N or arr[nr][nc] == -1:
            now_dir = (now_dir + 1) % 4  # 右轉
            continue

        # 可以移動
        r, c = nr, nc
        moved = True
        break

    # 四個方向都不能走 → 結束
    if not moved:
        break

print(stone)
