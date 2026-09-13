class TreeNode:
    def __init__(self, value):
        self.value = value  # 節點的值
        self.left = None    # 左子樹
        self.right = None   # 右子樹

# 建立樹的根節點
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)

# 進一步建立左子樹和右子樹
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)

# 訪問樹的節點值
print(root.value)       # 8
print(root.left.value)  # 3
print(root.right.value) # 10
