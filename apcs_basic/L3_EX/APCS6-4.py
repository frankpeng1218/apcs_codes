#start

times = [5, 6, 4, 5, 1, 8, 4]  # 定義時間列表

# 計算並輸出索引 2 到 4（含 2 不含 5）的總和
print(sum(times[2:5]))  

# 計算並輸出索引 3 到最後的總和
print(sum(times[3:]))  

# 計算並輸出索引 0 到 5（含 0 不含 6）的總和
print(sum(times[:6]))  

# 計算並輸出間隔 2 取值的總和（索引 0, 2, 4, 6）
print(sum(times[::2]))  
