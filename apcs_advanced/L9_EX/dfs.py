# 建立一個空的圖結構 (鄰接表)
G = []

def DFS(start):
    # 標記當前節點 start 已被訪問
    visit[start] = True

    # 遍歷與 start 相連的所有節點
    for i in G[start]:
        # 如果節點 i 尚未被訪問
        if visit[i] == False:
            # 將節點 i 的訪問狀態設為 "從 start 來的"
            # 這裡相當於記錄節點的前驅 (父節點)，方便之後還原路徑
            visit[i] = start

            # 遞迴呼叫 DFS，繼續往更深層搜尋
            DFS(i)

    # 遞迴結束，回傳 None 
    return
