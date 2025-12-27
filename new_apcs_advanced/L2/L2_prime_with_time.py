import time

#start
N = int(input())

start_time = time.time()

prime = []

for i in range(1, N+1):
    isPrime = True
    for j in range(2, i+1):
        if i%j == 0 and j!=i:
            isPrime = False

        elif j==i and isPrime==True:
            prime.append(i)

print(prime)
end_time = time.time()

print("excution time:", (end_time-start_time), "s")
