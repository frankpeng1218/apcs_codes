#
# 枚舉組合 1：列舉所有子集（不限定子集大小）
# 功能說明：
# 給定一組元素 elements
# 列出它的所有子集（包含空集合）
# 每個元素只有兩種選擇：選 or 不選
#

def enumerate_subsets(elements):
    # n 為元素個數
    n = len(elements)

    # subset 用來存放「目前正在建立的子集」
    # 這是一個動態變化的串列
    subset = []

    def backtrack(index):
        # index 表示目前正在考慮第幾個元素（0 ~ n-1）

        # 終止條件：
        # 當 index == n，代表每個元素都已經「選或不選」過
        if index == n:
            # 輸出目前形成的一個子集
            # 注意：subset 可能是空的，也可能包含多個元素
            print(subset)
            return

        # --------------------
        # 情況 1：選取第 index 個元素
        # --------------------
        # 將 elements[index] 加入目前子集
        subset.append(elements[index])

        # 遞迴處理下一個元素
        backtrack(index + 1)

        # 回溯（Backtracking）：
        # 把剛剛加入的元素移除
        # 讓 subset 回到「尚未選此元素」的狀態
        subset.pop()

        # --------------------
        # 情況 2：不選取第 index 個元素
        # --------------------
        # 不改變 subset，直接處理下一個元素
        backtrack(index + 1)

    # 從第 0 個元素開始做選 / 不選的決策
    backtrack(0)

# 測試範例：
# elements = [1, 2, 3]
# 子集總數為 2^3 = 8
enumerate_subsets([1, 2, 3])
