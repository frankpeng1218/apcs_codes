# c002. 10696 - f91
# 1. 遞迴練習

def f91(n):
    # 若 n >= 101，直接回傳 n - 10
    if n >= 101:
        return n - 10
    else:
        # 否則遞迴呼叫 f91(f91(n + 11))
        return f91(f91(n + 11))

while True:
    try:
        n = int(input())  # 讀取整數輸入

        if n == 0:        # 輸入 0 時結束
            break

        ans = f91(n)      # 計算 f91(n)
        print(f"f91({n}) = {ans}")  # 輸出結果
    except:
        break             # 非整數或 EOF 結束
