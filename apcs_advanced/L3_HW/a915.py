# 引入 cmp_to_key 模組，允許我們自定義比較規則用於排序
# 1. functool cmp_to_key
from functools import cmp_to_key

# 定義比較函數 obj，指定二維點的排序邏輯
def obj(a, b):
    # 比較 x 座標
    if a[0] > b[0]:
        return 1  # a 的 x 座標較大，排序靠後
    elif a[0] < b[0]:
        return -1  # a 的 x 座標較小，排序靠前
    else:
        # 如果 x 座標相等，則比較 y 座標
        if a[1] > b[1]:
            return 1  # a 的 y 座標較大，排序靠後
        elif a[1] < b[1]:
            return -1  # a 的 y 座標較小，排序靠前
        else:
            return 0  # x 和 y 座標都相等，保持不變

# 開始執行主程式
# 讀取點的數量 N
N = int(input())  # 第一行輸入一個正整數 N，表示有 N 個點

# 初始化一個空的列表，用於存放輸入的點座標
data = []

# 讀取 N 個點的座標
for i in range(N):
    # 每行輸入兩個以空格隔開的正整數 x[i] 和 y[i]，表示第 i 個點的座標
    row = list(map(int, input().split()))
    # 將點的座標加入列表中
    data.append(row)

# 使用 sorted 函數對點進行排序，並指定自定義的排序邏輯 obj
# cmp_to_key 將比較函數 obj 包裝成適用於 sorted 的 key
r = sorted(data, key=cmp_to_key(obj))

# 將排序後的結果逐行輸出
for i in r:
    # 格式化輸出每個點的座標，使用空格分隔 x 和 y
    print(i[0], i[1], end=" ")
    print()



# 2.lambda

# 開始執行主程式
# 讀取點的數量 N
N = int(input())  # 第一行輸入一個正整數 N，表示有 N 個點

# 初始化一個空的列表，用於存放輸入的點座標
data = []

# 讀取 N 個點的座標
for i in range(N):
    # 每行輸入兩個以空格隔開的正整數 x[i] 和 y[i]，表示第 i 個點的座標
    row = list(map(int, input().split()))
    # 將點的座標加入列表中
    data.append(row)

# 使用 sorted 函數對點進行排序，直接用 lambda 指定多層排序邏輯
# 先按 x 座標升序排序，如果 x 相等，再按 y 座標升序排序
r = sorted(data, key=lambda point: (point[0], point[1]))

# 將排序後的結果逐行輸出
for i in r:
    # 格式化輸出每個點的座標，使用空格分隔 x 和 y
    print(i[0], i[1], end=" ")
    print()
