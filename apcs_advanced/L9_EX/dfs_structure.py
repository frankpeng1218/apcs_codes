# 所有 node 數量
N = 6  

# 紀錄是否拜訪過
visit = [False for _ in range(N)]

# 圖的鄰接表（無向圖）
G = [
    [1, 2],      # 0 和 1、2 相連
    [0, 3],      # 1 和 0、3 相連
    [0],         # 2 和 0 相連
    [1, 4, 5],   # 3 和 1、4、5 相連
    [3],         # 4 和 3 相連
    [3]          # 5 和 3 相連
]

def DFS(s):
    visit[s] = True
    print(f"Visit node {s}")

    for v in G[s]:
        if visit[v] == False:
            parent = s
            DFS(v)

# 從節點 0 開始 DFS
DFS(0)
