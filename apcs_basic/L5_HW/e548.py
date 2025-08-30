#
# e548: 11995 - I Can Guess the Data Structure!
#

while True:
    try:
        s = []  # stack (堆疊)
        q = []  # queue (佇列)
        pq = [] # priority queue (優先佇列)

        isQueue = True       # 判斷是否可能是佇列
        isPQueue = True      # 判斷是否可能是優先佇列
        isStack = True       # 判斷是否可能是堆疊

        n = int(input())  # 讀取操作次數

        for _ in range(n):
            op, x = map(int, input().split())  # 讀取操作類型 (op) 和數值 (x)

            if op == 1:  # 插入操作
                s.append(x)  # 堆疊：後進先出
                q.append(x)  # 佇列：先進先出
                pq.append(x) # 優先佇列：取最大值優先

            elif op == 2:  # 移除操作
                
                if isQueue:  # 檢查是否仍然可能是佇列
                    if len(q) != 0 and q[0] == x:
                        q.pop(0)  # 佇列：從前端移除
                    else:
                        isQueue = False  # 若無法匹配，則不可能是佇列
                
                if isPQueue:  # 檢查是否仍然可能是優先佇列
                    if len(pq) != 0:
                        item = max(pq)  # 優先佇列應該刪除最大值
                        idx = pq.index(item)
                        if pq[idx] == x:
                            pq.pop(idx)
                        else:
                            isPQueue = False  # 若無法匹配，則不可能是優先佇列
                    else:
                        isPQueue = False
                
                if isStack:  # 檢查是否仍然可能是堆疊
                    if len(s) != 0 and (s[-1] == x):
                        s.pop()  # 堆疊：從頂部移除
                    else:
                        isStack = False  # 若無法匹配，則不可能是堆疊
        
        # 判斷結果
        if (isQueue and isStack) or (isQueue and isPQueue) or (isPQueue and isStack):
            print("not sure")  # 若多種可能性存在
        elif isQueue:
            print("queue")  # 若只有佇列符合
        elif isPQueue:
            print("priority queue")  # 若只有優先佇列符合
        elif isStack:
            print("stack")  # 若只有堆疊符合
        else:
            print("impossible")  # 若無任何資料結構符合

    except:
        break  # 讀取輸入結束時跳出迴圈
