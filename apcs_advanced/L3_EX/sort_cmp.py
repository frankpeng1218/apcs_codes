# 物件排序

from functools import cmp_to_key  # 匯入 cmp_to_key 以使用自訂比較函式

def obj(a, b):
    if a[1] > b[1]:  # 依據第二個欄位值進行比較 (數值較大者排後)
        return 1
    elif a[1] < b[1]:  
        return -1
    else:  # 若第二欄位相同，則比較第三欄位
        if a[2] > b[2]:  
            return 1
        elif a[2] < b[2]:  
            return -1
        else:  # 若第三欄位相同，則比較第四欄位
            if a[3] > b[3]:  
                return 1
            elif a[3] < b[3]:  
                return -1
            else:  # 若所有欄位都相同，則視為相等
                return 0

#start    
data = [['A', 100, 60, 30],  
        ['B', 80, 50, 80],  
        ['C', 80, 50, 90],  
        ['D', 70, 70, 85],  
        ['E', 50, 20, 60]]  # 待排序的物件列表

r = sorted(data, key=cmp_to_key(obj))  # 使用自訂比較函式進行排序

print(r)  # 輸出排序結果
