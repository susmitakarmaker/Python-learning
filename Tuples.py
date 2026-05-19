# Tuples are used to store multiple items in a single variable.

tuples1 = ("apple","banana","mango","cherry", 30, True, "orange")
print(tuples1)
print(len(tuples1))

# type
thisTuples = ("apple",)
print(type(thisTuples))

# Not a tuple
thisTuples = ("apple")
print(type(thisTuples))

# Tuples access and modification
tuples = (1,2,3,4,5,6,7,8,9)
print(tuples[-3:])
print(tuples[2])
print(tuples[-4])
print(max(tuples))
print(min(tuples))

# tuples unpacking
tuples2 = (2,4,6,8)
a,b,c,d = tuples2
print(a,b,c,d)
