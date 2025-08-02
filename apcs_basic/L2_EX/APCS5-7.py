# start

##for i in range(1, 10):
##    print("1" + "x" + str(i) + "= " + str(1*i), end =' ')


##for i in range(1, 10):
##    for j in range(1, 10):
##        if i*j < 10:
##            print(str(i) + "x" + str(j) + "= " + str(i*j), end=" ")
##        else:
##            print(str(i) + "x" + str(j) + "=" + str(i*j), end=" ")
##    print()



for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(f"{i}x{j}= {i*j}", end=" ")
        else:
            print(f"{i}x{j}={i*j}", end=" ")
    print()
