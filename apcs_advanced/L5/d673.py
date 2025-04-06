case_number = 1  # 用於紀錄案例編號

while True:
    # 讀取初始庫存問題數量
    initial_problems = int(input())
    if initial_problems == -1:  # 如果輸入為 -1，表示結束程式
        break

    # 第二行輸入，每個月新增的問題數量，共 12 個
    monthly_production = list(map(int, input().split()))  # 每月新增的問題數量

    # 第三行輸入，每個月需要解決的問題數量，共 12 個
    monthly_demand = list(map(int, input().split()))  # 每月需要的問題數量

    # 輸出當前案例標題
    print("Case " + str(case_number) + ":")

    current_inventory = initial_problems  # 當前的問題庫存量
    for month in range(0, 12):  # 遍歷 12 個月份
        if month == 0:  # 第一個月特殊處理
            if current_inventory >= monthly_demand[month]:  # 問題庫存足夠滿足當月需求
                print("No problem! :D")  # 輸出「沒有問題！」
                current_inventory -= monthly_demand[month]  # 減去已解決的問題數量
            else:  # 問題庫存不足
                print("No problem. :(")  # 輸出「有問題」
        else:  # 從第二個月開始
            current_inventory += monthly_production[month - 1]  # 增加上一個月生產的問題數量
            if current_inventory >= monthly_demand[month]:  # 如果當前問題庫存足夠
                print("No problem! :D")  # 輸出「沒有問題！」
                current_inventory -= monthly_demand[month]  # 減去已解決的問題數量
            else:  # 問題庫存不足
                print("No problem. :(")  # 輸出「有問題」

    case_number += 1  # 案例編號增加
