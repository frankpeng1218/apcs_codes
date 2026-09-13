tree = [0, "A", "B", "C", "D", "E", 0, "F"]
def show_children(index):
    if index >= len(tree) or tree[index] == 0:
        print("節點不存在")
        return
    l_index = index * 2
    r_index = index * 2 + 1

    if l_index < len(tree) and tree[l_index] != 0:
        L = tree[l_index]
    else:
        L = "無"

    if r_index < len(tree) and tree[r_index] != 0:
        R = tree[r_index]
    else:
        R = "無"

    print(f"節點 {tree[index]} 的左子節點: {L}，右子節點: {R}")

# 走訪整棵樹
for i in range(1, len(tree)):
    if tree[i] != 0:
        show_children(i)


# 建構二元樹
tree = [0] * 16

# 二元樹儲存函式：根據父節點索引與左右子節點設定
def save_node(index, value, left=None, right=None):
    if index >= len(tree):
        print("超出範圍，無法插入節點！")
        return
    tree[index] = value
    if left is not None:
        tree[index * 2] = left
    if right is not None:
        tree[index * 2 + 1] = right

save_node(1, 'A', 'B', 'C')   # A 的左右
save_node(2, 'B', 'D', 'E')   # B 的左右
save_node(3, 'C', None, 'F')  # C 的右節點是 F
