import sys

# 定義二分搜尋函數
def binary_search(sorted_array, array_length, target):
    left = 0  # 左邊界
    right = array_length - 1  # 右邊界

    while left <= right:
        mid = (left + right) // 2  # 計算中間索引
        if target > sorted_array[mid]:
            left = mid + 1  # 縮小搜尋範圍至右半部分
        elif target < sorted_array[mid]:
            right = mid - 1  # 縮小搜尋範圍至左半部分
        else:
            return mid + 1  # 找到目標值，返回其位置（1-based index）
    
    # 如果未找到目標值，返回 0
    return 0

# 開始程式
# 讀取輸入：第一行包含數列長度 N 和查詢數量 K
n_and_k = input()
n, k = map(int, n_and_k.split())  # n 表示數列長度，k 表示查詢數量

# 讀取輸入：第二行是排序數列 A
sorted_array = list(map(int, input().split()))

# 讀取輸入：第三行是查詢數列 X
queries = list(map(int, input().split()))

# 對每個查詢執行二分搜尋
for target in queries:
    print(binary_search(sorted_array, n, target))
