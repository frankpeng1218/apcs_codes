# 開始程式執行

T = int(input())  # 讀取測試案例數量

symbol = ['(', '[', '<', '{', ')', ']', '>', '}']  # 定義括號類型與對應的關係

for i in range(T):
    data = input()  # 讀取一行括號字串

    stack = []  # 初始化堆疊來存儲括號

    for i in range(len(data)):
        # 當堆疊為空時，直接將當前字元加入
        if not stack:
            stack.append(data[i])
        else:
            # 檢查當前字元是否與堆疊頂端的字元匹配
            if (symbol.index(data[i]) - 4) == symbol.index(stack[-1]):  
                stack.pop()  # 若匹配則移除堆疊頂端元素
            else:
                stack.append(data[i])  # 否則將當前字元加入堆疊

        # print(stack)  # 可選的除錯輸出

    # 若最終堆疊為空，表示括號匹配正確，輸出 "Y"
    if not stack:
        print("Y")
    else:
        print("N")  # 若堆疊非空，則括號未匹配正確，輸出 "N"
