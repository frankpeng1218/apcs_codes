#start

vowel = ['a', 'e', 'i', 'o', 'u']  # 定義母音字母列表

s = input()  # 讀取輸入字串

count = 0  # 初始化母音計數

# 遍歷輸入字串的每個字母
for i in s:
    for j in vowel:
        if i == j:  # 如果字母是母音
            count = count + 1  # 計數加一

print("Total:", count)  # 輸出母音總數
