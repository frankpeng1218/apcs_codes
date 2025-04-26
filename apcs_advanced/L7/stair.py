import time  # 匯入 time 模組，用來計算程式執行時間

# 定義一個遞迴函數 f(n)，計算樓梯走法數
def f(n):
    if n < 3:
        return n  # 如果 n 為 0、1、2，則回傳 n（f(0)=0, f(1)=1, f(2)=2）
    else:
        return f(n - 1) + f(n - 2)  # 遞迴公式：f(n) = f(n-1) + f(n-2)

start = time.time()  # 紀錄開始時間

# start
print(f(10))  # 呼叫函數並輸出結果（計算走上 10 階樓梯的方法數）

end = time.time()  # 紀錄結束時間

# 輸出執行時間（小數點後 3 位）
print("excution time:", round((end - start), 3), "s")
