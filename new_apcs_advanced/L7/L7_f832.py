#
# f832: 隕石
#

#start
n, m = map(int, input().split())

w = list(map(int, input().split()))
c = list(map(int, input().split()))

w.sort(reverse=True)
c.sort(reverse=True)

meteor, catcher = 0, 0

total_weight = 0

while meteor!=n and catcher !=m:
    if w[meteor] <= c[catcher]:
        total_weight += w[meteor]

        meteor += 1
        catcher += 1

    else:
        meteor += 1

print(total_weight)
