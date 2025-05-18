# 讀取 n（伺服器數量）、m（城市數量）、k（方案數量）
n, m, k = map(int, input().split())

# 讀取每個伺服器傳送到各城市的流量，q[i][j] 表示第 i 個伺服器傳送到第 j 個城市的流量
q = []
for i in range(n):
    q.append(list(map(int, input().split())))

# 用來儲存每種方案的總成本
cost = []

# 處理每一種方案
for i in range(k):
    # 讀取第 i 種方案中每個伺服器部署在哪個城市（c[i] = 城市編號）
    c = list(map(int, input().split()))
    
    # 初始化城市間的實際使用流量矩陣，inuse[x][y] 表示從城市 x 傳到城市 y 的總流量
    inuse = [[0 for k in range(m)] for x in range(m)]

    # 計算這個方案下，各城市之間的實際流量
    for idx in range(n):  # 遍歷每個伺服器
        for tgt in range(m):  # 遍歷每個目標城市
            # 第 idx 個伺服器設在 c[idx] 城市，把它要傳送到 tgt 城市的流量加入對應 inuse 矩陣
            inuse[c[idx]][tgt] += q[idx][tgt]

    # 開始計算此方案的總成本
    now = 0
    for x in range(m):  # 起始城市
        for y in range(m):  # 目標城市
            if x == y:
                # 如果起始與目標是同一城市，單位流量成本為 1
                now += inuse[x][y]
            elif inuse[x][y] <= 1000:
                # 如果城市之間傳送量不超過 1000，單位流量成本為 3
                now += inuse[x][y] * 3
            else:
                # 超過 1000 的部分，前 1000 單位流量每單位成本 3，超過的部分每單位成本 2
                now += 1000 * 3 + (inuse[x][y] - 1000) * 2

    # 將該方案的成本加入成本列表
    cost.append(now)

# 印出所有方案中最小的總成本
print(min(cost))
