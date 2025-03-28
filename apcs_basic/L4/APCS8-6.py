#import math
import math  # 匯入 math 模組

#start
PI = math.pi  # 取得 π 的值

r = float(input())  # 讀取輸入的半徑值，轉換為浮點數

circumference = 2 * r * PI  # 計算圓周長
area = r * r * PI  # 計算圓面積

print(round(circumference, 2))  # 輸出圓周長，四捨五入至小數點後兩位
print(round(area, 2))  # 輸出圓面積，四捨五入至小數點後兩位
