#e283. APCS 類似題 - 小崴的特殊編碼

import sys

letter = {"0 1 0 1": "A",
          "0 1 1 1": "B",
          "0 0 1 0": "C",
          "1 1 0 1": "D",
          "1 0 0 0": "E",
          "1 1 0 0": "F"}

##while True:
##    try:
##        n = int(input())
##        ans = ""
##        for _ in range(n):
##            s = input()
##            ans += letter[s]
##        print(ans)
##    except:
##        break

for i in sys.stdin:
    n = int(i)
    ans = ""
    for _ in range(n):
        # input() ≈ sys.stdin.readline().strip()
        # s = input()
        s = sys.stdin.readline().strip()
        ans += letter[s]
    print(ans)











