#
# 樓梯問題 (遞迴版本)
#

def f(n):
    if n<3:
        return n
    else:
        return f(n-1)+f(n-2)


# start
print(f(10))

