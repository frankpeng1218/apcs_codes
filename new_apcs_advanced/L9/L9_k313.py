#
# k313: 行李超重
#
import sys
'''
input = sys.stdin.read
data = input().split()
n = int(data[0])
t = int(data[1])
v = int(data[2])
'''
n, t, v = map(int, input().split())

w = []
l = []
sumW = 0
sumL = 0

index = 3
for i in range(n):
    t1, t2 = map(int, input().split())
    #w.append(int(data[index]))
    #l.append(int(data[index + 1]))
    w.append(t1)
    l.append(t2)
    sumW += w[i]
    sumL += l[i]
    index += 2

dp = [0] * (sumW + 1)

for i in range(n):
    for j in range(sumW, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + l[i])

ans = 999999

for j in range(t, sumW + 1):
    ans = min(ans, (j - t) * v + (sumL - dp[j]))

if t >= sumW:
    ans = 0

print(ans)
