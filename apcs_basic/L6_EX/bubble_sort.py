#
# 泡泡排序法實作
#
import random

# data = [ x for x in range(1, 10)]
# random.shuffle(data)

data = [5, 4, 3, 2, 1]  # 原始資料
print("排序前:", *data)  # 顯示排序前的內容

N = len(data)  # 資料長度

for i in range(0, N-1):  # 外層控制輪數，共需 N-1 輪
    for j in range(0, N-i-1):  # 內層控制每輪比較次數
        if data[j] > data[j+1]:  # 若前者大於後者則交換
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            print("change item:", data)  # 每次交換後顯示中間結果

print("排序後:", *data)  # 顯示排序後的內容
