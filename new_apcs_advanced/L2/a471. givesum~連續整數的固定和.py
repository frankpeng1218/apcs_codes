while True:  # 不斷讀取輸入，直到發生例外（例如 EOF）
    try:
        N = int(input())  # 讀入一個整數 N
        noSolution = True  # 標記是否尚未找到解

        # 嘗試所有可能的起始值 i
        for i in range(0, N):
            sum_ = 0  # 用來累加連續整數的總和

            # 從 i 開始，連續加到 j
            for j in range(i, N):
                sum_ += j  # 將 j 加入目前的總和

                # 如果連續整數的總和等於 N
                if sum_ == N:
                    print(f"{i}-{j}")  # 輸出起始與結束值
                    noSolution = False  # 表示已找到至少一組解
                    break  # 結束內層迴圈（固定 i 不再往下加）

        # 如果所有情況都試過仍沒有解
        if noSolution == True:
            print("No Solution...")

        print()  # 輸出一行空白，分隔不同測資的結果

    except:
        break  # 當沒有輸入或發生錯誤時，結束整個程式
