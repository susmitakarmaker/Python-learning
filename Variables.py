a = 5
b = "Susmita"

print(type(a))
print(type(b))

# Global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

