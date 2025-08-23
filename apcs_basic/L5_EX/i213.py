#
# i213: stack 練習
#

stack = []  # 初始化一個空的堆疊（stack）

def push(data):
    """ 將元素推入堆疊 """
    stack.append(data)

def pop():
    """ 從堆疊彈出頂部元素並返回 """
    r = stack.pop()
    return r

def top():
    """ 取得堆疊的頂部元素但不移除 """
    now_size = len(stack)
    t = stack[now_size - 1]
    return t

def size():
    """ 輸出堆疊的當前大小 """
    print(len(stack))

def empty():
    """ 判斷堆疊是否為空 """
    if len(stack) == 0:
        return True
    else:
        return False

# 開始執行堆疊操作
N = int(input())  # 讀取操作數量

for i in range(N):
    row = list(map(int, input().split()))  # 讀取一行輸入，轉換為整數列表

    if len(row) == 1:  
        k = row[0]  # 單個數字時，表示查詢或彈出
    else:
        k = row[0]  # 第一個數字代表操作類型
        d = row[1]  # 第二個數字為要推入的數據

    if k == 1:
        push(d)  # 推入數據 d 到堆疊
    elif k == 2:
        if empty():  
            print(-1)  # 如果堆疊為空，輸出 -1
        else:
            print(top())  # 輸出堆疊頂部元素
    elif k == 3:
        if not empty():  
            pop()  # 如果堆疊非空，彈出頂部元素
