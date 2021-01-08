# variables are created as we assign a value to it
# there is no command for defining variable
a = 10
print a # OUTPUT: 10

# we also change the value after we a set a value
a = "abhishek"
print a # OUTPUT: abhishek

# Var is case sensitive, hence below are two different variable
a = 5
A = 5

# assign multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x) # OUTPUT: Orange
print(y) # OUTPUT: Banana
print(z) # OUTPUT: Cherry


# one value to multiple variable
x = y = z = "test"

# GLOBAL value
# variable that are declared outside a function
# scoped variable cant be converted into z
x = "I AM GLOBAL"

def myFunc():
  y = "I AM LOCAL"
  global z1
  z1 = "I AM CONVERTED GLOBAL"
  print(x + " | " + y + " | " + z1)

myFunc() # OUTPUT: I AM GLOBAL | I AM LOCAL | I AM CONVERTED GLOBAL
print(z1) # OUTPUT: I AM CONVERTED GLOBAL
