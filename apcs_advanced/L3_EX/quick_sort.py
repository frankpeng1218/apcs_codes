import random  # 匯入 random 模組以生成隨機數

def quick_sort(data, left, right):
    if left < right:  # 確保區間內至少有兩個元素
        pivot = data[left]  # 選擇最左側元素作為基準點
        l = left  # 左指標
        r = right + 1  # 右指標，向右偏移以便處理

        while True:
            # 向右尋找小於 pivot 的位置
            while l < right:    
                l += 1
                if data[l] >= pivot:
                    break

            # 向左尋找大於 pivot 的位置
            while r > 0:
                r -= 1
                if data[r] <= pivot:
                    break

            if l >= r:  # 若指標交錯，則結束本輪交換
                break

            data[l], data[r] = data[r], data[l]  # 交換左右區間的元素
        
        data[left], data[r] = data[r], data[left]  # 將基準點與 r 指標元素交換

        quick_sort(data, left, r - 1)  # 遞迴排序左半部
        quick_sort(data, r + 1, right)  # 遞迴排序右半部

#start
N = int(input())  # 讀取整數 N，表示數字個數

arr = []  # 建立空陣列存放隨機數

for i in range(N):
    num = random.randint(1, 10)  # 生成 1 到 10 之間的隨機數
    arr.append(num)

print(arr)  # 輸出未排序的陣列
quick_sort(arr, 0, N - 1)  # 執行快速排序
print(arr)  # 輸出排序後的陣列
