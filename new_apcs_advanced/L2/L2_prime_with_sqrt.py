import time
import math

# 找質數, 籃子法
#start
N = int(input())

start_time = time.time()

prime = []

for i in range(2, N+1):
    isPrime = True

    end = int(math.sqrt(i))
    #print(end)
    
    for j in range(2, end+1):
        if i%j == 0 and j!=i:
            isPrime = False

    if isPrime==True:
        prime.append(i)
            

end_time = time.time()

print(prime)
print("excution time:", (end_time-start_time), "s")
