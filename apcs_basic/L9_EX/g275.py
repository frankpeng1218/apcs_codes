#
# g275: 七言對聯檢查
#
# 0: 平聲
# 1: 仄聲
#

# 讀取測資組數
n = int(input())

for i in range(n):
    # 讀入上聯 7 個字的平仄，存成整數 list
    p1 = list(map(int, input().split()))
    # 讀入下聯 7 個字的平仄，存成整數 list
    p2 = list(map(int, input().split()))

    violation = 0   # 記錄違規次數
    
    # 規則 A: 偶數位置 (第2字、第4字) 不同，且檢查第2字與第6字是否相同
    if p1[1] != p1[3] and p2[1] != p2[3]:
        if p1[1] == p1[5] and p2[1] == p2[5]:
            pass  # 符合條件，不違規
        else:
            violation += 1
            print("A", end='')  # 違反規則 A
    else:
        violation += 1
        print("A", end='')      # 違反規則 A
    
    # 規則 B: 上聯最後一字為仄聲，下聯最後一字為平聲
    if p1[6] == 1 and p2[6] == 0:
        pass
    else:
        violation += 1
        print("B", end='')      # 違反規則 B
    
    # 規則 C: 對應的第2、4、6字，必須一平一仄 (和為 1)
    if (p1[1]+p2[1]) == 1 and (p1[3]+p2[3]) == 1 and (p1[5]+p2[5]) == 1:
        pass
    else:
        violation += 1
        print("C", end='')      # 違反規則 C
    
    # 如果有違規則印換行，否則印 "None"
    if violation > 0:
        print()
    else:
        print("None")
