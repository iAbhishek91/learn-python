class FirstClass:
  x = 5

firstObject = FirstClass()
print firstObject.x


# CLASS WITH CONSTRUCTOR
## Define a call with a constructor
class ClassWithConstructor:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def add(self): # self parameter is a reference to the current instance of the class
    return self.a + self.b

## create a object
constructor = ClassWithConstructor(50, 60)

## Invoke member of class via object
print constructor.a
print(constructor.add())


#del constructor.