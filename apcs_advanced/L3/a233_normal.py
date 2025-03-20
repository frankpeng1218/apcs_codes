#start
import sys  # 匯入 sys 模組以讀取標準輸入 (stdin)

for s in sys.stdin:  # 迴圈讀取標準輸入的每一行
    N = int(s)  # 讀取整數 N，表示數字個數

    num = list(map(int, input().split()))  # 讀取 N 個整數並存入 num 陣列

    num.sort()  # 使用內建的排序函式對 num 進行排序

    # 輸出排序後的數字，使用空格間隔
    for i in range(N):
        print(num[i], end=' ')
    print()  # 換行
