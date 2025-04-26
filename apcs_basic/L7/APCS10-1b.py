import sys  # 匯入 sys 模組，用於讀取標準輸入（stdin）

# 使用 sys.stdin 持續讀取每一行輸入（通常用於檔案或大量資料輸入）
for s in sys.stdin:
    # 將每行輸入以空格切割，並轉換為整數列表
    nums = list(map(int, s.split()))

    # nums[0] 是 N，代表接下來要處理幾個數字
    N = nums[0]

    # 從 nums[1] 開始印出 N 個數字，中間以空格分隔
    for i in range(1, N + 1):
        print(nums[i], end=' ')
    
    # 每列結束後換行
    print()
