#
# 泡泡排序法實作
#
import random
import time

data = [x for x in range(1, 10)]  # 建立 1~9 的數字串列
random.shuffle(data)  # 打亂順序

print("排序前:", *data)  # 顯示原始亂數資料

N = len(data)  # 資料長度

t1 = time.time()  # 記錄排序開始時間

for i in range(0, N - 1):  # 外層控制排序輪數（總共 N-1 輪）
    for j in range(0, N - i - 1):  # 內層控制每輪比較次數
        if data[j] > data[j + 1]:  # 若前項大於後項則交換
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp
            print("change item:", data)  # 顯示每次交換後的狀態

t2 = time.time()  # 記錄排序結束時間

print("排序後:", *data)  # 顯示排序後結果
print("執行時間:", round(t2 - t1, 4), "s")  # 顯示排序執行所花時間（取小數第4位）
