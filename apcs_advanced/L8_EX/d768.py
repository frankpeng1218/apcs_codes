# d768. 10004 - Bicoloring

##這題是判斷無向圖是否為二分圖
##二分圖定義：若圖可用兩種顏色塗色，且所有相鄰節點顏色不同，則為二分圖；否則不是。
##BFS 判斷方式：
##從某節點開始標記顏色 1。
##相鄰節點標記為 2，繼續擴展。
##若遇到相鄰節點顏色相同，則非二分圖。
##圖的構建：
##使用鄰接表 (Adjacency List) 存儲邊。
##雙向存儲，因為圖為無向圖。
##這樣 BFS 逐層擴展，即可判斷圖是否為二分圖。
# d406 倒水時間(可參考)

MAX_SIZE = 200

# 使用BFS自定義函數來判斷是否可以用兩種顏色圖色
def BFS(color_map, start):
    # queue 的初始化, 從起點開始
    Q = [start]
    visit = [0 for _ in range(MAX_SIZE)] # 紀錄每個節點的顏色(0: 未訪問, 1: 顏色1, 2: 顏色2)
    #BFS starts
    while len(Q) > 0:
        # 取出當前節點
        now = Q.pop(0)
        #遊歷所有與"now" 相鄰的節點
        for i in color_map[now]:
            #取得下一個相鄰節點
            next_region = i
            # 若該節點未被塗色
            if visit[next_region] == 0:
                Q.append(next_region) # 加入BFS的queue
                if visit[now] == 1:
                    visit[next_region] = 2 # 當前節點是1的話, 則相鄰節點塗2
                else:
		    # 其實也是把第一個鄰居強制定義成顏色 1，而不是把第一個節點定義顏色 1。
                    visit[next_region] = 1 # 當前節點是2的話, 則相鄰節點塗1 

            # 兩個顏色一樣, 則無法二分塗色
            elif visit[next_region] == visit[now]:
                return False
    return True

while True:
    try:
        # 讀取節點數量(N)
        N = int(input())
        # 讀取邊的數量(M)
        M = int(input())
        # 建立鄰接表來存儲圖的連接關係
        color_map = [[] for _ in range(MAX_SIZE)]
        # 讀取M條邊建立無向圖
        for i in range(M):
            u, v = map(int, input().split())
            color_map[u].append(v)
            color_map[v].append(u) # 因為是無向圖, 所以需要雙向建立
        # 執行BFS從節點0開始
        result = BFS(color_map, 0)

        #判斷輸出
        if result:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
    except:
        break











    
