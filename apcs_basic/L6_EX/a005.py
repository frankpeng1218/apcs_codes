import sys

#start
N = int(input())  # 讀入測資組數

for i in range(N):
    s = input()  # 讀入一組序列字串
    seq = [ int(x) for x in s.split()]  # 將字串轉為整數序列

    isArithmetic = False  # 初始化為非等差數列
    isGeometric = True    # 預設為等比數列

    diff1 = seq[1]-seq[0]  # 第1與第0項差
    diff2 = seq[2]-seq[1]  # 第2與第1項差
    diff3 = seq[3]-seq[2]  # 第3與第2項差

    if diff1 == diff2 and diff2 == diff3:
        isArithmetic = True  # 符合等差條件

    diff = int(seq[3]/seq[2]);  # 假設為等比，取得公比

    for i in range(0, 3+1):
        if seq[i]%diff != 0:  # 檢查每項是否可被公比整除
            isGeometric = False  # 若不能則非等比
            break

    if isArithmetic == True:
        diff = diff1  # 使用等差公差
        for i in range(4):
            print(seq[i], end=' ')  # 輸出前四項
        print(seq[3]+diff)  # 輸出下一項（第五項）
    else:
        for i in range(4):
            print(seq[i], end=' ')  # 輸出前四項
        print(seq[3]*diff)  # 輸出等比第五項
