# 定義求最大公因數（GCD）的函式，使用歐幾里得算法（輾轉相除法）
def GCD(a, b):
    while True:
        # 確保 a 大於 b，若不滿足則交換 a 和 b
        if a < b:
            a, b = b, a
        
        # 如果 b 不為 0，則進行取餘數計算
        if b != 0:
            c = int(a % b)  # 取得餘數
            a = b           # 更新 a 為 b
            b = c           # 更新 b 為餘數
        else:
            break  # 當 b 為 0 時，跳出循環，a 即為最大公因數
    
    # 若滿足 break 條件，則 a 經過調整後會是最大公因數
    return a


#start

# 讀取一行輸入並以空格分割，將兩個數字轉換為整數
s = input()
data = s.split()

a = int(data[0])  # 第一個數字
b = int(data[1])  # 第二個數字

# 計算最大公因數
r = GCD(a, b)

# 輸出結果
print(r)
