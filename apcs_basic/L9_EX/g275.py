#
# Frank:
# g275: 七言對聯
#
# 0: 平聲
# 1: 仄聲

import sys

# start
for s in sys.stdin:  # 從標準輸入讀入行數（用於處理多筆資料）
    n = int(s)

    for i in range(n):
        p1 = list(map(int, input().split()))  # 上聯的七個字（0 或 1，代表平聲或仄聲）
        p2 = list(map(int, input().split()))  # 下聯的七個字（0 或 1，代表平聲或仄聲）

        violation = 0  # 違規次數（若為 0，表示無違規）

        # A 規則：
        # 二、四字需不同聲調（平仄不同），且二與六需同聲調
        if p1[1] != p1[3] and p2[1] != p2[3]:
            if p1[1] == p1[5] and p2[1] == p2[5]:
                pass  # 符合規則 A
            else:
                violation += 1
                print("A", end='')  # 違反 A：二六不同
        else:
            violation += 1
            print("A", end='')  # 違反 A：二四相同

        # B 規則：
        # 上聯（p1）結尾第七字應為仄聲（1），下聯（p2）結尾第七字應為平聲（0）
        if p1[6] == 1 and p2[6] == 0:
            pass
        else:
            violation += 1
            print("B", end='')  # 違反 B：尾音不符要求

        # C 規則：
        # 對仗要求：二、四、六字平仄相對（上下加總等於 1）
        if (p1[1] + p2[1]) == 1 and (p1[3] + p2[3]) == 1 and (p1[5] + p2[5]) == 1:
            pass
        else:
            violation += 1
            print("C", end='')  # 違反 C：平仄不相對

        if violation > 0:
            print()  # 如果有違規就換行顯示違規代碼
        else:
            print("None")  # 沒有違規則輸出 "None"
