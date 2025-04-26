# d378. 最小路徑
case = 1  # 用於標記測試案例編號

while True:
    try:
        # 讀取 N（行數）和 M（列數）
        N, M = map(int, input().split())

        # 讀取地圖數據並存入 grid
        grid = []
        for i in range(N):
            row = list(map(int, input().split()))  # 讀取每一行的數字
            grid.append(row)

        # 建立 DP 陣列：route[i][j] 表示到達 (i, j) 的最小體力消耗
        route = [[0 for j in range(M)] for i in range(N)]

        # 初始化起點 (0,0)
        route[0][0] = grid[0][0]

        # 邊界初始化（第一列）：只能從左邊來
        for j in range(1, M):
            route[0][j] = route[0][j-1] + grid[0][j]

        # 邊界初始化（第一行）：只能從上面來
        for i in range(1, N):
            route[i][0] = route[i-1][0] + grid[i][0]

        # 動態規劃填表
        for i in range(1, N):          # 每一行
            for j in range(1, M):      # 每一列
                # 從上面或左邊來的最小值，加上目前格子的值
                route[i][j] = min(route[i-1][j], route[i][j-1]) + grid[i][j]

        # 輸出結果
        print(f"Case #{case} :\n{route[N-1][M-1]}")
        case += 1  # 測試案例編號遞增
        
    except:
        break  # 輸入結束時跳出迴圈
