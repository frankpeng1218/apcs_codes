

# 讀取 N（切割次數）和 L（木條總長度）
N, L = map(int, input().split())

# 初始狀態的切割點：木條的起點 0 和終點 L
stick = [0, L]  # 這個列表會動態維護當前的切割點

# 儲存切割位置與對應的順序
temp = []

# 讀取每筆切割資訊
for i in range(N):
    x, order = map(int, input().split())
    temp.append((order, x))  # (切割順序, 切割位置)

# 依據切割順序 `order` 來排序
temp.sort()  # 按照切割順序（第 1 個數字）排序

ans = 0  # 儲存總切割費用

for _, cut_position in temp:
    # 直接將切割點加入 stick 陣列
    stick.append(cut_position)

    # 每次插入後排序，確保 stick 陣列仍然是遞增的
    stick.sort()

    # 找到 cut_position 在 stick 中的索引
    idx = stick.index(cut_position)

    # 計算費用（左右相鄰點的距離）
    ans += stick[idx+1] - stick[idx-1]


print(ans)



import bisect  # 引入 bisect 模組，進行二分搜尋

# 讀取 N（切割次數）和 L（木條總長度）
N, L = map(int, input().split())

# 初始狀態的切割點：木條的起點 0 和終點 L
stick = [0, L]  # 這個列表會動態維護當前的切割點

# 儲存切割位置與對應的順序
temp = []

# 讀取每筆切割資訊
for i in range(N):
    x, order = map(int, input().split())
    temp.append((order, x))  # (切割順序, 切割位置)

# 依據切割順序 `order` 來排序
temp.sort()  # 按照切割順序（第 1 個數字）排序

ans = 0  # 儲存總切割費用

for _, cut_position in temp:
    # 使用 bisect.bisect_left 找到切割點應該插入的位置，並確保仍符合遞增順序，並返回index的值
    idx = bisect.bisect_left(stick, cut_position)

    #######bisect範例
    # stick = [0, 5, 10]
    # x = 5
    # print(bisect.bisect_left(stick, x))   # 1
    # print(bisect.bisect_right(stick, x))  # 2
    ######

    # 插入新的切割點
    stick.insert(idx, cut_position)

    # 計算切割費用（左右相鄰點的距離）
    ans += stick[idx+1] - stick[idx-1]

print(ans)



# bisect.bisect_left(stick, cut_position)：
# 作用：在 stick（已排序列表）中找到 cut_position 應該插入的位置，並確保插入點仍然符合遞增順序。
# 返回值：回傳 cut_position 應該插入的位置的索引。


