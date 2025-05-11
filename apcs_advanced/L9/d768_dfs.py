# d768. 10004 - Bicoloring｜DFS (Depth-First Search)


#####################################################################
# BFS參考
# Zero JudgeAPCS 解題攻略｜d768. 10004 - Bicoloring｜BFS (Breadth-First Search)
# https://youtu.be/9vSMKHwCrS0
#####################################################################


MAX_SIZE = 200

# result = DFS(color_map, 0, 1, visit)

def DFS(color_map, node, color, visit):
    visit[node] = color # 塗上當前顏色1
    for neighbor in color_map[node]: # 遊歷相鄰節點
        if visit[neighbor] == 0 : # 若該節點未被塗色
            if not DFS(color_map, neighbor, -color, visit): # 塗色為相反顏色
                return False # 若遞迴發現衝突則返回False
        elif visit[neighbor] == visit[node]: # 若相鄰節點與當前節點顏色相塗, 則非二分圖
            return False
    return True
    
while True:
    try:
        # 讀取節點數量(N)
        N = int(input())
        if N == 0:
            break
        # 讀取邊的數量(M)
        M = int(input())
        # 建立連接表來儲存塗的連接關係
        color_map = [[] for _ in range(MAX_SIZE)]
        # 讀取M條邊並建立無向圖
        for i in range(M):
            u, v = map(int, input().split())
            color_map[u].append(v)
            color_map[v].append(u)
        # 初始化訪問陣列
        visit = [0 for _ in range(MAX_SIZE)] # 0: 未訪問, 1: 顏色1, -1: 顏色2
        # 執行DFS, 從節點0開始, 初始化顏色為1
        result = DFS(color_map, 0, 1, visit)
        # 判斷輸出
        if result:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE")
    except:   
        break















    


