# Frank解題影片：https://www.youtube.com/watch?v=9439qoHNsN0

# a010. 因數分解
# 知識點: 遞歸的方式取出因數的次數
import sys

MAX_SIZE = 1000000  # 設定最大範圍
# 定義所有因數的次數 (初始化都為0)
number_count = [0 for i in range(MAX_SIZE)]

# 自定義函數，用來計算所有因數的數量
def divide(n):
    n = int(n)  # 轉換為整數
    temp = n  # 暫存變數
    for i in range(2, n + 1):  # 從2開始找因數
        if n % i == 0:  # 若 i 是 n 的因數
            number_count[i] = number_count[i] + 1  # 記錄該因數出現的次數
            temp = temp / i  # 將 n 除以 i，繼續分解
            break  # 跳出迴圈，只分解一次
    # 當 temp = n，表示沒有進行因數分解，代表 n 已為 1
    if temp != n:
        return divide(temp)  # 遞迴處理剩餘的數值

# 讀取輸入，逐行處理
for s in sys.stdin:
    N = int(s)  # 讀取整數 N

    divide(N)  # 進行因數分解

    # 計算 "*" 的數量 (用來控制輸出格式)
    mul_count = 0
    for i in range(2, MAX_SIZE):
        if number_count[i] > 0:  # 如果該數出現過
            mul_count = mul_count + 1  # 計算有多少個不同的因數
    mul_count = mul_count - 1  # 由於最後一個因數不需要 "*"，所以減 1

    # 輸出質因數分解結果
    for k in range(2, MAX_SIZE):
        if number_count[k] != 0:  # 如果 k 是 N 的因數
            if number_count[k] == 1:
                print(k, end='')  # 若因數只出現一次，直接輸出
            else:
                print(f'{k}^{number_count[k]}', end='')  # 若因數出現多次，顯示次方格式

            # 如果還沒輸出完所有因數，則加上 " * "
            if mul_count != 0:
                print(' * ', end='')
                mul_count = mul_count - 1  # 減少計數，避免最後多印 "*"
    
    print()  # 換行輸出下一組測資結果
    number_count = [0 for i in range(MAX_SIZE)]  # 重置 number_count 陣列，以便處理下一筆輸入
