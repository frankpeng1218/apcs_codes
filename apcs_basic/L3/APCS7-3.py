#start

N = int(input())  # 讀取輸入的數字 N

# 產生一個列表，包含從 1 到 N，每個數字乘以 3 的結果
num = [3 * x for x in range(1, N + 1)]

print(num)  # 輸出結果列表
