#f149. 3. 炸彈偵測器
import sys

# 定義函數，用來顯示地圖（用於除錯）
def showmap(m, r, c):
    for i in range(0, r):  # 遍歷每一列
        for j in range(0, c):  # 遍歷每一行
            print(m[i][j], end=' ')  # 顯示當前格子的值，空格分隔
        print()  # 換行

#start
size = list(map(int, input().split()))
R = size[0]
C = size[1]

MAP = []  # 初始化一個空列表來存儲地圖數據

# 從標準輸入中逐行讀取地圖數據
r = 0
for s in sys.stdin:
    row = list(map(int, s.split()))  # 將每一行轉換為整數列表
    MAP.append(row)  # 將該行加入地圖列表中
    r += 1
    if r >= R:  # 如果已經讀取了 R 行，則停止讀取
        break

# 初始化變數來記錄已偵測到和未偵測到的炸彈數量
detected = 0
undetected = 0

# 開始偵測炸彈
for i in range(0, R):  # 遍歷地圖的每一行
    for j in range(0, C):  # 遍歷地圖的每一列

        # 如果當前格子不是空地（0）或炸彈（1），則視為偵測器
        if MAP[i][j] != 0 and MAP[i][j] != 1:  # 偵測器的標記值為 >= 5

            for n in range(i - 1, (i + 1) + 1):  # 偵測器上下的行
                for m in range(j - 1, (j + 1) + 1):  # 偵測器左右的列
                    # 確保不越界，並排除檢查到自己的位置
                    if m >= 0 and m < C and n >= 0 and n < R and not (m == j and n == i):
                        # 如果發現相鄰格子也是偵測器，則設為已偵測（6）
                        if MAP[n][m] >= 5:
                            MAP[n][m] = 6  # 標記為已偵測
                            MAP[i][j] = 6  # 標記當前偵測器為已偵測


            # 如果當前位置是偵測器，則檢查周圍是否有炸彈
            if MAP[i][j] == 5:
                for n in range(i - 1, (i + 1) + 1):  # 偵測器上下的行
                    for m in range(j - 1, (j + 1) + 1):  # 偵測器左右的列
                        if m >= 0 and m < C and n >= 0 and n < R:  # 確保不越界
                            if MAP[n][m] == 1:  # 如果找到炸彈
                                detected += 1  # 已偵測炸彈數 +1
                                MAP[n][m] = 0  # 移除炸彈標記，避免重複計算

# 統計未偵測到的炸彈數量
for i in range(0, R):  # 遍歷每一行
    for j in range(0, C):  # 遍歷每一列
        if MAP[i][j] == 1:  # 如果格子是炸彈
            undetected += 1  # 未偵測炸彈數 +1

# 輸出結果
print(detected, undetected)  # 分別輸出已偵測和未偵測到的炸彈數量

