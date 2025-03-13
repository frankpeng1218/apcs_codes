import sys

#start
T = int(input())  # 讀取標準輸入，將其轉換為整數 T（及格分數）

for s in sys.stdin:  # 逐行讀取標準輸入
    score = int(s)  # 將輸入的字串轉換為整數 score

    if score >= T:  # 判斷分數是否大於或等於及格分數 T
        print("pass")  # 若符合條件，輸出 "pass"
    else:
        print("fail")  # 若不符合條件，輸出 "fail"
