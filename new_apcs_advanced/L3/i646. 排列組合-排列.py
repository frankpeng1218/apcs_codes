# i646. 排列組合－排列

from itertools import permutations

# 題目最多只會用到前 8 個字母
ch = "abcdefgh"

while True:
    try:
        # 讀入 N
        N = int(input())

        # 終止條件：輸入 0 時結束
        if N == 0:
            break

        # 取出前 N 個字母
        # 例如：
        # N = 3 → items = "abc"
        # N = 7 → items = "abcdefg"
        items = ch[:N]

        # 使用 itertools.permutations
        # 產生 items 中所有長度為 N 的排列
        # 每一個 combo 是一個 tuple，例如 ('a','b','c')
        for combo in permutations(items, N):
            # 將 tuple 轉成字串後輸出
            # ('a','b','c') → "abc"
            print(''.join(combo))

    except:
        break
