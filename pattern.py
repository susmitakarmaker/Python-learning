# String multiplication: *       |  *       |     *
#                        **      |  ***     |    **
#                        ***     |  *****   |   ***



n = 5
for i in range(1,n+1):
    print(i * "*")

n = 5
for i in range(1,n+1):
    print((2*i-1) * "*")

n = 5
for i in range(1,n+1):
    print(" " * (n-i)+ "*" *i)


# nested loop:

n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*", end= " ")
    print()

n = 5
for i in range(1,n+1):
    for j in range(2*i-1):
        print("*", end= " ")
    print()


n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end= "")
    for k in range(i):
        print("*", end= "")
    print()
    