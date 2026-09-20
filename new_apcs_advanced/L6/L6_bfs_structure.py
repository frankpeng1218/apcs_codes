#
# BFS 範例寫法（Breadth First Search）
# 功能：從起點 S 開始，使用廣度優先搜尋，
#       依照「一層一層」的順序走訪圖中的節點
#

# ---------- start ----------

# 讀取節點數量（節點編號假設為 1 ~ N）
N = int(input())

# 建立鄰接表（Adjacency List）
# G[i] 用來存放與節點 i 相鄰的所有節點
# 使用 N+1 是為了不使用索引 0，方便對應節點編號
G = [[] for i in range(N + 1)]

# 讀取邊的資料並建立圖
for _ in range(N):
    # u, v 為具有關係的兩個節點（有向圖）
    u, v = map(int, input().split())
    G[u].append(v)

# 設定 BFS 起點
S = int(input())

# R 作為 queue（佇列），用來存放待走訪的節點
R = [S]

# visit 陣列：紀錄節點是否已被拜訪
# 0 表示尚未拜訪，1 表示已拜訪
visit = [0 for i in range(N + 1)]

# ---------- BFS 開始 ----------
while len(R) > 0:
    # 從 queue 的前端取出一個節點
    now = R.pop(0)

    # 將目前節點標記為已拜訪
    visit[now] = 1

    # 走訪目前節點 now 的所有相鄰節點
    for next_node in G[now]:
        # 若相鄰節點尚未拜訪
        if visit[next_node] == 0:
            # 標記為已拜訪並加入 queue
            visit[next_node] = 1
            R.append(next_node)

# 顯示每個節點是否被拜訪過
print(visit)


# input
# 4
# 1 2
# 1 3
# 2 4
# 3 4
# 1

# output
# [0, 1, 1, 1, 1]
