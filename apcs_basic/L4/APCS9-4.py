import sys  # 匯入 sys 模組以讀取標準輸入

# 定義幸運訊息列表
bank = ['Lucky Ball',
        'Lucky Sheep',
        'Lucky Guy',
        'OK',
        'Good Luck']

#start
for s in sys.stdin:  # 逐行讀取標準輸入
    chrlist = list(s)  # 將輸入字串轉換為字元列表
    oddValue = 0  # 初始化奇數索引字元 ASCII 值總和
    evenValue = 0  # 初始化偶數索引字元 ASCII 值總和

    for i in range(len(chrlist)):  # 遍歷字元列表
        if i % 2 == 0:  # 偶數索引
            evenValue += ord(chrlist[i])  # 加總 ASCII 值
        else:  # 奇數索引
            oddValue += ord(chrlist[i])  # 加總 ASCII 值

    lucky = abs(evenValue - oddValue) % 5  # 計算幸運值（差值取模 5）

    print(bank[lucky])  # 輸出對應的幸運訊息
