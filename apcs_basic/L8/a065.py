import sys

# 定義一個列表 CODE，裡面包含了所有大寫英文字母，用來找字母的索引位置
CODE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#start
for s in sys.stdin:  # 從標準輸入讀入每一行字串（通常用於批改系統或線上 Judge）
    #no.1
    #data = list(s)
    #移除最後的 '\n'
    #data.pop()

    #no.2
    # 使用 strip() 移除字串開頭和結尾的空白字符，包括換行符 '\n'
    # 再用 list() 將字串轉為字元列表
    data = list(s.strip())

    # 遍歷每一對相鄰的字母
    for i in range(len(data)-1):
        # 計算兩字母在 CODE 中索引的絕對差值，代表兩字母之間的距離
        result = abs(CODE.index(data[i]) - CODE.index(data[i+1]))
        # 將結果直接列印出來，不換行
        print(result, end='')

    # 每處理完一行輸入，換行一次
    print()
