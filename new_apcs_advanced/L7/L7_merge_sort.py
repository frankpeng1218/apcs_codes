#
# 合併排序法實作
#

import random

N=10

def merge_data(L, R):
    result = []

    l_index = 0
    r_index = 0

    while l_index < len(L) and r_index < len(R):
        if L[l_index] < R[r_index]:
            result.append(L[l_index])
            l_index += 1
        else:
            result.append(R[r_index])
            r_index += 1

    result += L[l_index:]
    result += R[r_index:]

    return result

def merge_sort(arr):
    if len(arr) <=1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    print("L", left)
    right = merge_sort(arr[mid:])
    print("R", right)

    return merge_data(left, right)

# 建立未排序串列
nums = [ random.randint(1, 100) for i in range(N) ]
print(nums)

r = merge_sort(nums)

print(r)
