# e792. a3.旅行(Trip)
# 圖論（Graph）, DFS（深度優先搜尋）, 路徑存在性判斷

def dfs(start, goal, visited):
    """
    使用 DFS（Depth-First Search）判斷
    是否存在一條從 start 到 goal 的路徑
    """

    # 如果目前走到的點已經是目標點，代表找到路徑
    if start == goal:
        return True

    # 標記目前節點為已拜訪，避免重複走訪造成無限遞迴
    visited[start] = True

    # 走訪所有從 start 可以到達的鄰居節點
    for neighbor in adj[start]:
        # 如果該鄰居還沒被拜訪過
        if not visited[neighbor]:
            # 繼續從鄰居做 DFS
            if dfs(neighbor, goal, visited):
                return True  # 只要有一條路成功就回傳 True

    # 所有路都走過，仍無法到達 goal
    return False



# n：節點數
# m：邊數
# q：詢問次數
n, m, q = map(int, input().split())

# 建立鄰接串列（Adjacency List）
# adj[i] 代表從節點 i 出發可以到達的所有節點
adj = [[] for _ in range(n)]

# 讀取圖的邊（有向邊）
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)  # 從 a 可以飛到 b

# 處理每一筆詢問
for _ in range(q):
    a, b = map(int, input().split())

    # 每一個查詢都要重新建立 visited
    # visited[i] = 是否在本次 DFS 中拜訪過節點 i
    visited = [False] * n

    # 使用 DFS 檢查是否能從 a 走到 b
    if dfs(a, b, visited):
        print("YES")
    else:
        print("NO")
