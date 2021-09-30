# EVERY THING IN PYTHON IS OBJECT
# TWO TYPE OF CLASS: Defined, User defined class

# SIMPLE CLASS
## Define a simple class
class FirstClass:
  '''document string'''
  x = 5

## Create a object of the above class
firstObject = FirstClass()


## Access the class document string
print(FirstClass.__doc__) # First way
help(FirstClass) # Second way, help prints many other details of the class

## Access class member using object
print(firstObject.x) # OUTPUT: 5












# use INTERNAL method
class ClassUseInstanceMethod:
  def a(self):
    return "first function"
  
  def b(self):
    print(self.a())

obj = ClassUseInstanceMethod()
obj.b()


