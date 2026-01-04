#
# 枚舉元組（tuple）的遞迴函式
# 功能說明：
# 從 1 ~ N 中取值
# 產生長度為 k 的所有可能序列

def enumerate_tuples(N, k):
    # solution 用來存目前正在建立的序列
    # 長度為 k，每個位置一開始都是 None
    solution = [None] * k 

    def backtrack(pos):
        # pos 表示目前要填第幾個位置（0 ~ k-1）

        # 終止條件：
        # 當 pos == k，代表 k 個位置都已填好
        if pos == k:
            # 使用 *solution 將 list 拆開來輸出
            # 例如 [1,2,3] 會輸出成：1 2 3
            print(*solution) 
            return

        # 嘗試在第 pos 個位置，放入所有可能的數字
        # num 從 1 到 N（包含 N）
        for num in range(1, N + 1):
            # 將目前選擇的數字放到第 pos 個位置
            solution[pos] = num

            # 遞迴呼叫，繼續填下一個位置
            backtrack(pos + 1)

            # 回溯（backtracking）說明：
            # 這裡不需要特別把 solution[pos] 清空
            # 因為下一次迴圈會直接覆蓋這個位置

    # 從第 0 個位置開始遞迴枚舉
    backtrack(0)

# N = 3, k = 3
# 代表從 {1,2,3} 中
# 產生所有長度為 3 的序列
enumerate_tuples(3, 3)
