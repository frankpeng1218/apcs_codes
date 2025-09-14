# 讀入節點數量 N
N = int(input())

# 初始化圖的鄰接串列 G，G[0] 不使用（節點從 1 到 N）
G = [ [] for i in range(N+1) ]

# 讀入 N 條邊的資訊，建立圖的連結關係
for s in range(N):
    u, v = map(int, input().split())  # u 有一條邊指向 v
    G[u].append(v)  # 在 u 的鄰接串列中加入 v

# 讀入起點 A 和終點 B
A, B = map(int, input().split())

# 初始化 BFS 的佇列，從起點 A 開始搜尋
R = [A]

# 初始化訪問紀錄串列，visit[i] = 1 表示節點 i 已經拜訪過
visit = [0 for i in range(N+1)]

# 開始 BFS 搜尋
while len(R) > 0:
    now = R.pop(0)      # 取出目前要處理的節點（先進先出）
    visit[now] = 1      # 標記目前節點已經拜訪過

    # 探訪所有與 now 相鄰的節點
    for next_node in G[now]:
        if visit[next_node] == 0:     # 如果還沒拜訪過
            visit[next_node] = 1      # 標記為已拜訪
            R.append(next_node)      # 加入 BFS 佇列等待處理

# 判斷是否可以從 A 走到 B
print("Yes" if visit[B] else "No")
