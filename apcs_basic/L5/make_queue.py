queue = []  # 初始化一個空的佇列（queue）
MAX_SIZE = 10  # 設定佇列的最大容量

def enqueue(data):
    """ 將元素加入佇列的尾端 """
    queue.append(data)

def dequeue():
    """ 移除佇列的前端元素並返回 """
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
    """ 取得佇列的前端元素（不移除） """
    return queue[0]

def rear():
    """ 取得佇列的尾端元素（不移除） """
    return queue[len(queue) - 1]

# 開始測試佇列功能
for i in range(5):
    if not isFull():  # 若佇列未滿，則插入元素
        enqueue(i)
    else:
        print("Queue is full, can't add item.")  # 若佇列已滿，則輸出提示訊息

print(queue)  # 輸出當前佇列狀態

for j in range(6):
    if not isEmpty():  # 若佇列非空，則取出元素
        print(dequeue(), queue)  # 彈出佇列前端元素，並輸出當前佇列狀態
    else:
        print("Queue is empty, can't pop item.")  # 若佇列為空，則輸出提示訊息
