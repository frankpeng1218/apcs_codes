import sys
sys.setrecursionlimit(1000000)  # 設定最大遞迴深度，避免樹太深導致 RecursionError

# 定義 DFS 函式，用來從當前節點往下探索，計算每個節點的「高度」
def dfs(node):
    global height  # 使用全域變數 height 記錄每個節點的高度

    # 如果該節點沒有任何子節點，代表它是「葉節點」
    if len(G[node]) == 0:
        height[node] = 0  # 葉節點的高度定義為 0
        return 0

    else:
        mx = 0  # 初始化該節點的最大子高度為 0
        for i in G[node]:  # 遍歷當前節點的所有子節點
            dfs(i)  # 遞迴探索子節點
            # 在所有子節點中，取最高高度 + 1 作為自己的高度
            mx = max(mx, height[i] + 1)

        height[node] = mx  # 記錄該節點的高度

# ---------- 主程式開始 ----------
n = int(input())  # 讀入節點數量（n 個節點，編號 0 到 n-1）

# 初始化鄰接串列（G[i] 存的是節點 i 的子節點列表）
G = [[] for i in range(n)]

# 初始化 Parent[i] = -1 表示每個節點預設沒有父節點
Parent = [-1 for i in range(n)]

# 讀取每個節點的子節點資訊
for i in range(n):
    row = list(map(int, input().split()))  # 輸入一行（第 i 行）

    if row[0] > 0:  # 如果有子節點
        t = []
        for x in range(1, len(row)):  # 取出子節點，轉為 0-based 編號
            t.append(row[x] - 1)

        G[i] = t  # 記錄節點 i 的所有子節點

        # 將子節點 j 的父節點設為 i
        for j in G[i]:
            Parent[j] = i

# 找出根節點（唯一一個沒有父節點的節點，Parent 值為 -1）
for r in range(n):
    if Parent[r] == -1:
        root = r
        break

# 初始化每個節點的高度為 0
height = [0 for x in range(n)]

# 從根節點開始 DFS 遞迴計算高度
dfs(root)

# 計算所有節點的高度總和（也就是整棵樹的深度總和）
ans = 0
for x in range(n):
    ans += height[x]

# 輸出根節點（題目要求 1-based），以及所有節點深度的總和
print(root + 1)
print(ans)
