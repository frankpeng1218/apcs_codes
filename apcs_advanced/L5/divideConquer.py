import sys

def search(arr, s, e):
    # divide end: 當子陣列長度為1時，回傳該元素作為最小值與最大值
    if s+1 == e:
        return arr[s], arr[s]
    m = (s+e)//2

    # 繼續分割: 將陣列一分為二，分別遞迴查找最小值與最大值
    left_min, left_max = search(arr, s, m)
    right_min, right_max = search(arr, m, e)

    # 往上回傳時: 取左右兩個子陣列中的最小值與最大值
    return (min(left_min, right_min), max(left_max, right_max))

for s in sys.stdin:
    data = list(map(int, s.split()))

    # 呼叫search函數尋找最小值與最大值
    result_min, result_max = search(data, 0, len(data))
    # 輸出最小值與最大值
    print(result_min, result_max)
