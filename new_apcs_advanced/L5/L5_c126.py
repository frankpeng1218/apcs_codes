#
# c126: Tree Recovery
#
import sys

# 定義樹的節點結構
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # 根節點是前序遍歷的第一個元素
    root_value = preorder[0]
    root = TreeNode(root_value)

    # 找到根節點在中序遍歷中的位置
    root_index_in_inorder = inorder.index(root_value)

    # 左子樹的中序和前序
    left_inorder = inorder[:root_index_in_inorder]
    left_preorder = preorder[1:len(left_inorder)+1]

    # 右子樹的中序和前序
    right_inorder = inorder[root_index_in_inorder+1:]
    right_preorder = preorder[len(left_inorder)+1:]

    # 遞迴建樹
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root

def postorderTraversal(root):
    if not root:
        return []
    # 後序遍歷：左子樹 -> 右子樹 -> 節點
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.value]


# start
for row in sys.stdin:
    prestring, instring = map(list, row.split())
    
    root = buildTree(prestring, instring)
    postorder_result = postorderTraversal(root)

    print("".join(postorder_result))

