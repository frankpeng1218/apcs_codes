#
# 樓梯問題 (遞迴版本)
#

import time

def f(n):
    if n<3:
        return n
    else:
        return f(n-1)+f(n-2)

start = time.time()

# start
print(f(10))

end = time.time()

print("excution time:", round((end-start), 3), "s")
