import sys

#start
# 輸入：
# 一共有三個數字，並且在同一行
for s in sys.stdin:
    s = s.split()  # 將輸入字串以空格分割成列表
    
    a = int(s[0])  # 轉換第一個數字為整數
    b = int(s[1])  # 轉換第二個數字為整數
    c = int(s[2])  # 轉換第三個數字為整數

    # 計算：
    # 任意兩邊相加必須大於第三邊，符合三角形不等式定理
    if a + b > c and b + c > a and c + a > b:
        print("Yes")  # 若符合條件，輸出 "Yes"
    else:
        print("No")  # 若不符合條件，輸出 "No"
