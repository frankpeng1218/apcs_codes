import sys, math

# 開始讀取輸入
N = int(input())  # 讀取玩家數量 (不過此變數未使用)

# 從標準輸入中讀取每位玩家的牌
for s in sys.stdin:
    data = list(map(int, s.split()))  # 將每位玩家的 5 張牌轉換為整數列表

    # 將牌的編號轉換為花色和點數
    handcard = []  # 存儲每張牌的花色和點數
    for i in data:
        card = []  
        flower = math.ceil(i / 13)  # 花色 (1: 黑桃, 2: 紅桃, 3: 方塊, 4: 梅花)
        number = i % 13             # 點數 (0: K, 1~12: A~Q)
        card.append(flower)         # 加入花色
        card.append(number)         # 加入點數

        handcard.append(card)       # 將該牌加入手牌列表

    score = 0  # 初始化得分

    # 檢查順子 (Straight)
    card_num = []  # 存儲所有牌的點數
    for i in range(5):
        card_num.append(handcard[i][1])
    card_num.sort()  # 將點數排序

    diff = 0  # 計算連續差值
    for i in range(4):
        if card_num[i+1] - card_num[i] == 1:  # 如果相鄰兩張牌的點數差為 1
            diff += 1

    if diff == 4:  # 如果 5 張牌點數連續
        score = 4  # 設置基礎分數為 4 (順子)

        # 檢查是否為同花 (Flush)
        now_flower = handcard[0][0]  # 紀錄第一張牌的花色
        isFlush = True
        for i in range(1, 5):  # 檢查每張牌的花色是否相同
            if handcard[i][0] != now_flower:
                isFlush = False
        if isFlush:  # 如果是同花
            score += 3  # 分數加 3 (同花順)

    else:  # 如果不是順子
        # 檢查對子和重複點數
        num_type = []  # 用來存儲有重複的點數
        for i in range(5):
            now_point = handcard[i][1]  # 取出當前牌的點數
            for j in range(i+1, 5):  # 與其他牌進行比較
                if handcard[j][1] == now_point:  # 如果點數相同
                    score += 1  # 增加分數 (每對 1 分)
                    if now_point not in num_type:  # 如果該點數尚未記錄
                        num_type.append(now_point)  # 記錄該點數
        # 檢查是否為葫蘆 (Full House)
        if len(num_type) == 2 and score == 4:  # 如果有兩種重複的點數且分數為 4 (一對+三條)
            score += 1  # 分數加 1 (葫蘆)

    # 輸出該玩家的最終分數
    print(score)
