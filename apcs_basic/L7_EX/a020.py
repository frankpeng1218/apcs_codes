# 將身分證字號的英文字母轉換為對應的數字代碼
def translateCode(letter):
    CODE = {
        'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34,
        'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'O':35, 'P':23, 'Q':24, 'R':25,
        'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33
    }
    return CODE[letter]


id_number = list(input())  
# 例如輸入 "T112663836" -> ["T", "1", "1", "2", "6", "6", "3", "8", "3", "6"]

# 取出第一個字母並轉換成數字代碼
area_code = translateCode(id_number[0])   # "T" -> 27

# 身分證檢查公式的第一部分：字母代碼拆成十位數與個位數計算
x1 = area_code // 10          # 十位數
x2 = (area_code % 10) * 9     # 個位數 × 9

# 計算從第 2 碼到第 9 碼（數字）的加權總和
# 權重依序為 8, 7, 6, 5, 4, 3, 2, 1
body_sum = 0
for i in range(1, 9):  
    body_sum += int(id_number[i]) * (9 - i)

# 取出最後一碼（檢查碼）
check_digit = int(id_number[9])

# 驗證公式
verify_code = (x1 + x2 + body_sum + check_digit) % 10

# 判斷是否為合法的身分證字號
if verify_code == 0:
    print("real")   # 合法
else:
    print("fake")   # 不合法
