# 1 + 2 + 3 + ----- + n

n = int(input("Enter the number : "))
sum = 0
for x in range(1, n+1 , 1):
    sum = sum + x
print(sum)

# 2 + 4 + 6 + ----- + n

n1 = int(input("Enter the number : "))
sum1 = 0
for y in range(2, n1 + 1 , 2):
    sum1 = sum1 + y
print(sum1)

# 1^2 + 2^2 + 3^3 + ----- + n^n

n2 = int(input("Enter the number : "))
sum2 = 0
for z in range(1, n2 + 1 , 1):
    sum2 = sum2 + z*z
print(sum2)
