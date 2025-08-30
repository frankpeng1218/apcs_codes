# 1912年是元年，民國1年

import sys

sign = ["鼠", "牛", "虎", "兔", "龍",
        "蛇", "馬", "羊", "猴", "雞",
        "狗", "豬"]  # 依序對應 12 生肖

# start
for s in sys.stdin:
    year = int(s)  # 將輸入的字串轉為整數年份

    if year > 0:  # 正年份（西元後）
        if year % 12 == 0:
            print(sign[11])  # 餘數為0時對應最後一個生肖「豬」
        else:
            index = year % 12 - 1  # 其餘依照餘數-1 對應生肖
            print(sign[index])

    elif year < 0:  # 負年份（西元前）
        abs_year = abs(year)  # 取絕對值處理
        if abs_year % 12 == 0:
            print(sign[0])  # 餘數為0時對應第一個生肖「鼠」
        else:
            index = 12 - abs_year % 12  # 其餘反向找回對應生肖
            print(sign[index])
