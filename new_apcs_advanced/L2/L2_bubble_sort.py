#
# 泡泡排序法範例
#

import random

data = [ x for x in range(1, 10)]
random.shuffle(data)

print("排序前:", *data)

compare_count = 0  # 記錄比較次數
swap_count = 0     # 記錄交換次數

N = len(data)
for i in range(N):
    for j in range(N-i-1):
        compare_count += 1
        if data[j] > data[j+1]:
            # 傳統三步交換，凸顯交換成本
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            swap_count += 1

print("排序結果：", data)
print("總比較次數：", compare_count)
print("總交換次數：", swap_count)

