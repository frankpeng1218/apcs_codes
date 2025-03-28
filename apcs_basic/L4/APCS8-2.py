#start

s1 = input()  # 第一行輸入
s2 = input()  # 第二行輸入

s1 = s1.split()  # 分割字串為列表
s2 = s2.split()  # 分割字串為列表

man = int(s1[0])  # 人的位置
wolf = int(s1[1])  # 狼的位置
atk = int(s1[2])  # 攻擊範圍

house = [int(i) for i in s2]  # 建立房屋距離列表

if man < wolf:
    dist = sum(house[man+1:wolf+1])  # 計算從人位置後一格到狼位置之間的距離總和
else:
    dist = sum(house[wolf+1:man+1])  # 計算從狼位置後一格到人位置之間的距離總和

if dist <= atk:
    print("Yes")  # 可以攻擊到狼
else:
    print("No")  # 攻擊範圍不足
