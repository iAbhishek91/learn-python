# SIMPLE CLASS
## Define a simple class
class FirstClass:
  x = 5

## Create a object of the above class
firstObject = FirstClass()

## Access class member using object
print firstObject.x # OUTPUT: 5




# CLASS WITH CONSTRUCTOR
## Define a call with a constructor
class ClassWithConstructor:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  # self parameter is a reference to the current instance of the class
  def add(self):
    return self.a + self.b

  def addThreeNumber(abc, third):
    return abc.a + abc.b + third
  

## create a object
constructor = ClassWithConstructor(50, 60)

## Invoke member of class via object
print constructor.a # OUTPUT: 50
print(constructor.add()) # OUTPUT: 110
print(constructor.addThreeNumber(10)) # OUTPUT: 120


## Modify class members
constructor.a = 100
print(constructor.addThreeNumber(10)) # OUTPUT: 170








# INHERITANCE
## Parent class definition
class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def getFullName(self):
    return self.fname + " " + self.lname


## Child class definition
class Student(Person):
  # if we implement, __init__ in child class, parent __init__ will not be invoked
  # hence we need to invoke that manually from child constructor, very similar to Javascript
  def __init__(self, fname, lname, year):
    # Python also Javascript way of calling parent class __init__
    # SYNTAX super().__init__(fname, lname)
    Person.__init__(self, fname, lname)
    self.year = year
  
  def welcome(self):
    print("Welcome " + self.getFullName() + ", to batch of " + self.year)

## Create a instance of Student
abhi = Student("Abhishek", "Das", "2021")
abhi.welcome() # OUTPUT: Welcome Abhishek Das, to batch of 2021