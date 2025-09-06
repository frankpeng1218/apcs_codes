while True:
    try:
        #start

        # 讀取一個整數 N，代表學生人數
        N = int(input())

        # 建立空的列表 student，用來儲存每位學生的資料
        student = []

        # 重複 N 次，讀取每位學生的資料
        for i in range(N):
            s = input()                       # 讀取一行學生資料
            si = [ x for x in s.split()]      # 將資料以空白分割成多個欄位（例如名字、成績等）
            student.append(si)                # 將這筆學生資料加到 student 列表中

        # 印出學生資料的二維列表
        print(student)

    except:
        break  # 若發生例外（例如輸入結束），就跳出 while 迴圈
