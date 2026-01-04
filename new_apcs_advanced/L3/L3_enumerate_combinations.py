#
# 枚舉組合 2：C(n, m)
# 功能說明：
# 給定一組元素 elements（共 n 個）
# 列出所有「選 m 個、不重複、順序不重要」的組合
#

def enumerate_combinations(elements, m):
    # n 為元素總數
    n = len(elements)

    # subset 用來存放「目前正在建構的組合」
    subset = []

    def backtrack(start):
        # start 表示「下一個可以選取的元素索引」
        # 確保後續只能往後選，避免重複與順序問題

        # --------------------
        # 終止條件 1：
        # 若目前已選取 m 個元素，代表形成一個合法組合
        # --------------------
        if len(subset) == m:
            print(subset)
            return

        # --------------------
        # 終止條件 2（基本剪枝）：
        # 若 start 已超過元素範圍，代表沒有元素可選
        # --------------------
        if start >= n:
            return

        # --------------------
        # 嘗試從 start 開始，選取每一個可能的元素
        # --------------------
        for i in range(start, n):
            # 選取第 i 個元素
            subset.append(elements[i])

            # 遞迴處理下一個位置
            # 下一次只能從 i+1 之後的元素開始選
            backtrack(i + 1)

            # 回溯（Backtracking）：
            # 將剛剛選取的元素移除
            # 嘗試其他組合可能
            subset.pop()

            # 說明：
            # 「不選 elements[i]」的情況
            # 會由 for 迴圈自動帶到下一個 i
            # 不需要額外寫一條遞迴

    # 從索引 0 開始選取元素
    backtrack(0)


# 範例：
# elements = [1, 2, 3, 4, 5]
# m = 3
# 總組合數為 C(5, 3) = 10
enumerate_combinations([1, 2, 3, 4, 5], 3)
