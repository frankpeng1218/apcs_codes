import sys  # 匯入 sys 模組，允許從標準輸入讀取資料

#start
for s in sys.stdin:  
    nums = s.split()  # 讀取一行輸入，並將其拆分成數字字串列表

    size = len(nums)  # 計算數字個數

    for i in range(size):  
        nums[i] = int(nums[i])  # 將數字字串轉換為整數
    
    print(sum(nums) / size)  # 計算並輸出平均值
