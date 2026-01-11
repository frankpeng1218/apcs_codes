# 原始地圖（5x5）
# 1 代表可走/連通的格子
# 0 代表不可走/空格
arr = [[1, 0, 0, 0, 1],
       [1, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 1, 1, 0],
       [1, 0, 0, 0, 0]]

# 標記陣列，用來記錄哪些格子「已經被走過」
# 一開始全部都是 0（尚未拜訪）
marker = [[0, 0, 0, 0, 0] for x in range(5)]


def search_map(arr, marker, x, y):
    """
    使用 DFS（深度優先搜尋）從 (x, y) 開始，
    將所有「相連的 1」標記成已拜訪
    """

    # ----------- 邊界檢查 -----------
    # 如果座標超出地圖範圍，直接結束
    if (x < 0 or x >= 5) or (y < 0 or y >= 5):
        return 0
    
    # ----------- 是否可以走 -----------
    # 條件：
    # 1. 該位置是 1（可走）
    # 2. 尚未被標記過（marker == 0）
    elif arr[x][y] == 1 and marker[x][y] == 0:
        
        # 將目前位置標記為「已拜訪」
        marker[x][y] = 1

        # ----------- 遞迴搜尋四個方向 -----------
        # 上:
        search_map(arr, marker, x, y-1)
        # 下:
        search_map(arr, marker, x, y+1)
        # 左:
        search_map(arr, marker, x-1, y)
        # 右:
        search_map(arr, marker, x+1, y) 


# ----------------- 主程式開始 -----------------

# 從座標 (2, 2) 開始搜尋
search_map(arr, marker, 2, 2)

# 計算被標記為 1 的格子數量
c = 0
for i in range(5):
    for j in range(5):
        if marker[i][j] == 1:
            c += 1

# 印出連通區域的大小
print(c)
