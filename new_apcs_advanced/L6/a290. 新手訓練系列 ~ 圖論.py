import sys

# 透過 sys.stdin 讀取輸入資料
for s in sys.stdin:
    # 讀取 N（城市數量）與 M（道路數量）
    N, M = map(int, s.split())

    # 建立鄰接表來儲存有向圖
    G = [ [] for i in range(N+1) ]  # 範圍 N+1，因為城市編號從 1 到 N

    # 讀取 M 條有向道路
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())  # 透過 readline 讀取並解析
        G[u].append(v)  # 在城市 u 的鄰接表中加入 v，表示可以從 u 到 v

    # 讀取起點 A 與終點 B
    A, B = map(int, sys.stdin.readline().split())

    # 使用 BFS 來檢查是否可以從 A 到達 B
    Q = [A]  # BFS 佇列，從 A 城市開始
    visit = [0 for i in range(N+1)]  # 記錄是否訪問過該城市

    # 進行 BFS
    while len(Q) > 0:
        now = Q.pop(0)  # 取出佇列最前面的城市
        visit[now] = 1  # 標記該城市為已訪問

        # 拓展 BFS，檢查從 now 出發的所有鄰接城市
        for next_city in G[now]:
            if visit[next_city] == 0:  # 若該城市尚未訪問
                visit[next_city] = 1  # 標記已訪問
                Q.append(next_city)  # 加入佇列，繼續搜索

    # 判斷是否能從 A 到達 B
    if visit[B] == 1:
        print("Yes!!!")  # 可以到達
    else:
        print("No!!!")  # 無法到達
