#
# DFS 範例寫法（Depth First Search）
# 功能：從起點 S 開始，使用深度優先搜尋走訪圖中所有可到達的節點
#

def DFS(s):
    # 將目前節點 s 標記為已拜訪
    visit[s] = True

    # 走訪所有與節點 s 相鄰的節點
    for next_node in G[s]:
        # 若相鄰節點 next_node 尚未被拜訪
        if not visit[next_node]:
            # 將節點 next_node 記錄到走訪順序結果中
            R.append(v)
            # 以 next_node 為起點繼續進行 DFS（一路往深處走）
            DFS(next_node)

# ---------- start ----------

# 讀取節點數量（節點編號為 0 ~ N-1）
N = int(input())

# 讀取邊的數量
M = int(input())

# visit 陣列：紀錄每個節點是否已被拜訪
# False 表示尚未拜訪，True 表示已拜訪
visit = [False for _ in range(N)]

# 建立鄰接表（Adjacency List）來表示圖
# G[i] 存放與節點 i 相鄰的所有節點
G = [[] for _ in range(N)]

# 讀取 M 條邊並建立無向圖
for _ in range(M):
    # u, v 為一條邊所連接的兩個節點
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)   # 無向圖需雙向加入

# 讀取 DFS 的起始節點
S = int(input())

# R 用來紀錄 DFS 的走訪順序
# 先將起點加入結果中
R = [S]

# 從起點 S 開始進行深度優先搜尋
DFS(S)

# 輸出 DFS 走訪的節點順序
print(*R)


# input
# 4
# 3
# 0 1
# 0 2
# 1 3
# 0

# logic: 0 → 1 → 3 → 回來 → 2
# output: 0 1 3 2