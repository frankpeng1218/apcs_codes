import sys

# start
for s in sys.stdin:
    data = list(s)       # 將輸入的字串轉成字元 list，包含 '\n'
    data.pop()           # 移除最後的換行符號 '\n'
    
    length = len(data)   # 資料長度

    # 初始化變數
    first_char = ''      # 記錄目前出現次數最多的字元
    temp_char = ''       # 暫時記錄目前連續的字元
    sum_char = 0         # 記錄目前出現最多次的次數
    temp_sum = 1         # 暫時計算目前連續的次數

    # 開始遍歷每一個字元
    for i in range(length):
        if i == 0:
            first_char = data[0]  # 第一個字元先設為目前最大
            sum_char = 1          # 初始出現次數為 1

        else:
            # 如果跟前一個一樣，就增加連續次數
            if data[i] == data[i-1]:
                temp_char = data[i]
                temp_sum += 1
            else:
                # 不一樣時，比較目前 temp_sum 是否比 sum_char 大
                if temp_sum > sum_char:
                    first_char = temp_char    # 更新最多次的字元
                    sum_char = temp_sum       # 更新最多次數

                # 重新統計新的字元
                temp_char = data[i]
                temp_sum = 1

        # 特別處理最後一個字元（如果最後一串是最長的）
        if i == length - 1:
            if temp_sum > sum_char:
                first_char = temp_char
                sum_char = temp_sum

    # end of for
    print(first_char, sum_char)  # 輸出最多連續出現的字元與次數
