# There are THREE type of variables
## Instance variable
## Static variable
## Local Variable


# There are THREE type of method
## Instance Method
## Class Method ==>
## Static Method ==>

# STATIC keyword do not exist in python
class TypeOfVariableMethod:
  '''Demo of different type variable and method'''
  def __init__(self): # self points to current object

  _STATIC = "I am static"
  def printStatic():
    print(StaticVariable._STATIC)
  
StaticVariable.printStatic()
