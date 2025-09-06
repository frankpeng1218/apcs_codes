#start

# 讀取一行輸入字串
s = input()

# 將輸入字串以空白分割成多個元素，存成 data 列表
data = [ x for x in s.split()]

# 計算有多少個元素
N = len(data)

# 建立一個空列表 num，用來存放每個元素拆解後的字元列表
num = []

# 對每個元素逐一處理
for i in range(0, N):
    temp = list(data[i])  # 將字串 data[i] 拆成字元列表
    num.append(temp)      # 加入 num 列表中

# 輸出結果
print(num)
