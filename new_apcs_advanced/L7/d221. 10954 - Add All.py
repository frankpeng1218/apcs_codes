while True:
    try:
        # 讀取輸入的 N 值，代表有多少個數字
        N = int(input())
        if N == 0:  # 若 N == 0，則結束輸入
            break

        # 讀取數列並排序
        num = list(map(int, input().split()))
        num.sort()  # 初始排序，確保從最小的開始相加

        ans = 0  # 紀錄最小代價
        
        # 進行 N-1 次合併
        for i in range(N - 1):
            a = num.pop(0)  # 取出當前最小的數
            b = num.pop(0)  # 取出第二小的數

            c = a + b  # 計算兩數之和
            ans += c  # 累加代價

            num.append(c)  # 將新數放回數列
            num.sort()  # 重新排序，確保下次選擇最小的數
            
        print(ans)  # 輸出最小代價

    except:
        break  # 捕捉輸入錯誤或 EOF，然後跳出迴圈
