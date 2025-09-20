# 讀入兩個整數 N 和 M，N 表示有幾組資料，M 表示每組資料內的數字個數
N, M = map(int, input().split())

# 處理 N 組資料
for i in range(N):
    result = 0  # 用來計算每組中有多少數字是相同的

    # 讀入第一組資料，包含 M 個整數
    data1 = list(map(int, input().split()))

    # 讀入第二組資料，包含 M 個整數
    data2 = list(map(int, input().split()))

    # 開始比對兩組資料中相同的數字
    for number in data1:
        if number in data2:  # 如果第一組的數字在第二組中也出現
            result += 1   # 則相同數字的計數加一

    # 輸出這一組中有幾個相同的數字
    print(result)
