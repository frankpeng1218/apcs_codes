#
# 枚舉子集和（Subset Sum Enumeration）
# 功能說明：
# 給定一組數字 numbers
# 列出「所有子集」對應的總和
# 每個元素只有兩種選擇：選 or 不選
#

def enumerate_subset_sums(numbers):
    # n 為數字個數
    n = len(numbers)

    def backtrack(index, current_sum):
        # index：目前正在考慮第幾個元素（0 ~ n-1）
        # current_sum：到目前為止所累加的子集總和

        # 終止條件：
        # 當 index == n，代表所有元素都已經「選或不選」過
        if index == n:
            # 輸出一個子集所對應的總和
            print(current_sum)
            return

        # --------------------
        # 選擇 1：選取第 index 個元素
        # --------------------
        # 將 numbers[index] 加入目前的總和
        backtrack(index + 1, current_sum + numbers[index])

        # --------------------
        # 選擇 2：不選取第 index 個元素
        # --------------------
        # current_sum 保持不變
        backtrack(index + 1, current_sum)

    # 從第 0 個元素、目前總和為 0 開始遞迴
    backtrack(0, 0)


# 測試範例：
# numbers = [1, 2, 4]
# 子集共有 2^3 = 8 種
enumerate_subset_sums([1, 2, 4])
