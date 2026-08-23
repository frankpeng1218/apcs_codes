#
# 枚舉排列（Permutation）
# 功能說明：
# 給定一組元素 elements
# 列出所有「不重複、順序有差」的排列
#

def enumerate_permutations(elements):
    # n 為元素個數，也是排列長度
    n = len(elements)

    # used[i] 用來記錄 elements[i] 是否已經被使用過
    # False 表示尚未使用，True 表示已被放入排列中
    used = [False] * n

    # perm 用來存目前正在建構的排列結果
    # perm[pos] 代表排列中第 pos 個位置的元素
    perm = [None] * n

    def backtrack(pos):
        # pos 表示目前要填排列的第幾個位置（0 ~ n-1）

        # 終止條件：
        # 當 pos == n，表示 n 個位置都已填滿
        if pos == n:
            # 使用 *perm 將排列結果拆開來輸出
            print(*perm)
            return

        # 嘗試在第 pos 個位置，放入每一個「尚未使用」的元素
        for i in range(n):
            # 如果 elements[i] 還沒有被使用過
            if not used[i]:
                # 標記此元素為已使用
                used[i] = True

                # 將該元素放入排列的第 pos 個位置
                perm[pos] = elements[i]

                # 遞迴呼叫，繼續填下一個位置
                backtrack(pos + 1)

                # 回溯（Backtracking）：
                # 將 elements[i] 標記回「未使用」
                # 讓它可以在其他排列分支中被再次使用
                used[i] = False

    # 從排列的第 0 個位置開始遞迴
    backtrack(0)


# 列出 [0, 1, 2, 3, 4] 的所有排列
# 總排列數為 5! = 120
enumerate_permutations([0, 1, 2, 3, 4])
