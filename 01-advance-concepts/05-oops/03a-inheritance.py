
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