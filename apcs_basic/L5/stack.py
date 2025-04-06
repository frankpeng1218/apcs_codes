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

# 開始測試堆疊功能
print(stack)  # 輸出初始的堆疊狀態（應為空列表）
push("a")  # 推入 "a"
push("b")  # 推入 "b"
push("c")  # 推入 "c"
pop()      # 彈出頂部元素 "c"
push("d")  # 推入 "d"
size()     # 輸出當前堆疊大小
print(stack)  # 輸出最終堆疊內容
