import sys

# 從標準輸入 (stdin) 讀取每一行輸入資料
for s in sys.stdin:
    # 將這一行以空白分割，轉成整數列表
    # 例如輸入 "5 10 20 30 40 50" -> nums = [5, 10, 20, 30, 40, 50]
    nums = list(map(int, s.split()))  # nums = [int(i) for i in s.split()]

    # nums[0] 表示後面有幾個數字
    N = nums[0]

    total = 0  # 用來累加總和
    # 從 nums[1] 到 nums[N] 把所有數字加總
    for i in range(1, N+1):
        total = total + nums[i]
        
    # 平均值 = 總和 / 數字個數
    average = total / N

    # 印出平均值
    print(average)
