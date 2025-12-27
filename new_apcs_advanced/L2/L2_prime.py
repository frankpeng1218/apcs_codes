#start

N = int(input())

for i in range(1, N+1):
    isPrime = True
    for j in range(2, i+1):
        if i%j == 0 and j!=i:
            isPrime = False

        elif j==i and isPrime==True:
            print(i)
