coins = list(map(int, input().split()))

money = int(input())

num = 0

for i in range(len(coins)-1, -1, -1):
    num = num + money//coins[i]
    money = money%coins[i]

print(num)
