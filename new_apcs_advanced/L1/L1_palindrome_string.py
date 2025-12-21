#
# 字串迴文
#

def is_palindrome_recursive(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome_recursive(s, left+1, right-1)


# start
s = input().strip()
if is_palindrome_recursive(s, 0, len(s)-1):
    print("yes")
else:
    print("no")


# 方法二：
s = input().strip()
print("yes" if s == s[::-1] else "no")
