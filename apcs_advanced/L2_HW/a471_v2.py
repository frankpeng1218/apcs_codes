import math  # 匯入 math 模組，用於計算平方根
import sys  # 匯入 sys 模組，用於讀取標準輸入


# 關鍵是找出a和n
# 2. 數列和公式的解法
# Sn = [n/2*(2a+n-1)*d], Sn(數列和), d(公差) = 1, a(首項), n(連續數列的長度)
# 因為d = 1 -> Sn = [n/2*(2a+n-1)]
# -> 2Sn = [n*(2a+n-1)]

# 第一個條件n 的範圍: 由上面的式子可得2<=n<=sqrt(2Sn), n一定至少是2
# 第一個條件: 2Sn/n要能被整除-> 2*Sn%n == 0
# 第二個條件: Sn = [n/2*(2a+n-1)]-> a = [2Sn/n-(n-1)]/2-> [2Sn/n-(n-1)]%2 == 0

# 透過標準輸入讀取數值
for s in sys.stdin:
    Sn = int(s)  # 轉換輸入為整數 Sn，代表目標數值

    noSolution = True  # 設定變數來追蹤是否找到解
    output = []  # 用於儲存所有找到的解

    # 遍歷可能的 n 值 (數列長度)，範圍從 2 到 sqrt(2*Sn)
    # 因為等差數列求和公式 S = n * (2a + (n - 1)) / 2 轉換為 2S = n * (2a + n - 1)
    # 可知 2Sn 必須能被 n 整除
    for n in range(2, int(math.sqrt(2 * Sn)) + 1): # 因為range會漏掉所以要+1
        if (2 * Sn) % n == 0:  # 檢查 2Sn 是否能被 n 整除
            if (2 * Sn / n - n + 1) % 2 == 0:  # 確保 (2Sn/n - n + 1) 是偶數，才能確保 a 是整數
                a = (2 * Sn / n - n + 1) / 2  # 計算首項 a
                noSolution = False  # 設定為 False，表示至少找到一組解

                if a <= 0:  # a是由Sn和n推導出來該次迴圈的唯一解, 有可能會有<=0的情況, 但是0<a, 所以要排除, 要直接break for迴圈, 因為n只會越來越大, a若有其他迴圈獲得的解也只會越來閱小
                    break
                else:
                    end = a + n - 1  # 計算數列的結尾數字
                    tmp = str(int(a)) + "-" + str(int(end))  # 格式化輸出
                    output.append(tmp)  # 將結果存入陣列

    # 如果遍歷完所有可能的情況都沒有找到解，輸出 "No Solution..."
    if noSolution:
        print("No Solution...")
    else:
        # 逆序輸出所有找到的解，因為較大的數列長度的解應該先顯示, 因為我們是從n=2開始跑for 迴圈
        for i in range(len(output) - 1, -1, -1):
            print(output[i])

    print()  # 輸出一個空行，格式化輸出
