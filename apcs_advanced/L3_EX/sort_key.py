# 自訂鍵值排序

data = ["85C",        # 字串長度：3
        "Starbucks",  # 字串長度：9
        "Louisa",     # 字串長度：6
        "Dante",      # 字串長度：5
        "MrBrown"]    # 字串長度：7

r = sorted(data, key=len)  # 依據字串長度進行排序

print(r)  # 輸出排序結果
