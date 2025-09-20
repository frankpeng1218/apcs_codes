# 讀取兩個整數 N 和 M（N 表示測資筆數，M 在此程式中未使用）
N, M = map(int, input().split())

# 進行 N 筆測試資料的處理
for i in range(N):
    result = 0  # 用來記錄每筆資料中出現相同數字的次數（即重複的數字個數）

    # 讀取兩列數字字串，通常每列有 M 個數字
    data1 = input()
    data2 = input()

    # 將兩列資料合併成一列字串（用空格隔開）
    data = data1 + " " + data2  # 例如：data = "1 5 6 8 9 13 3 4 5 7 8 11"

    # 將字串拆解成整數清單
    seq = list(map(int, data.split()))

    # 將清單中的數字排序，以便找出相鄰且相同的數字（即重複出現的數字）
    seq.sort()

    # 檢查有多少個相鄰元素是相同的（也就是重複的數字）
    for x in range(len(seq)-1):
        if seq[x] == seq[x+1]:
            result += 1  # 如果當前元素與下一個元素相同，計數器加一

    # 輸出該筆資料中重複數字的出現次數
    print(result)
