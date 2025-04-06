queue = []  # 初始化一個空的佇列（Queue）
MAX_SIZE = 100  # 設定佇列的最大大小為 100

def enqueue(data):
    """ 將元素加入佇列（尾部） """
    queue.append(data)

def dequeue():
    """ 從佇列移除並返回前端（頭部）的元素 """
    data = queue.pop(0)
    return data

def isFull():
    """ 判斷佇列是否已滿 """
    if len(queue) == MAX_SIZE:
        return True
    else:
        return False

def isEmpty():
    """ 判斷佇列是否為空 """
    if len(queue) == 0:
        return True
    else:
        return False

def front():
    """ 取得佇列的前端（頭部）元素但不移除 """
    return queue[0]

def rear():
    """ 取得佇列的尾端元素但不移除 """
    return queue[len(queue)-1]

# 開始執行主程式
N = int(input())  # 讀取操作的次數

for i in range(N):
    s = input()  # 讀取一行指令
    data = [ int(x) for x in s.split() ]  # 將輸入轉換為整數列表

    if data[0] == 1:  # 指令 1：將元素加入佇列
        enqueue(data[1])

    elif data[0] == 2:  # 指令 2：輸出佇列前端的元素（若佇列為空則輸出 -1）
        if isEmpty() == True:
            print(-1)
        else:
            print(front())

    elif data[0] == 3:  # 指令 3：從佇列移除前端的元素（若非空）
        if isEmpty() == False:
            dequeue()
