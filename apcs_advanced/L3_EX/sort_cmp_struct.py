# 物件排序

from functools import cmp_to_key  # 匯入 cmp_to_key 用於自訂比較函式

def obj(a, b):
    # 
    # 若輸入兩個元素 a, b
    # 自行定義比較的條件
    #

#start
data = [ ... ]  # 待排序的物件列表

r = sorted(data, key=cmp_to_key(obj))  # 使用自訂比較函式進行排序
