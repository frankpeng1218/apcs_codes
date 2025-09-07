import sys  # 匯入 sys 模組，用來讀取標準輸入 (stdin)

# 使用 sys.stdin 可以逐行讀取輸入 (通常用在競賽、處理大量輸入的情境)
for s in sys.stdin:  
    # 把讀到的一行字串 s，用空白切割，再用 map(int, ...) 轉換成整數
    nums = list(map(int, s.split()))  
    
    # 等價寫法 (列表生成式)，同樣是把字串逐一轉換成整數
    # nums = [int(i) for i in s.split()]

    # 輸出轉換後的整數列表
    print(nums)
