# f606. 2. 流量
# 1. 流量累積
# 2. 費用計算

# n: 伺服器數量, m: 城市數量, k: 方案數量
n, m, k = map(int, input().split())

# 讀取Q, 每個伺服器傳送到各城市的流量
Q = [list(map(int, input().split())) for i in range(n)]

# 紀錄每個方案的總花費
costs = [] 

# 讀取k種方案並計算成本
for i in range(k):
    c = list(map(int, input().split())) # 讀取該方案的伺服器擺放城市
    flow = [[0] *m for _ in range(m)] # 初始化城市間的流量矩陣

    # 計算伺服器流量傳輸到各城市
    for server_idx in range(n): # 遊歷每個伺服器(0~n-1)
        server_city = c[server_idx] # 取得該伺服器的擺放城市(在哪個城市運行伺服器)

        for target_city in range(m): # 遊歷目標城市(0~m-1)
            transmission_amount = Q[server_idx][target_city] # 伺服器要傳輸到該城市的流量
            flow[server_city][target_city] += transmission_amount

    cost = 0 # 初始化成本

    # 計算該方案的總成本
    for x in range(m): # 遊歷每個起始城市
        for y in range(m): # 遊歷每個目標城市
            if flow[x][y] >0: # 如果有流量要傳輸
                if x == y:
                    cost += flow[x][y] * 1
                else:
                    if flow[x][y] <= 1000:
                        cost += flow[x][y] * 3
                    else:
                        cost += (1000*3) + ((flow[x][y] -1000) * 2) # 前1000個單位*3, 超過的*2
    costs.append(cost)

print(min(costs))







        














    
