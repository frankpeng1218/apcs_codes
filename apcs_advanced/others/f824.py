# 中文數字轉阿拉伯數字對應表
# 用來將輸入的中文字數字（如「一」、「二」）轉換成數字（1、2）
chinese_to_digit = {
    '一': 1,
    '二': 2,
    '三': 3,
    '四': 4,
    '五': 5,
    '六': 6,
    '七': 7,
    '八': 8,
    '九': 9,
    '十': 10
}

# 完全手動建立阿拉伯數字轉中文數字對應表（反向）
# 讓程式能將數字（如 2）轉回對應的中文（「二」）
digit_to_chinese = {}

# 以下為手動逐一轉換的對應設定
k = '一'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '二'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '三'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '四'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '五'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '六'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '七'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '八'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '九'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

k = '十'
v = chinese_to_digit[k]
digit_to_chinese[v] = k

# 手動加入加法結果可能會出現的數字（11~20）對應的中文寫法
digit_to_chinese[11] = '十一'
digit_to_chinese[12] = '十二'
digit_to_chinese[13] = '十三'
digit_to_chinese[14] = '十四'
digit_to_chinese[15] = '十五'
digit_to_chinese[16] = '十六'
digit_to_chinese[17] = '十七'
digit_to_chinese[18] = '十八'
digit_to_chinese[19] = '十九'
digit_to_chinese[20] = '二十'

# 進入讀取輸入的主迴圈
while True:
    try:
        # 嘗試讀取一行輸入並移除前後空白
        line = input().strip()

        # 如果不是長度為3的字串（不符合格式），直接輸出「謬」
        if len(line) != 3:
            print("謬")
            continue

        # 拆解輸入：第一個字是第一個數字，第二個字是操作詞，第三個字是第二個數字
        first = line[0]
        operator = line[1]
        third = line[2]

        # 如果中間的字是「有」或「又」，表示要進行加法運算
        if operator == '有' or operator == '又':
            # 確保第一個和第三個字都在我們定義的中文數字裡
            if first in chinese_to_digit and third in chinese_to_digit:
                a = chinese_to_digit[first]
                b = chinese_to_digit[third]
                total = a + b  # 執行加法

                # 檢查加總結果是否在我們的對應表中
                if total in digit_to_chinese:
                    print(digit_to_chinese[total])  # 輸出對應的中文數字
                else:
                    print("謬")  # 若無對應，則視為錯誤
            else:
                print("謬")  # 若任何一邊不是合法數字，輸出「謬」
        else:
            print("謬")  # 若中間字不是「有」或「又」，也輸出「謬」

    except:
        # 如果讀取失敗（例如 EOF 結束輸入），跳出迴圈
        break
