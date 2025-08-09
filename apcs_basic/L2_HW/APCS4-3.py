import sys

#start
for s in sys.stdin:  # 逐行讀取標準輸入
    num = int(s)  # 將輸入的字串轉換為整數 num

    if num % 2 == 0:  # 判斷 num 是否為偶數
        print("even")  # 若是偶數，輸出 "even"
    else:
        print("odd")  # 若是奇數，輸出 "odd"
