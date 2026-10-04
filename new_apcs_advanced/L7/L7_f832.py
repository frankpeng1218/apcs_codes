#
# ZeroJudge f832: 隕石
# 核心演算法：貪婪演算法（Greedy Algorithm）+ 雙指標（Two Pointers）
# 解題策略：
# 1. 目標是攔截「最大總重量」的隕石。
# 2. 將「隕石重量」與「攔截器容量」皆由大到小排序。
# 3. 優先考慮當前最重的隕石：
#    - 若目前最大容量的攔截器接得住，就直接接（最佳選擇，兩者皆消耗）。
#    - 若目前最大容量的攔截器都接不住，表示「任何攔截器都接不住這顆隕石」，只能放棄該隕石，繼續看下一顆較輕的。
#

# 讀入 n（隕石數量）與 m（攔截器數量）
n, m = map(int, input().split())

# w: 各隕石的重量串列
# c: 各攔截器的最大承載容量串列
w = list(map(int, input().split()))
c = list(map(int, input().split()))

# 由大到小排序（降序），確保每次都先考慮最重隕石與最大容量攔截器
w.sort(reverse=True)
c.sort(reverse=True)

# 雙指標：meteor 指向當前考慮的隕石，catcher 指向當前可用的最大攔截器
meteor, catcher = 0, 0

# 累加成功攔截的隕石總重量
total_weight = 0

# 當還有隕石未處理，且還有可用攔截器時，持續比對
while meteor != n and catcher != m:
    # 情況 1：當前最大攔截器接得住這顆隕石
    if w[meteor] <= c[catcher]:
        total_weight += w[meteor]  # 累加重量
        meteor += 1                # 隕石已被成功攔截，看下一顆
        catcher += 1               # 該攔截器已使用，換下一個攔截器
    
    # 情況 2：連目前最大容量的攔截器都裝不下這顆隕石
    else:
        # 後續更小的攔截器更不可能裝得下它，只能放棄此隕石，看下一顆較輕的
        meteor += 1

# 輸出成功攔截的最大總重量
print(total_weight)