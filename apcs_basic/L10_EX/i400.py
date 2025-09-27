# i400. 2. 字串解碼

# step2：根據 ei 的每一位是 0 或 1 來改變 T 的順序
def step2(T, ei, n):
    tString = ""
    T = list(T)
    for dx in range(n-1, -1, -1):  # 反向遍歷 ei
        if ei[dx] == "0":
            # 如果是 0，將 T 的最後一個字元加到 tString 的前面
            tString = T[-1] + tString
        else:
            # 如果是 1，將 T 的最後一個字元加到 tString 的後面
            tString = tString + T[-1]
        T.pop()  # 移除已使用的最後一個字元
    return tString

# step1：根據 ei 的 '1' 個數是否為奇數來決定是否要交換 T 的前後段
def step1(T, ei, n):
    checkE = 0
    for i in ei:
        if i == "1":
            checkE += 1
    if checkE % 2 == 0:
        return T  # 偶數就不變
    else:
        if n % 2 == 0:  # 偶數長度字串
            T1 = T[0:n//2]     # 前半
            T2 = T[n//2:n]     # 後半
            return T2 + T1     # 後半接前半
        else:  # 奇數長度字串
            T1 = T[0:n//2]     # 前段
            mid = T[n//2]      # 中間一個字元
            T2 = T[n//2+1:n]   # 後段
            return T2 + mid + T1  # 後段 + 中間 + 前段

# 主程式：不斷讀取資料直到輸入結束
while True:
    try:
        m, n = map(int, input().split())  # m 次操作，每次長度為 n 的控制字串
        e = []
        for i in range(m):
            e.append(list(input()))  # 每個 ei 是 n 位元的控制字串（由 '0' 和 '1' 組成）
        T = input()  # 被加密的字串
        temp = T
        # 從最後一組控制字元往前還原
        for i in range(m-1, -1, -1):
            temp = step2(temp, e[i], n)
            temp = step1(temp, e[i], n)
        print(temp)
    except:
        break  # 若無輸入或發生例外則跳出
