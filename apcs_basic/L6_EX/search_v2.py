import random

number = random.randint(1, 100)

lower = 0
upper = 100

i = 50
count = 0
while True:
    if i == number:
        print("I got you, the number is:", i)
        print("count:",count)
        break
    count += 1
    if i < number:
        lower = i
        i = int((lower+upper)/2)
    elif i > number:
        upper = i
        i = int((lower+upper)/2)

    print("i:", i)
    print("lower:", lower)
    print("upper:", upper)
