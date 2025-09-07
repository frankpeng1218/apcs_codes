while True:
    try:
        # 讀取學生數量 N
        N = int(input())  # 範例輸入：5

        # 建立一個空清單，用來存放所有學生資料
        student = []

        # 讀取 N 筆學生資料
        for i in range(N): 
            s = input()  # 範例輸入：60547020S Wayne

            # 依空白切割字串 → ["60547020S", "Wayne"]
            si = [x for x in s.split()]

            # 加入 student 清單
            student.append(si)

        # 輸出所有學生資料
        print(student)

    except:
        # 當輸入結束或發生錯誤時，跳出迴圈
        break


# 更快的方式
while True:
    try:
        N = int(input())  # 讀取學生數量
        student = [input().split() for _ in range(N)]  # 一行就能完成
        print(student)
    except:
        break
