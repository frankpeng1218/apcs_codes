import sys  # 匯入 sys 模組，允許從標準輸入讀取資料

#start
student = [4, 3, 2, 1]  # 初始化學生編號列表

for s in sys.stdin:
    op = s.split()  # 讀取輸入並拆分為指令列表

    if op[0] == "1":  
        print(len(student))  # 輸出學生數量
    elif op[0] == "2":  
        student.append(int(op[1]))  # 將新學生編號加入列表
        print(student)  # 輸出更新後的列表
    elif op[0] == "3":  
        student.remove(int(op[1]))  # 從列表中移除指定的學生編號
        print(student)  # 輸出更新後的列表
    elif op[0] == "4":  
        student.sort()  # 將學生編號進行排序
        print(student)  # 輸出排序後的列表
