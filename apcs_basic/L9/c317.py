# 持續執行直到遇到錯誤（例如 EOF 或無法轉換輸入為整數）才跳出
while True:
    try:
        # 讀取要處理的組數（例如輸入為 3，表示接下來有 3 組資料）
        s = int(input())  # 例如輸入 3

        # 對每組輸入資料進行處理
        for i in range(s):
            data_input = input()  # 例如輸入 "258 24 20"
            data = list(map(int, data_input.split()))  # 將輸入字串分割並轉為整數列表

            dollar = data[0]  # 總金額，例如 258
            coinA = data[1]   # 幣值 A，例如 24
            coinB = data[2]   # 幣值 B，例如 20

            # 嘗試用最多數量的 coinA 來湊錢
            numA = int(dollar / coinA)

            # 嘗試找到一組 coinA 和 coinB 的組合，能剛好湊出 dollar
            while numA >= 0:
                # 如果剩下的金額不能被 coinB 整除，減少一個 coinA 繼續嘗試
                if (dollar - coinA * numA) % coinB != 0:
                    numA = numA - 1
                else:
                    # 剩下的金額可以用 coinB 湊成，就跳出迴圈
                    break

            if numA >= 0:
                # 計算 coinB 的數量
                numB = int((dollar - coinA * numA) / coinB)
                total = numA + numB  # 計算總共用了多少個硬幣
                print(total)
            else:
                # 如果找不到任意組合能湊出正確金額，就輸出 -1
                print(-1)

    except:
        # 如果發生錯誤（如 EOF），就跳出 while 迴圈
        break
