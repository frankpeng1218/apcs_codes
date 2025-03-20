#start

# [國語, 英文, 數學, 自然, 社會]
John = [90, 95, 75, 80, 85]  # John 的各科成績
Mary = [60, 75, 99, 55, 90]  # Mary 的各科成績
Oliver = [80, 80, 30, 95, 90]  # Oliver 的各科成績

# 輸出 John's 英文與數學成績
print("John's English", John[1], "Math", John[2])  

# 計算 Mary 的前三科平均分數並輸出
print("Mary's avg=", (Mary[0] + Mary[1] + Mary[2]) / 3)  

# 計算 Oliver 的自然與數學成績差值並輸出
print("Oliver's highest diff", Oliver[3] - Oliver[2])  
