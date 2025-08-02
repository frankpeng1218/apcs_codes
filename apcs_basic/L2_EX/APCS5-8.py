# M = int(input())  # 讀取使用者輸入的整數 M（列數）
# N = int(input())  # 讀取使用者輸入的整數 N（行數）

# for i in range(N):  # 外層迴圈控制行數
#     for j in range(M):  # 內層迴圈控制列數
#         print("*", end='')  # 連續輸出星號
#     print()  # 換行

# for i in range(5 + 1):  # 外層迴圈控制行數（從 0 到 5）
#     for j in range(1, i + 1):  # 內層迴圈控制每行的星號數量
#         print("*", end='')  # 連續輸出星號
#     print()  # 換行

# 輸出右對齊的星號三角形
for i in range(1, 6):  # 迴圈從 1 到 5
    print(" " * (5 - i) + "*" * i)  # 先輸出空格，然後輸出星號
