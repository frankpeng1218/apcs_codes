#
# 泡泡排序法範例
#

# 泡泡排序法 (寫法1)
def bubble_sort(arr):
    for i in range(0, len(arr)-1):  # 外層迴圈控制排序過程的輪數
        for j in range(len(arr)-1, i, -1):  # 內層迴圈從陣列末端往前比較與交換
            if arr[j] <= arr[i]:  # 若當前數值小於或等於前一個數值，則交換
                arr[j], arr[i] = arr[i], arr[j]

    return arr  # 返回排序後的陣列

'''
# 泡泡排序法 (寫法2)
def bubble_sort(arr):
    for i in range(len(arr)-1):  # 外層迴圈控制排序過程的輪數
        for j in range(0, len(arr)-i-1):  # 內層迴圈從開頭遍歷至未排序區域的末端
            if arr[j] > arr[j+1]:  # 若當前數值大於下一個數值，則交換
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr  # 返回排序後的陣列
'''

#start
arr = [64, 34, 25, 12, 22, 11, 90]  # 測試陣列
  
r = bubble_sort(arr)  # 執行泡泡排序

print(r)  # 輸出排序結果
