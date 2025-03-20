while True:
   try:
      year = int(input())  # 讀取使用者輸入並轉換為整數（年份）

      # 判斷是否為閏年
      if year % 4 == 0 and year % 100 != 0:  # 能被 4 整除但不能被 100 整除
          print("閏年")  # 是閏年
      elif year % 400 == 0:  # 能被 400 整除
          print("閏年")  # 是閏年
      else:
          print("平年")  # 其他情況皆為平年
      
   except:  # 若輸入無效或發生錯誤，則跳出迴圈
      break
