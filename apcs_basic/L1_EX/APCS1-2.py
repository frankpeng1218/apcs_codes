s1 = "Orange"  # 定義變數 s1，內容為字串 "Orange"
s2 = "Apple"   # 定義變數 s2，內容為字串 "Apple"

print(s1, s2)  # 直接輸出兩個變數，預設以空格分隔
print(s1, s2, sep="@")  # 使用 sep 參數自訂分隔符號，這裡以 "@" 取代空格
print(s1 + s2)  # 使用 + 來連接（串接）兩個字串，結果為 "OrangeApple"
print(s1 + s2, end=" ")  # end 參數設定輸出結尾為 " "，下一行的輸出會接在後面
print(s1 + s2 + "\n")  # "\n" 代表換行符號，確保輸出換行
