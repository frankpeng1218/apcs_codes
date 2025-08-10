#
# a233 排序
#

def bubble_sort(arr):
    # 外層迴圈控制排序過程的輪數
    for i in range(0, len(arr)-1):
        # 內層迴圈從陣列末端往前比較與交換
        for j in range(len(arr)-1, i, -1):
            if arr[j] <= arr[i]:  # 如果當前數值小於或等於前一個數值，則交換
                arr[j], arr[i] = arr[i], arr[j]

    return arr  # 返回排序後的陣列
    

#start
N = int(input())  # 讀取整數 N，表示數字個數

num = list(map(int, input().split()))  # 讀取 N 個整數並存入 num 陣列

sorted_num = bubble_sort(num)  # 對 num 進行氣泡排序

# 輸出排序後的數字，使用空格間隔
for i in range(N):
    print(sorted_num[i], end=' ')
print()  # 換行
