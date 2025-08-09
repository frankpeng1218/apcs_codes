#start

# 定義星期的元組
week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

date = int(input())  # 讀取當前日期（數字）
day = input()  # 讀取當前日期對應的星期
next_date = int(input())  # 讀取下一個日期（數字）

start = week.index(day)  # 找到當前星期在元組中的索引
print(start)  # 輸出當前星期的索引

# 計算下一個日期對應的星期
temp = ((next_date - date) % 7 + start) % 7  

print("next_date is", week[temp])  # 輸出下一個日期的星期
