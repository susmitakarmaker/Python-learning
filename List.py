fruits = ['apple','orange','mango','banana']
fruits.sort()
print(fruits)
print(fruits[0])     #index 0 print
print(len(fruits))
print(fruits*2)     # double print index


# Access list item
print(fruits[0:3])    # 0 to 3 all print
print(fruits[1:])     # index 1 to last print
print(fruits[-1])     # index last print

# Update list item
fruits[-1] = 'jackfruit'
print(fruits)

# List item add
fruits.append("lemon")
print(fruits)

# insert(index,item)
fruits.insert(1,"papaya")
print(fruits)

# remove item list
fruits.remove("mango")
print(fruits)

#pop(index)
fruits.pop(0)
print(fruits)

