import sys

N = 0  # 儲存輸入的數字 N

# 答案的數列（第0位沒用到，所以用 index 從 1 開始）
ans = [ 0 for i in range(10) ]

# 記錄數字出現的次數，避免重複挑選（用來控制每個數字只能出現一次）
num_times = [ 0 for i in range(10) ]

# 遞迴函數：從 step 位置開始找下一個數字
def find_next(step):

    # 如果已經填滿了 N 個位置（step 超出範圍），表示一組排列完成，輸出結果
    if step == N + 1:
        for i in range(1, N + 1):
            print(ans[i], end='')  # 印出一整組排列
        print()  # 換行
        return  # 結束這次遞迴

    # 嘗試從 N 開始往 1 減（反向順序排列），試著填入還沒出現過的數字
    for x in range(N, 0, -1):
        if num_times[x] == 0:  # 如果 x 還沒被使用過
            ans[step] = x      # 把 x 放進答案序列中
            num_times[x] = 1   # 標記 x 已使用

            find_next(step + 1)  # 遞迴處理下一個位置

            num_times[x] = 0   # 回溯，重設為未使用

# start
for s in sys.stdin:
    # 忽略只有換行的輸入行（例如輸入結束時按 Enter）
    if s[0] != '\n':  # 需要加入此行, 請參考 a524 本題討論
        N = int(s)
        find_next(1)  # 從第一個位置開始找排列
