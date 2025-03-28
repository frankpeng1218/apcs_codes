# 雜訊文字 需要移除的符號
noise = '()-[]{};:<>?@#$%^&*'

#start
s = input()  # 讀取使用者輸入的字串
words = s.split()  # 以空格分割字串成單字列表

correct = ''  # 初始化儲存處理後字串的變數

for w in words:  # 遍歷每個單字
    w_len = len(w)  # 取得單字長度
    string = ""  # 初始化存放過濾後字元的變數
    
    for i in range(0, w_len):  # 遍歷單字內的每個字元
        if w[i] not in noise:  # 若該字元不在 noise 列表中
            string += w[i]  # 加入到處理後的字串中
            
    correct += string + " "  # 將處理後的單字加回正確的句子

print(correct.strip())  # 輸出結果，並移除最後多餘的空格
