year = int(input())  # 讀取使用者輸入的年份並轉換為整數

# 判斷是否為閏年
if year % 400 == 0:  # 若年份能被 400 整除，則為閏年
    print("Yes")
else:
    if year % 4 == 0 and year % 100 != 0:  # 若年份能被 4 整除但不能被 100 整除，則為閏年
        print("Yes")
    else:  # 其他情況皆為平年
        print("No")
