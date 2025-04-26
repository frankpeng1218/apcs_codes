while True:
    try:
        #start

        # 讀取一個整數 N，代表卡牌的對數（總共有 2*N 個資料）
        N = int(input())

        # 讀取一行字串，包含 2*N 個代表卡牌的字元
        s = input()

        # 將字串以空格分割成一個列表
        data = s.split()

        # 初始化一個空的 stack 用來存卡牌
        stack = []

        i = 0
        # 將每兩個字元組成一張卡牌，直到 2*N 個字元處理完
        while i < 2 * N:
            card = data[i] + data[i + 1]  # 將相鄰的兩個字元合併為一張卡
            # print(card)  # 可取消註解來檢查每張卡內容
            stack.append(card)           # 將卡牌放入堆疊中
            i += 2                        # 一次跳兩個，處理下一對字元

        # 輸出所有卡牌的列表
        print(stack)

    except:
        break  # 如果發生例外（如輸入結束），跳出迴圈
