# d406. 倒水時間

##BFS (廣度優先搜尋, Breadth-First Search) 
##1. 從起點開始，依序訪問與當前節點相鄰的節點。
##2. 使用佇列 (Queue) 來管理要擴展的節點，確保最先訪問的節點先被處理。
##3. 層層擴展，確保最短距離。

case= 1 # 代表第幾次

while True:
    try:
        S = int(input()) # S=2不可上流, S=1 可上流
        N, M = map(int, input().split()) # N(row), M(column)

        # 讀取水管地圖
        MAP = []
        for i in range(N):
            row = list(map(int, input().split())) # 0 表示無水管, 1表示有水管
            MAP.append(row)

        # 初始化標記的矩陣(紀錄水流到達每個點的時間)
        marked = [[0 for _ in range(M)] for _ in range(N)]
        
        # 設定初始點(水從最上方開始流)
        r, c = 0, 0

        # 找到最上方(第一個row)的第一個水管
        while MAP[r][c] == 0:
            c += 1 # 移動到下一個水管

        # BFS 初始化
        Q = [[r, c]] # 定義第一個擴展點
        marked[r][c] = 1 # 標記第一個時間點

        # BFS 開始遊歷
        while len(Q) > 0:
            now = Q.pop(0) # 取出queue的第一個點
            r, c = now[0], now[1]

            # 移動方向(左, 下, 右, 上)
            # 左移動(c-1)
            if c - 1 >= 0: # 不要超過邊界
                if MAP[r][c-1] == 1 and marked[r][c - 1] == 0: # 確保水管沒標記(沒有被走過)
                    marked[r][c-1] = marked[r][c] + 1 #紀錄水管到達的時間
                    Q.append([r, c-1])

            # 下移動(r+1)
            if r + 1 <N:
                if MAP[r+1][c] == 1 and marked[r+1][c] == 0:
                    marked[r+1][c] = marked[r][c] + 1
                    Q.append([r+1, c])

            # 右移動(c+1)
            if c + 1 < M: # 不要超過邊界
                if MAP[r][c+1] == 1 and marked[r][c+1] == 0: # 確保水管沒標記(沒有被走過)
                    marked[r][c+1] = marked[r][c] + 1 #紀錄水管到達的時間
                    Q.append([r, c+1])

            # 上移動(r-1) (只有S=1時可以上流)
            if r-1 >=0 and S == 1:
                if MAP[r-1][c] == 1 and marked[r-1][c] == 0:
                    marked[r-1][c] = marked[r][c] + 1
                    Q.append([r-1, c])

        # output
        print(f"Case {case}:")
        for i in range(N):
            for j in range(M):
                print(marked[i][j], end=" ")
            print()

        case += 1
    except:
        break
























    
