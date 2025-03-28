#start

s = input()  # 讀取使用者輸入的字串
data = s.split()  # 將輸入字串以空格分割成列表

temp = int(data[0])  # 取得第一個數值並轉換為整數 (氣溫)
weather = data[1]  # 取得第二個字串 (天氣狀況)

# 使用舊式格式化方式輸出
print("今天的氣溫是 %d 度, 天氣是 %s 天" % (temp, weather))

# 使用 format() 方法格式化輸出
print("今天的氣溫是 {} 度, 天氣是 {} 天".format(temp, weather))
