# i645. 排列組合－組合

from itertools import combinations

# 題目規定最多只會用到前 10 個小寫字母
letters = 'abcdefghij'

while True:
    try:
        # 讀入 N, M
        # 例如輸入：4 2
        # 表示從前 4 個字母 a b c d 中選 2 個
        N, M = map(int, input().split())

        # 終止條件：輸入 0 0 時結束程式
        if N == 0 and M == 0:
            break

        # 取出前 N 個字母
        # 例如 N = 4 → items = "abcd"
        items = letters[:N]

        # 使用 itertools.combinations
        # 產生所有從 items 中選出 M 個元素的組合
        # 每一個 combo 會是一個 tuple，例如 ('a','b')
        for combo in combinations(items, M):
            # 將 tuple 轉成字串後輸出
            # ('a','b') → "ab"
            print(''.join(combo))

    except:
        break
