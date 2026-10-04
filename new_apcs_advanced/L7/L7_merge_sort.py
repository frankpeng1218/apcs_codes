#
# 合併排序法（Merge Sort）實作
# 核心觀念：分治法（Divide and Conquer）
# 1. 分割（Divide）：將串列從中間對半切，遞迴切到長度 <= 1。
# 2. 合併（Conquer / Merge）：將兩個已排序的子串列，按大小依序合併為一個排序好的新串列。
#

import random

# 定義要隨機生成的資料數量
N = 10

def merge_data(L, R):
    """
    將兩個已排序好的串列 L (Left) 與 R (Right) 合併成一個新的已排序串列
    """
    result = []  # 存放合併後的結果

    l_index = 0  # 左側串列的讀取指標
    r_index = 0  # 右側串列的讀取指標

    # 當兩邊都還有元素尚未比較時，持續進行比大小
    while l_index < len(L) and r_index < len(R):
        if L[l_index] < R[r_index]:
            # 左邊較小，將左邊元素加入結果，並將左指標右移
            result.append(L[l_index])
            l_index += 1
        else:
            # 右邊較小或相等，將右邊元素加入結果，並將右指標右移
            result.append(R[r_index])
            r_index += 1

    # 將剩餘沒比完的元素一次接在結果後面（因為兩串列原本就已排序，直接切片拼接即可）
    result += L[l_index:]
    result += R[r_index:]

    return result

def merge_sort(arr):
    """
    合併排序法的主遞迴函式
    """
    # 遞迴終止條件（Base Case）：當長度小於等於 1 時，本身即已排好序，直接返回
    if len(arr) <= 1:
        return arr

    # 1. 分割：找出中間索引位置
    mid = len(arr) // 2

    # 2. 遞迴呼叫：對左半部進行排序
    left = merge_sort(arr[:mid])
    print("L", left)  # 印出當前完成排序的左半部（除錯/觀察流程用）

    # 3. 遞迴呼叫：對右半部進行排序
    right = merge_sort(arr[mid:])
    print("R", right)  # 印出當前完成排序的右半部（除錯/觀察流程用）

    # 4. 合併：將左右兩邊排序後的結果合併並回傳
    return merge_data(left, right)

# 建立未排序串列：隨機生成 N 個介於 1 到 100 之間的整數
nums = [random.randint(1, 100) for i in range(N)]
print("原始未排序串列：", nums)

# 執行合併排序
r = merge_sort(nums)

# 輸出最終排序結果
print("最終排序結果：", r)