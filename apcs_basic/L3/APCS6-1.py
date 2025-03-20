# start

# 定義銀行帳戶餘額列表
bank = [50000, 30000, 120000]  

# 將列表中的值分別存入變數 a, b, c
a = bank[0]  
b = bank[1]  
c = bank[2]  

# 計算 1% 的利息後更新帳戶餘額
bank[0] = a * 1.01  
bank[1] = b * 1.01  
bank[2] = c * 1.01  

# 輸出更新後的銀行帳戶餘額
print(bank)
