#
# APCS 110/11
# P1: 修補圍籬
#

#start
n = int(input())
bar = list(map(int, input().split()))

total = 0

for i in range(1, n-1):

    if bar[i] == 0:
        L = bar[i-1]
        R = bar[i+1]

        now_h = min(L, R)
        total += now_h

#Left
if bar[0] == 0:
    total += bar[1]

#Right
if bar[n-1] == 0:
    total += bar[n-2]

print(total)
