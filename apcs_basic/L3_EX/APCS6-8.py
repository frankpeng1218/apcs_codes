import sys  # 匯入 sys 模組，允許從標準輸入讀取資料

#start
people = {'A': 0, 'B': 0, 'C': 0}  # 初始化投票計數字典

for s in sys.stdin:
    vote = int(s)  # 讀取並轉換輸入為整數

    # 根據投票數更新對應候選人的計票數
    if vote == 1:
        people['A'] = people['A'] + 1
    elif vote == 2:
        people['B'] = people['B'] + 1
    elif vote == 3:
        people['C'] = people['C'] + 1

    print(people)  # 輸出當前投票結果
