# 方法 1：逐步處理
s = input()              # 從鍵盤讀入一行字串，例如輸入: "1 2 3 4"
s = s.split()            # 以空白分割字串，結果變成: ["1", "2", "3", "4"]
nums = []                # 建立一個空的列表，用來存放轉換後的整數

for i in s:              # 逐一取出字串列表中的元素
    nums.append(int(i))  # 把字串轉成整數，並加到 nums 列表裡

print(nums)              # 輸出結果，例如: [1, 2, 3, 4]


# 方法 2：列表生成式 (list comprehension)
s = input()                     # 從鍵盤讀入一行字串
nums = [int(i) for i in s.split()]  # 先 split() 切成字串，再逐一轉換成 int，直接組成新列表


# 方法 3：更簡潔，直接寫在一行
nums = [int(i) for i in input().split()]  
# 讀取輸入、切割、轉換、組成列表，一行完成


# 方法 4：利用 map 函數
nums = list(map(int, input().split()))  
# input().split() → 先得到字串列表
# map(int, ...)   → 把每個字串轉換成整數
# list(...)       → 把 map 物件轉換成真正的列表
