# 讀取節點數量 n
n = int(input()) 

# 初始化陣列：
parent = [-1] * (n+1)  # parent[i] 記錄節點 i 的父節點 (-1 表示還未設定) # 裡面放該index的媽媽
height = [-1] * (n+1)  # height[i] 記錄節點 i 的高度 (-1 表示還未計算)
height[0] = 0  # 確保陣列 height 有初始值
child_count = [0] * (n+1)  # child_count[i] 記錄節點 i 有多少個子節點 # 該index點有多少子節點數量



# **讀取樹的結構**
for node in range(1, n+1):
    temp = list(map(int, input().split()))  # 讀取一行輸入，格式: [子節點數量, 子節點1, 子節點2, ...]
    child_count[node] = temp.pop(0)  # 第一個數字表示這個節點有多少個子節點
    for child in temp:  
        parent[child] = node  # 記錄 child 節點的父節點為 node

# **找出葉節點 (沒有子節點的節點)**
leaf_nodes = []
for node in range(1, n+1):
    if parent[node] == -1:  # 父節點仍為 -1，表示它是根節點 (唯一沒有父節點的節點)
        root = node  
    if child_count[node] == 0:  # 若該節點沒有子節點，則視為葉節點
        leaf_nodes.append(node)  # 把葉節點存入 `leaf_nodes` 陣列
        height[node] = 0  # 根據題意，葉節點的高度為 0

# **計算每個節點的高度 (使用 BFS-like 方法)**
while leaf_nodes:  # 當還有葉節點待處理時
    node = leaf_nodes.pop(0)  # 取出 `leaf_nodes` 陣列中的第一個葉節點
    parent_node = parent[node]  # 找出該葉節點的父節點
    if parent_node != -1:  # 避免 root 沒有父節點的情況
        height[parent_node] = max(height[parent_node], height[node] + 1)  
        # 計算父節點的高度 = max(當前高度, 子節點的高度 + 1)
        
        child_count[parent_node] -= 1  # 該父節點的子節點數量減少 (因為這個子節點已處理完)
        
        if child_count[parent_node] == 0 and parent[parent_node] != -1:  
            # 如果這個父節點的所有子節點都處理完了，且它不是根節點，則加入 `leaf_nodes`
            leaf_nodes.append(parent_node)  # 父節點變成新的葉節點，加入隊列繼續處理

# **輸出根節點**
print(root)  # 根節點是唯一沒有父節點的節點 (parent[root] == -1)

# **輸出所有節點的高度總和 H(T)**
print(sum(height))  # H(T) = 所有節點的高度加總

