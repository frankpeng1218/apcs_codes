#start

# 從 1 到 100 進行迴圈
for i in range(1, 100 + 1):
    if i % 2 == 0:  # 如果 i 是偶數
        continue  # 跳過本次迴圈，不執行後續程式碼

    print(i, "is odd.")  # 輸出奇數及其對應訊息
