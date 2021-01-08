# if-elif-else is the only conditional statement
# there is NO SWITCH statement in python
# we will check later how we can create a function which act as switch.

# IF-ELSE
if True:
  print("Inside IF")
else:
  print("Inside ELSE")


# IF-ELIF-ELSE
if False:
  pass # pass statement used when there is nothing to write, as block cant be empty
elif True:
  print("Inside ELIF")
else:
  print("Inside ELSE")



a=10
b=20
# SHORTHAND
## only IF
#if a > b: print("a is greater than b")
## if else (TERNARY OPERATOR). Unlike, Javascript, ?: is NOT available in python
## if-elif-else
#print("A") if a > b else print("B")
#print("A") if a > b else print("=") if a == b else print("B")