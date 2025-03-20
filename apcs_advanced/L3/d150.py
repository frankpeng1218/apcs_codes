
# d150. 11369 - Shopaholic

#start

while True:
    try:
        n = int(input())  # 讀取測試案例數量

        for i in range(n):
            item_num = int(input())  # 讀取商品數量

            price = input()  # 讀取商品價格
            price = list(map(int, price.split()))  # 轉換為整數列表

            price.sort(reverse=True)  # 降序排列，使最貴的商品優先

            max_save = sum(price[2::3])  # 每三件商品取最便宜的作為折扣金額累加

            print(max_save)  # 輸出最大折扣金額

    except:  # 捕捉例外以處理輸入結束
        break
