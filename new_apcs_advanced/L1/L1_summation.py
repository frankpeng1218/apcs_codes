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



# 方法二:
N = int(input())
total = 0
for i in range(N+1):
    total += i
print(total)

# 方法三:
N = int(input())
print(sum(range(N+1)))

# 方法四:
print(sum(range(int(input())+1)))