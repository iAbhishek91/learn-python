# NOTE we don't put space between binary operator like in JAVA or JAVASCRIPT
# there tools like lints - mypy
# ARITHMETIC
print(2**3) # power - OUTPUT:  8
print(5//2) # floor division - OUTPUT: 2


# BITWISE
print(2&4) # bitwise AND - OUTPUT: 0
print(2|4) # bitwise OR - OUTPUT: 6
print(2^4) # bitwise XOR - OUTPUT: 0
print(~2) # bitwise NOR - OUTPUT: 1


# LOGICAL
print(True and False) # OUTPUT: False
print(True or False) # OUTPUT: True
print(not False) # OUTPUT: True


#COMPARISION
print('abhishek' == 'abhishek')  # OUTPUT: True
print(10 != 11)  # OUTPUT: True


#IDENTITY
# used for validating variable
# almost similar to === in Javascript
# VALID OPERATORS: is, is not
a = ["a", "b"]
b = ["a", "b"]
print(a == b) # OUTPUT: True
print(a is b) # OUTPUT: False


#MEMBERSHIP
# used to check if a value is part of collection
# VALID OPERATORS: in, not in
v_list = ['apple', 'guava', 'cherry']
print('apple' in v_list) # OUTPUT: True

v_tuple = ('apple', 10, True)
print(10 in v_tuple) # OUTPUT: True