while True:  # 持續進行迴圈直到遇到錯誤（例如輸入結束）才跳出
    try:
        # 讀取輸入的兩個整數 n 和 m
        n, m = map(int, input().split())

        ans = []          # 儲存轉換過程的結果
        boring = False    # 判斷是否為 "Boring!" 的標記

        if n == 0 or m == 0:  # 如果任一數為 0，直接判定為 "Boring!"
            boring = True
        else:
            ans.append(n)     # 把初始值 n 加入結果中
            while n > 1:
                if n % m == 0:     # 如果 n 可以被 m 整除
                    n //= m        # 就把 n 除以 m
                    ans.append(n)  # 並將結果加入 ans 中
                else:
                    boring = True  # 若不能整除，則為 "Boring!"
                    break

        if boring == True:
            print("Boring!")       # 印出 "Boring!"
        else:
            for i in ans:          # 印出 ans 中的所有數字
                print(i, end=' ')
            print()

    except:
        break  # 當遇到輸入錯誤或 EOF 時跳出迴圈
