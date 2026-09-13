import sys
from bisect import bisect_right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(a, l, r):
    if l > r:
        return None
    if l == r:
        return TreeNode(a[r])
    
    # 使用 bisect_right 來加速查找位置
    pos = bisect_right(a, a[r], l, r)
    return TreeNode(a[r], dfs(a, l, pos - 1), dfs(a, pos, r - 1))

def output(root, fa, result):
    if root is None:
        return
    output(root.left, root.val, result)
    result.append(f"{root.val} {fa}\n")
    output(root.right, root.val, result)

# start
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
    
root = dfs(a, 0, n - 1)
    
# 使用 list 暫存結果
result = []
output(root, -1, result)
    
# 一次性輸出，避免多次 IO 操作
sys.stdout.write("".join(result))
