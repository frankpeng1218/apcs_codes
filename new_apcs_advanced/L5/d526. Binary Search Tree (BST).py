# d526. Binary Search Tree (BST)
# 二元搜尋樹（Binary Search Tree, BST）
# 遞迴（Recursion）
# 類別（class）

class TreeNode:
    def __init__(self, value):
        self.value = value # 節點存放的數值
        self.l = None # 左節點
        self.r = None # 右節點

def insert_value(root, new_value):
    # 若root 是None, 表示找到插入的位置, 建立新節點
    if root is None:
        return TreeNode(new_value)
    # 若new_value < root.value: 插入左邊的節點
    if new_value < root.value:
        root.l = insert_value(root.l, new_value)
    # 否則就插入右邊的節點
    else:
        root.r = insert_value(root.r, new_value)
    return root

def preorder_display(root):
    if root:
        print(root.value, end=" ")# 先印根
        preorder_display(root.l) # 印左邊
        preorder_display(root.r) # 印右邊
        
while True:
    try:
        N = int(input()) # 6
        data = list(map(int, input().split())) # 5 2 10 4 9 15

        # 第一個數字作為BTS的根(root)
        root = TreeNode(data[0]) # 5

        # 依序插入剩餘的數字
        for i in range(1, len(data)):
            root = insert_value(root, data[i])

        # 印出BST的前序遍歷
        preorder_display(root)
        print()
        
    except:
        break
