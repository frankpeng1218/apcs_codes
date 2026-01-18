# g309: 傳遞杯子蛋糕
# 樹結構（Binary Tree）, 遞迴（Recursion）

def pass_cupcakes(animal_id, cupcakes):
    if animal_id == -1: # 沒有子動物(空的節點)
        return

    # 取得左右子動物
    left_child = tree[animal_id]["left"]
    right_child = tree[animal_id]["right"]

    # 計算子動物的數量(存在才算)
    # 不等於-1的話就是True=1
    child_num = (left_child != -1) + (right_child != -1)

    # 情況1: 當前動物沒有子動物, 蛋糕全部給自己
    if child_num == 0:
        final_cupcakes[animal_id] += cupcakes
        return

    # 情況2: 非最終的動物, 要將蛋糕分(子動物以及自己)
    share = cupcakes // (child_num + 1)# 每份的大小
    remainder = cupcakes % (child_num + 1) # 多出來的蛋糕

    # 給當前主動分的節點(動物) share + remainder
    final_cupcakes[animal_id] += share + remainder

    # 將share分給左右子動物(若存在)
    pass_cupcakes(left_child, share)
    pass_cupcakes(right_child, share)
        

# N: 動物數量, K: 蛋糕數
N, K = map(int, input().split()) # 6 9

tree = {} # 儲存每隻動物的左右子動物
final_cupcakes = [0] * N # 紀錄最後得到的蛋糕數

# 讀取N行動物資訊
for _ in range(N):
    animal_id, L, R = map(int, input().split()) # 0 1 2
    tree[animal_id] = {
        "left": L,
        "right": R
        }

# 從國王(編號0)開始分蛋糕
pass_cupcakes(0, K)

# 將結果輸出成一行, 空白格開
output_string = " ".join(str(x) for x in final_cupcakes)
print(output_string)



