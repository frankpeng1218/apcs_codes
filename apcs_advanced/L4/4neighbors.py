# 定義一個 5x5 的二維陣列，其中 1 代表可行區域，0 代表不可行區域
arr = [[1, 0, 0, 0, 1],
       [1, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 1, 1, 0],
       [1, 0, 0, 0, 0]]

# 建立一個與 arr 相同大小的標記陣列，初始值全部為 0，代表尚未訪問
marker = [[0, 0, 0, 0, 0] for x in range(5)]  

def search_map(arr, marker, x, y):
    """
    使用深度優先搜尋 (DFS) 探索 arr 中的 1，並標記已訪問過的位置。

    參數:
    - arr: 代表地圖的二維陣列
    - marker: 用來記錄已經訪問過的區域
    - x, y: 當前探索的位置座標
    """

    # 若超出邊界 (x 或 y 不在 [0, 4] 範圍內)，則返回
    if (x < 0 or x >= 5) or (y < 0 or y >= 5):
        return
    
    # 若當前位置是 1 且未被標記過，則進行標記並繼續遞迴探索
    if arr[x][y] == 1 and marker[x][y] == 0:
        marker[x][y] = 1  # 標記為已訪問

        # 依照四個方向進行遞迴搜尋 (上下左右)
        # 依照四個方向進行探索(4 beighbors)
        search_map(arr, marker, x-1, y)# 左
        search_map(arr, marker, x+1, y)# 右
        search_map(arr, marker, x, y-1)#上
        search_map(arr, marker, x, y+1)#下
        # 依照四個方向進行探索(8 beighbors)
        search_map(arr, marker, x-1, y-1)# 左上
        search_map(arr, marker, x-1, y+1)# 左下
        search_map(arr, marker, x+1, y-1)#右上
        search_map(arr, marker, x+1, y+1)#右下

# **開始搜尋，從 (2,2) 這個位置開始**
search_map(arr, marker, 2, 2)

# 計算標記為 1 的格子數量，即連通區域的大小
c = 0
for i in range(5):
    for j in range(5):
        if marker[i][j] == 1:
            c += 1  # 若該位置被標記，則計數加 1
            
# 輸出連通區塊內的 1 的數量
print(c)
