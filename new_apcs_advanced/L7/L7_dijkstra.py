#
# Dijkstra 最短路徑演算法（Dijkstra's Algorithm）實作
# 適用情境：單源最短路徑（Single-Source Shortest Path），且圖中「不可包含負權重邊」
# 資料結構：鄰接矩陣（Adjacency Matrix）
# 時間複雜度：O(V^2)，V 為頂點數量
#

def dijkstra_path(graph, start):
    """
    計算起點 start 到圖中所有節點的最短路徑距離
    :param graph: 2D List (鄰接矩陣)，graph[u][v] 代表節點 u 到 v 的權重，0 代表無直接相連
    :param start: 起點節點編號 (0-indexed)
    :return: dist 串列，dist[i] 代表從起點到節點 i 的最短距離
    """
    n = len(graph)
    INF = float('inf')        # 以無限大代表目前無法到達或尚未探索
    dist = [INF] * n          # 記錄起點到各節點當前的已知最短距離
    visited = [False] * n     # 記錄節點是否已確定最短距離（已造訪/已收斂）

    # 起點到自身的距離初始化為 0
    dist[start] = 0

    # 圖中有 n 個節點，理論上最多需進行 n 次「挑選與鬆弛」的過程
    for _ in range(n):
        # 步驟 1：貪婪策略（Greedy Choice）
        # 從「尚未確定最短距離（not visited）」的節點中，挑選目前距離起點最小的節點 u
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        # 若找不到可拜訪的節點（剩餘節點距離皆為 INF，代表不連通），提前結束
        if u == -1:
            break

        # 步驟 2：標記節點 u 為已確定（在此步後，dist[u] 不會再被更新）
        visited[u] = True

        # 步驟 3：鬆弛操作（Relaxation）
        # 嘗試透過節點 u 作為中繼點，更新與 u 相鄰且尚未確定的節點 v 之最短路徑
        for v in range(n):
            # 條件：u 與 v 有相連邊（!= 0）且節點 v 尚未確定最短距離
            if graph[u][v] != 0 and not visited[v]:
                # 三角不等式：若經過 u 到達 v 比較短，則更新 dist[v]
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist


# --- 測試資料說明 ---
# 節點數 7（A~G 對應 0~6），邊數 12
# 輸入格式：每行包含 x y c（x 與 y 之間有一條權重為 c 的無向邊）
'''
7 12
0 2 3
0 5 2
1 3 1
1 4 2
1 5 6
1 6 2
2 3 4
2 4 1
2 5 2
3 6 2
4 5 3
5 6 5
'''

# --- 主程式 ---

# 設定起點為節點 0（對應節點 A）
start = 0

# 輸入節點數 N 與邊數 K
N, K = map(int, input().split())

# 建立 N x N 的鄰接矩陣，初始權重皆為 0（代表未相連）
graph = [[0 for _ in range(N)] for _ in range(N)]

# 讀入 K 條邊並建構「無向圖」（雙向權重相同）
for _ in range(K):
    x, y, c = map(int, input().split())
    graph[x][y] = c
    graph[y][x] = c

# 執行 Dijkstra 演算法獲取起點到各點的最短距離
distances = dijkstra_path(graph, start)

# 將節點編號對應至可讀性高的英文字母
city_map = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 格式化輸出各節點的最短距離
for i, d in enumerate(distances):
    print(f"從 A 到 {city_map[i]} 的最短距離：{d}")