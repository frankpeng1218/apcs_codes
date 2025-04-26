import time  # 匯入 time 模組，用來測量執行時間（雖然目前被註解掉）

MAX_SIZE = 10000  # 設定表格最大計算到第 10000 項
table = []  # 建立一個空的 list 作為儲存費波那契數列的表格

# start
N = int(input())  # 讀入使用者輸入的整數 N，代表要查詢的項目（第 N 項）

#start = time.time()  # 計算開始時間（目前這行被註解掉）

# 初始化費波那契數列的前兩項
table.append(1)  # 第 1 項（table[0]）為 1
table.append(2)  # 第 2 項（table[1]）為 2

# 利用迴圈從第 3 項開始遞推到 MAX_SIZE 項
for i in range(2, MAX_SIZE):
    t = table[i - 1] + table[i - 2]  # 費波那契遞推公式：f(n) = f(n-1) + f(n-2)
    table.append(t)  # 把計算結果加到 table 裡

print(table[N - 1])  # 輸出第 N 項（因為索引從 0 開始，所以是 N-1）

#end = time.time()  # 計算結束時間（目前這行被註解掉）
#print("excution time:", round((end-start), 3), "s")  # 印出執行時間（小數點後 3 位）
