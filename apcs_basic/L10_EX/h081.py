# h081: 程式交易

# 讀取輸入
n, D = map(int, input().split())  # n: 天數, D: 價格波動閾值
prices = list(map(int, input().split()))  # 股票的每日價格列表

# 初始化變數
x = 0  # 當前參考價格（買入價或賣出後的基準價），一開始為沒有持有股票(x=0)
haveStock = False  # 是否持有股票
benefit = 0  # 總獲利

# 遍歷每一天的股票價格
for i in range(n):
    # 尚未持有股票(第一次) 或 (條件3)尚未持有股票且價格滿足條件，可以買進
    if x == 0 or (prices[i] <= (x - D) and haveStock == False):
        x = prices[i]  # 更新參考價格為買入價
        haveStock = True  # 設定為已持有股票

    # (條件2)若已持有股票且價格滿足條件，可以賣出
    elif prices[i] >= (x + D) and haveStock == True:
        benefit += prices[i] - x  # 計算當前獲利並累加到總獲利
        x = prices[i]  # 更新參考價格為賣出後的新基準價
        haveStock = False  # 設定為未持有股票

# 輸出總獲利
print(benefit)
