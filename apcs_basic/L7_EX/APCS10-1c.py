import sys  # 匯入 sys 模組，用來讀取標準輸入（stdin）

# 使用 sys.stdin 逐行讀取輸入
for s in sys.stdin:
    # 將每行輸入的字串轉換成字元列表
    # 例如輸入 "abc123\n" 會變成 ['a', 'b', 'c', '1', '2', '3', '\n']
    ID = list(s)

    # 印出轉換後的字元列表
    print(ID)
