import sys  # 匯入 sys 模組，用於讀取標準輸入

# 透過標準輸入讀取數值
for i in sys.stdin:  
    N = int(i)  # 轉換輸入為整數 N，代表目標數值

    noSolution = True  # 設定一個變數來追蹤是否找到解

    # 遍歷所有可能的起始數 i
    for i in range(0, N):  
        sum_ = 0  # 初始化累加和
        # 從 i 開始累加，檢查是否能得到 N
        for j in range(i, N):  
            sum_ += j  # 累加當前數字
            if sum_ == N:  # 如果總和剛好等於 N，表示找到解
                print(str(i) + "-" + str(j))  # 輸出這段連續數列的範圍
                noSolution = False  # 設定為 False，表示至少找到一組解
                break  # 跳出內層迴圈，開始找下一個起始數

    # 如果遍歷完所有可能的情況都沒有找到解，輸出 "No Solution..."
    if noSolution == True:  
        print("No Solution...")  

    print()  # 輸出一個空行，格式化輸出
