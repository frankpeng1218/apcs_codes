#從檢查公式範例求得->
#10-(135%10)-檢查碼=0->透過這個公式抓出所有可能

import sys

# 英文字母對應的身份證代碼（英文轉數字）
CODE = {
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34,
    'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'O':35, 'P':23, 'Q':24, 'R':25,
    'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33
}

# 用來查詢字母用的字串
code_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 預先算好每個字母對應的「前兩位碼」總和：第1位x1 + 第2位x2 (x2 權重為9)
codeSum = []

#set x1+x2
#先一次算出全部會是多少值
for i in range(26):
    x1 = int(CODE[code_string[i]] / 10)           # 英文代碼的十位數
    x2 = CODE[code_string[i]] % 10 * 9            # 英文代碼的個位數 × 權重9
    codeSum.append(x1 + x2)                       # 加總並存進codeSum

# 從最後一碼來反求
#start
for s in sys.stdin:
    testID = list(s)                              # 把輸入轉為字元列表
    #最後一碼
    checkSum = int(testID[8])                     # 檢查碼是最後一位 (第9碼)
	
    #第1~8碼總和，依據身份證號碼的加權規則，權重依序為 8 ~ 1
    xN = 0
    for i in range(7+1):
        xN += int(testID[i]) * (8 - i)

    # 英文字母的部分，要找出所有可能符合檢查碼的開頭字母
    for x in range(26):
        # 如果代入某一個英文字母的總合（英文碼加權 + 數字碼加權 + 檢查碼）符合規則，印出該英文字母
        if (10 - (codeSum[x] + xN) % 10 - checkSum) == 0:
        #if (codeSum[x] + xN + checkSum) % 10 == 0:   # ← 這是另一種寫法，邏輯等價
            word = code_string[x]
            print(word, end='')                    # 找到就印出來
    print()                                        # 每筆輸入結束後換行
