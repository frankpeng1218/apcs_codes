import random  # 匯入 random 模組以生成隨機數

N = 10  # 定義要產生的隨機數數量

def merge_data(L, R):
    result = []  # 儲存合併後的排序結果

    l_index = 0  # 左子陣列索引
    r_index = 0  # 右子陣列索引

    # 合併兩個已排序的子陣列
    while l_index < len(L) and r_index < len(R):
        if L[l_index] < R[r_index]:  # 若左子陣列當前元素較小，則加入結果陣列
            result.append(L[l_index])
            l_index += 1
        else:  # 否則加入右子陣列的當前元素
            result.append(R[r_index])
            r_index += 1

    # 加入剩餘未處理的元素
    result += L[l_index:]
    result += R[r_index:]

    return result  # 返回合併後的排序結果

def merge_sort(arr):
    if len(arr) <= 1:  # 若陣列長度小於等於 1，則直接返回
        return arr

    mid = len(arr) // 2  # 找出陣列的中點
    left = merge_sort(arr[:mid])  # 遞迴排序左半部
    print("L", left)  # 顯示當前排序後的左半部
    right = merge_sort(arr[mid:])  # 遞迴排序右半部
    print("R", right)  # 顯示當前排序後的右半部

    return merge_data(left, right)  # 合併兩個已排序的子陣列

# 建立未排序串列，包含 N 個 1 到 100 之間的隨機數
nums = [random.randint(1, 100) for i in range(N)]
print(nums)  # 輸出未排序的數列

r = merge_sort(nums)  # 執行合併排序

print(r)  # 輸出排序後的數列
