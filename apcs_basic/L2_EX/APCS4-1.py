#start

x = True  # 定義布林值變數 x，設為 True
y = False  # 定義布林值變數 y，設為 False

a = x and y  # 布林運算：x 和 y 進行 AND 運算，結果為 False

b = 11  # 定義整數變數 b，設為 11
c = 5.5  # 定義浮點數變數 c，設為 5.5

d = b < c  # 比較運算：判斷 b 是否小於 c，結果為 False
e = b >= c * 2  # 比較運算：判斷 b 是否大於等於 c 乘以 2，結果為 False

print(type(a))  # 輸出變數 a 的資料型態（bool）
print(type(b))  # 輸出變數 b 的資料型態（int）
print(type(c))  # 輸出變數 c 的資料型態（float）
print(d)  # 輸出變數 d 的值（False）
print(e)  # 輸出變數 e 的值（False）
