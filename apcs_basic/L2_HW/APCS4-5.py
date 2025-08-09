score = int(input())  # 讀取使用者輸入的分數並轉換為整數

if score >= 80:  # 若分數大於等於 80
    print("A")  # 輸出 "A"
elif 60 <= score <= 79:  # 若分數介於 60 到 79 之間（包含 60）
    print("B")  # 輸出 "B"
else:  # 若分數小於 60
    print("C")  # 輸出 "C"
