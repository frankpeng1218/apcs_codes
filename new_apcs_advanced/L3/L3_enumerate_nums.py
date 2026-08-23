#
# 枚舉數字 1~10
# 每一個位置都可以選 1~10
# 總共選 5 次（允許重複，順序有差）
#

def backtrack(n):
    # n 代表目前填到第幾個位置（0 ~ 4）

    # 終止條件：
    # 當已經填滿 5 個位置時
    if n == 5:
        # *solution 代表把 list 裡的元素「拆開」來輸出
        # 等同於 print(solution[0], solution[1], ..., solution[4])
        print(*solution)
        return

    # 嘗試在第 n 個位置，放入 1~10 的每一個數字
    for i in range(10):
        # 將第 n 個位置設定為 i+1（因為 i 是 0~9）
        solution[n] = i + 1

        # 遞迴呼叫，繼續填下一個位置
        backtrack(n + 1)

# 建立一個長度為 5 的陣列，用來存目前的選擇結果
solution = [0 for _ in range(5)]

# 從第 0 個位置開始填
backtrack(0)
