while True:  
    try:
        # 讀取輸入的數字 N，表示有 N 張牌
        N = int(input())  # 範例輸入：3

        # 讀取輸入的牌資料（花色 + 數字 交錯）
        s = input()  # 範例輸入：S 1 H 9 D 9

        # 將字串依空白切割成清單
        # 範例：["S", "1", "H", "9", "D", "9"]
        data = s.split()

        # 建立一個空的 stack，用來存放牌組合後的結果
        stack = []

        # 使用 i 當索引，初始值為 0
        i = 0

        # 迴圈條件：i 必須小於 2*N
        # 因為每張牌需要兩個元素（花色 + 數字）
        # 所以 N 張牌總共會有 2*N 個輸入
        while i < 2 * N:
            # 將花色與數字組合成一張牌
            card = data[i] + data[i+1]  # 例如： "S" + "1" → "S1"

            # 印出當前的牌
            print(card)

            # 將牌放入 stack
            stack.append(card)

            # 每次處理完一張牌，要跳過 2 個元素
            i += 2

        # 最後輸出完整的 stack（所有牌的列表）
        print(stack)

    except:
        # 如果輸入結束（例如 Ctrl+D），或輸入錯誤，結束程式
        break
