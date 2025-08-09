import sys  # 匯入 sys 模組，允許從標準輸入讀取資料

# 逐行讀取標準輸入
for s in sys.stdin:
    nums = [ int(i) for i in s.split() ]  # 將輸入的字串拆分並轉換為整數列表
    M = nums[0]  # 取得第一個數字，代表月份
    D = nums[1]  # 取得第二個數字，代表日期
    S = (M*2 + D) % 3  # 計算運勢指數 S
    
    # 根據運勢指數 S 的值輸出對應的結果
    if S == 0:
        print("普通")  # S 為 0，輸出 "普通"
    elif S == 1:
        print("吉")  # S 為 1，輸出 "吉"
    else:
        print("大吉")  # S 為 2，輸出 "大吉"
