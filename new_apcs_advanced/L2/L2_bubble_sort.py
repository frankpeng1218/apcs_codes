import random              # 匯入 random 模組，用來隨機打亂資料

# 建立一個包含 1~9 的串列
data = [x for x in range(1, 10)]

# 將串列中的資料隨機打亂（模擬未排序的資料）
random.shuffle(data)

# 印出排序前的資料
print("排序前:", data)

compare_count = 0          # 記錄「比較」發生的次數
swap_count = 0             # 記錄「交換」發生的次數

N = len(data)              # 取得串列長度（元素個數）

# 外層迴圈：控制「第幾輪排序」
# 每一輪都會把一個最大的數字排到最後面
for i in range(N):

    # 內層迴圈：進行相鄰元素的比較
    # N - i - 1 的原因：
    # 1. 最後 i 個元素已經排好，不需要再比較
    # 2. j+1 不可以超出索引範圍
    for j in range(N - i - 1):

        compare_count += 1     # 每進行一次比較就累加一次

        # 如果前面的數字比後面的數字大，就需要交換
        if data[j] > data[j + 1]:

            # 傳統三步驟交換（使用暫存變數 temp）
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

            swap_count += 1    # 每交換一次就累加一次

# 印出排序後的結果
print("排序結果：", data)

# 印出總比較次數
print("總比較次數：", compare_count)

# 印出總交換次數
print("總交換次數：", swap_count)
