import random

N = int(input())  # 讀入要產生的隨機整數數量

nums = []  # 用來儲存隨機整數的清單

for i in range(N):
    x = random.randint(1, 100)  # 產生 1 到 100 之間的隨機整數
    nums.append(x)  # 將隨機數加入清單

print(nums)  # 輸出原始的隨機數清單
nums.sort()  # 對清單進行排序
print("min value:", nums[0])  # 輸出最小值（排序後的第一個數）
print("MAX value:", nums[N-1])  # 輸出最大值（排序後的最後一個數）
