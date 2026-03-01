# k714: 外送接單
# 貪心法(Greedy Algorithm)：依截止時間排序（因為要先處理時間的問題）

# 讀取訂單數量
n = int(input())

orders = []  # 每筆存 (p, t)：p = 需要時間，t = deadline

# 讀取每筆訂單
for _ in range(n):
    p, t = map(int, input().split())
    orders.append((p, t))

# 步驟 1：依照截止時間 t 排序（若 t 相同 → p 小的先）
orders.sort(key=lambda x: (x[1], x[0]))


# def sort_rule(order):
#     return (order[1], order[0])  # (t, p)
# orders.sort(key=sort_rule)

# decorated = []
# for p, t in orders:
#     decorated.append(((t, p), (p, t)))  # 把排序依據包進去
# decorated.sort()  # Python 直接排 tuple
# orders = [item[1] for item in decorated]

total_p = 0         # 已接單的總耗時
selected = []       # 已選擇的訂單所花費的時間（p 值）

# 步驟 2：逐筆嘗試接單
for p, t in orders:

    selected.append(p)
    total_p += p

    # 若總耗時超過該訂單截止時間 → 刪除耗時最久的訂單
    if total_p > t:
        longest_p = max(selected)
        selected.remove(longest_p)
        total_p -= longest_p

# selected 的數量就是可完成的訂單數
print(len(selected))
