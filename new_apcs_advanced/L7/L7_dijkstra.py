#
# Dijkstra's Algorthm 實作
#

def dijkstra_path(graph, start):
    n = len(graph)
    INF = float('inf') # 相當於 9999999 = 無限大 
    dist = [INF] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        # 選出還沒訪問過、目前距離最小的點
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break  # 沒有可訪問的節點

        visited[u] = True

        # 更新與 u 相鄰的所有節點的距離
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist

# start

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

'''
graph = [
    # A  B  C  D  E  F  G
    [ 0, 0, 3, 0, 0, 2, 0],  # A
    [ 0, 0, 0, 1, 2, 6, 2],  # B
    [ 3, 0, 0, 4, 1, 2, 0],  # C
    [ 0, 1, 4, 0, 0, 0, 2],  # D
    [ 0, 2, 1, 0, 0, 3, 0],  # E
    [ 2, 6, 2, 0, 3, 0, 5],  # F
    [ 0, 2, 0, 0, 0, 5, 0]   # G
]
'''

# start
start = 0  # A
N, K = map(int, input().split())
graph = [ [0 for j in range(N)] for i in range(N) ]

for _ in range(K):
    x, y, c = map(int, input().split())
    graph[x][y] = c
    graph[y][x] = c
    
distances = dijkstra_path(graph, start)

city_map = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for i, d in enumerate(distances):
    print(f"從 A 到 {city_map[i]} 的最短距離：{d}")

