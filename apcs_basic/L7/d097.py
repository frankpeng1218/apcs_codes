while True:
    try:
        # 讀取一行輸入並轉換成整數列表
        nums = list(map(int, input().split()))
        
        # 第一個數字為總數 n，移除後續只留下元素差值部分
        n = nums[0]
        nums.pop(0)

        # 初始化一個長度為 n 的列表來記錄各差值出現的次數
        delta = [0 for x in range(n)]

        # 計算相鄰兩數的絕對差，並在對應的位置累加
        for i in range(1, n):
            d = abs(nums[i] - nums[i-1])
            if d <= n - 1:
                delta[d] += 1

        # 判斷是否為 Jolly Jumper：差值從 1 到 n-1 每個都剛好出現一次
        isJolly = True
        for i in range(1, n):
            if delta[i] != 1:
                isJolly = False
                break

        # 輸出結果
        if isJolly == True:
            print("Jolly")
        else:
            print("Not jolly")
    except:
        # 若遇到 EOF 或其他錯誤則跳出迴圈
        break
