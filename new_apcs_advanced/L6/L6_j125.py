#
# j125: 蓋步道
#

n = int(input())
a = [[0] * 305 for _ in range(305)]
inf = int(1e9)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 讀取地圖資料
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# 設定邊界為 inf（不可通行）
for i in range(0, n + 2):
    a[0][i] = inf
    a[n + 1][i] = inf
    a[i][0] = inf
    a[i][n + 1] = inf

def check(lim):
    dis = [[-1] * 305 for _ in range(305)]
    dis[1][1] = 0
    q = [(1, 1)]
    
    while q:
        nowx, nowy = q.pop(0)  # 彈出 queue 的前端元素
        for dx, dy in directions:
            nxtx, nxty = nowx + dx, nowy + dy
            if dis[nxtx][nxty] != -1:
                continue
            if abs(a[nowx][nowy] - a[nxtx][nxty]) <= lim:
                dis[nxtx][nxty] = dis[nowx][nowy] + 1
                q.append((nxtx, nxty))
    
    return dis[n][n]

# 二分搜尋最佳解
l, r = -1, 1000000
ans = -1
while r - l > 1:
    mid = (l + r) // 2
    tmp = check(mid)
    if tmp == -1:
        l = mid
    else:
        r = mid
        ans = tmp

print(r)
print(ans)
