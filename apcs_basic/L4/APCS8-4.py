# 定義攝氏轉華氏溫度的函式
def change(c):
    f = c * (9 / 5) + 32  # 攝氏轉換為華氏
    return f  # 回傳華氏溫度

#start
temp = int(input())  # 讀取輸入的攝氏溫度

now_f = change(temp)  # 呼叫 change 函式進行轉換
print(round(now_f))  # 四捨五入後輸出華氏溫度
