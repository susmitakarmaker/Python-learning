fruits = ['apple','orange','mango','banana']
print(fruits)

# Access list item
print(fruits[0:3])    # 0 to 3 all print

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
fruits.remove('mango')
print(fruits)

#pop(index)
fruits.pop(3)
print(fruits)

