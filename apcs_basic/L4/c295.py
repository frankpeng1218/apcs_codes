while True:  # 無限迴圈，用於持續讀取輸入直到發生例外或中斷
    try:
        # 讀取輸入並分成兩個值
        input_line = input().split()
        n = int(input_line[0])  # 將第一個值轉為整數 n（代表有 n 群數據）
        m_unused = int(input_line[1])  # 第二個值不會用到（但仍需讀取以符合輸入格式）

        m = []  # 用來存放每一群數據的列表
        for i in range(n):  # 讀取 n 行數據
            input_line = input().split()  # 讀取一行輸入
            v = [int(x) for x in input_line]  # 將每個值轉為整數
            v.sort(reverse=True)  # 將該組數據降序排序（從大到小）
            m.append(v)  # 將排序後的數據加入 m 清單

        # 計算總和
        total_sum = 0  # 初始化總和變數
        for v in m:  # 遍歷每組數據
            total_sum += v[0]  # 取每組的最大值並累加

        print(total_sum)  # 輸出總和

        flag = 0  # 用來標記是否有符合條件的數字
        for v in m:  # 遍歷每組數據
            max_value = v[0]  # 取得該組的最大值
            if total_sum % max_value == 0:  # 如果總和可以被該最大值整除
                if flag == 0:  # 如果是第一次找到符合條件的數字
                    print(max_value, end='')  # 直接輸出，不換行
                else:  # 如果不是第一次
                    print('', max_value, end='')  # 在前面加上空格
                flag = 1  # 設定標記，表示找到符合條件的數字

        if flag == 0:  # 如果沒有找到任何符合條件的數字
            print(-1)  # 輸出 -1

    except:  # 捕捉輸入錯誤或異常（如 EOF）
        break  # 結束迴圈
