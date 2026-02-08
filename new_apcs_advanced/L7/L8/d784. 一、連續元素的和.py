# d784: 連續元素的和
# 動態規劃（DP）
# Kadane's Algorithm（最大子序和）
# Kadane's Algorithm 參考影片https://www.youtube.com/watch?v=g-XcfPbLwQ8

n = int(input())  # 測試資料筆數

for _ in range(n):
    nums = list(map(int, input().split()))

    length = nums.pop(0)  # 第一個值為陣列長度
    dp = [0] * length  # dp[i] = 以 i 結尾的最大連續和

    # 初始化：以第 0 個數字結尾的最大和，就是 nums[0]
    dp[0] = nums[0]

    for i in range(1, length):
        # 兩種選擇：
        # 1. 重新開始一段序列（只取 nums[i]）
        # 2. 接續前面的最大和（dp[i-1] + nums[i]）
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    # 最大子序和就是所有 dp 值中的最大值
    print(max(dp))

# nums = [-5, -2, 6, -1, 3]
# dp = [0] * 5

# 1. dp[0] = nums[0] = -5
# 2. dp[1] = max(nums[1], dp[1-1] + nums[1]) = -2
# 3. dp[2] = max(nums[2], dp[2-1] + nums[2]) = 6
# 4. dp[3] = max(nums[3], dp[3-1] + nums[3]) = 5
# 5. dp[4] = max(nums[4], dp[4-1] + nums[4]) = 8