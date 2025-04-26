# 定義求最大公因數（GCD）的函式，使用輾轉相減法（輾轉相除法的變形）
def GCD(a, b):
    if a == b:
        return a  # 若 a 與 b 相等，最大公因數即為其本身

    # 如果 b > a，就交換 a 和 b 的值，確保 a > b
    if b > a:
        temp = a
        a = b
        b = temp
        # 也可以用簡潔寫法：a, b = b, a

    # 計算 a 與 b 的差，並遞迴呼叫 GCD
    c = a - b
    return GCD(b, c)


#start

# 讀取一行輸入並以空格切割，再將每個值轉換成整數
s = input()
data = list(map(int, s.split()))

# 計算輸入中前兩個數的最大公因數
result = GCD(data[0], data[1])

# 輸出結果
print(result)
