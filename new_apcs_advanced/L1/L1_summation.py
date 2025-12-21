#
# 遞迴連續和(逆向)
#

def sumX(n):
    if n<=1:
        return 1
    else:
        return sumX(n-1)+n

N = int(input())

print(sumX(N))


