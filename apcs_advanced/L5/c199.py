while True:
    try:
        # 讀取輸入的高度列表
        heights = list(map(int, input().split()))  # 第一個數為山的總數，其餘為每分鐘的高度紀錄

        n = heights[0]  # 總高度紀錄數量
        heights.pop(0)  # 移除第一個數字，剩下的是每分鐘的高度紀錄

        peak_count = 0  # 記錄小山頭的數量

        # 遍歷高度紀錄，從第二個位置到倒數第二個位置檢查小山頭
        for i in range(1, n - 1):
            left = heights[i - 1]  # 當前高度的左側高度
            current = heights[i]  # 當前高度
            right = heights[i + 1]  # 當前高度的右側高度

            # 條件 1: 確認是否是標準小山頭
            if current > left and current > right:
                peak_count += 1

            # 條件 2: 處理水平延伸的小山頭
            if current > left and current == right:
                t = i + 1  # 指標指向右邊相同高度的下一個位置
                value = heights[t]  # 目前延伸高度的值

                # 向右延伸直到找到不等於當前高度的點
                while value == current:
                    t += 1
                    if t == n:  # 避免超過範圍
                        t -= 1
                        break
                    value = heights[t]

                # 如果延伸結束後右側高度比當前高度低，則計算為小山頭
                if heights[t] < current:
                    peak_count += 1

        # 輸出結果，小山頭的數量
        print(peak_count)
    except:
        break  # 結束輸入時退出程式
