# start
s = input()
data = s.split()

temp = int(data[0])
weather = data[1]

# old
print("今天的氣溫是 %d 度, 天氣是 %s 天" % (temp, weather))

# format
print("今天的氣溫是 {} 度, 天氣是 {} 天".format(temp, weather))

# f-string
print(f"今天的氣溫是 {temp} 度, 天氣是 {weather} 天")

# common
print("今天的氣溫是 " + str(temp) + " 度," + " 天氣是 " + str(weather) + " 天")
