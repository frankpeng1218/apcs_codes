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
    right = merge_sort(arr[mid:])  # 遞迴排序右半部

    return merge_data(left, right)  # 合併兩個已排序的子陣列

#start
N = int(input())  # 讀取整數 N，表示數字個數

num = list(map(int, input().split()))  # 讀取 N 個整數並存入 num 陣列

sorted_num = merge_sort(num)  # 執行合併排序

# 輸出排序後的數字，使用空格間隔
for i in range(N):
    print(sorted_num[i], end=' ')
print()  # 換行
