import time


MAX_SIZE = 10000
table = []

#start
N = int(input())

#start = time.time()

table.append(1)
table.append(2)

for i in range(2, MAX_SIZE):
    t = table[i-1]+table[i-2]
    table.append(t)

print(table[N-1])

#end = time.time()
#print("excution time:", round((end-start), 3), "s")
