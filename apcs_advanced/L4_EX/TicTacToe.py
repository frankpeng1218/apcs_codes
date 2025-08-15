while True:  # 無限迴圈，持續接收輸入，直到發生例外 (如 EOF)
    try:
        # 讀取測試案例的數量 N
        N = int(input())

        # 逐一處理每個測試案例
        for idx in range(N):
            arr = []  # 用於存放 3x3 井字棋盤的二維陣列

            # 讀取 3 行輸入，每行包含 3 個數字 (0 或 1)，代表井字棋盤的狀態
            for i in range(3):
                row = list(map(int, input().split()))  # 讀取一行並轉換為整數列表
                arr.append(row)  # 將該行加入棋盤陣列

            isWin = False  # 初始化變數，表示是否有玩家獲勝

            # 檢查橫排 (行) 是否有三個相同的數字 (0 或 1)
            for i in range(3):  # 遍歷 3 行
                if arr[i][0] == arr[i][1] == arr[i][2] == 0:  # 若該行全為 0
                    isWin = True
                    print("Player1 win")  # Player1 (代表 0) 獲勝
                elif arr[i][0] == arr[i][1] == arr[i][2] == 1:  # 若該行全為 1
                    isWin = True
                    print("Player2 win")  # Player2 (代表 1) 獲勝

            # 檢查直排 (列) 是否有三個相同的數字 (0 或 1)
            for j in range(3):  # 遍歷 3 列
                if arr[0][j] == arr[1][j] == arr[2][j] == 0:  # 若該列全為 0
                    isWin = True
                    print("Player1 win")  # Player1 獲勝
                elif arr[0][j] == arr[1][j] == arr[2][j] == 1:  # 若該列全為 1
                    isWin = True
                    print("Player2 win")  # Player2 獲勝

            # 檢查左上到右下的對角線
            if arr[0][0] == arr[1][1] == arr[2][2] == 0:  # 若對角線全為 0
                isWin = True
                print("Player1 win")  # Player1 獲勝
            if arr[0][0] == arr[1][1] == arr[2][2] == 1:  # 若對角線全為 1
                isWin = True
                print("Player2 win")  # Player2 獲勝
            
            # 檢查右上到左下的對角線
            if arr[0][2] == arr[1][1] == arr[2][0] == 0:  # 若對角線全為 0
                isWin = True
                print("Player1 win")  # Player1 獲勝
            if arr[0][2] == arr[1][1] == arr[2][0] == 1:  # 若對角線全為 1
                isWin = True
                print("Player2 win")  # Player2 獲勝

            # 如果沒有玩家贏，則判定為平局
            if not isWin:
                print("draw")

    except:
        break  # 當發生例外 (如 EOF，無輸入時)，跳出迴圈，結束程式
