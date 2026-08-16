#
# 遞迴連續和(順向)
#

def sumX(s, n): # n=5, s=1 從1開始連加
    if s<n:
        return sumX(s+1, n)+s
    else:
        return n

N = int(input())

print(sumX(1, N))


