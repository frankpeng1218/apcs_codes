#
# BST 遞迴版本
#

def bs_recursive(arr, target, left, right):
    if left >= right:                # 終止條件：找不到
        return -1

    mid = (left + right) // 2       # 中間位置
    if arr[mid] == target:          # 找到了！
        return mid + 1              # 回傳 1-based index
    elif arr[mid] < target:         # 搜尋右半邊
        return bs_recursive(arr, target, mid + 1, right)
    else:                           # 搜尋左半邊
        return bs_recursive(arr, target, left, mid)

#start
a = list(map(int, input().split()))
t = int(input())

print(bs_recursive(a, t, 0, len(a)))

