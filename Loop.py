i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  

# While loop: print 1-5, skip 3 with continue
a = 0
while a < 6:
  a += 1
  if a == 3:
    continue
  print(a)

# For loop

fruits = ["apple", "banana", "cherry"]
for y in fruits:
  print(y)

fruits = ["apple", "banana", "cherry"]
for b in fruits:
  print(b)
  if b == "cherry":
    break
  
fruits = ["apple", "banana", "cherry"]
for c in fruits:
  if c == "banana":
    continue
  print(c)

# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for w in adj:
  for z in fruits:
    print(w, z)