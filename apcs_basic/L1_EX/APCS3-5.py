#start

#輸入: 平地溫度
temp = int(input("請輸入平地溫度"))  # 讓使用者輸入平地溫度，轉換為整數

#計算: 溫度轉換
Y_temp = temp - (3952 / 100) * 0.6  # 計算玉山山頂溫度變化
F_temp = temp - (3776 / 100) * 0.6  # 計算富士山山頂溫度變化
J_temp = temp - (4158 / 100) * 0.6  # 計算少女峰山頂溫度變化

#輸出: 高山溫度
print("玉山山頂的溫度:", round(Y_temp, 1))  # 使用 round() 四捨五入至小數點第一位
print("富士山山頂的溫度:", round(F_temp, 1))
print("少女峰山頂的溫度:", round(J_temp, 1))
