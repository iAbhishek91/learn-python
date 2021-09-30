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
print(constructor.a) # OUTPUT: 50
print(constructor.add()) # OUTPUT: 110
print(constructor.addThreeNumber(10)) # OUTPUT: 120


## Modify class members
constructor.a = 100
print(constructor.addThreeNumber(10)) # OUTPUT: 170







print("*"*30)
# Constructor in case of SIMPLE INHERITANCE
class Employee():
    def __init__(self, f_name, lastname):
        self.f_name = f_name
        self.lastname = lastname

    def printFullName(self):
        print(self.f_name + " " + self.lastname)


class Developer(Employee):
    def __init__(self, f_name, lastname, prog_language):
        super().__init__(f_name, lastname)
        self.prog_language = prog_language

    def printProgrammingLanguage(self):
        print(self.f_name + " knows " + self.prog_language)


dev1 = Developer('Rob', 'Dickson', 'bash')
dev2 = Developer('Adam', 'Murrey', 'go')


dev1.printProgrammingLanguage()
dev2.printProgrammingLanguage()





print("*"*30)
# Constructor in case of MULTIPLE INHERITANCE
class Person():
    def __init__(self, f_name, lastname):
        self.f_name = f_name
        self.lastname = lastname

    def printFullName(self):
        print(self.f_name + " " + self.lastname)

class Employee1(Person):
    def __init__(self, f_name, lastname, company):
        super().__init__(f_name, lastname)
        self.company = company

    def printJobDetails(self):
        print(self.f_name + " works for company: " + self.company)


class Developer1(Employee1):
    def __init__(self, f_name, lastname, company, prog_language):
        super().__init__(f_name, lastname, company)
        self.prog_language = prog_language

    def printProgrammingLanguage(self):
        print(self.f_name + " knows " + self.prog_language)


dev1 = Developer1('Rob', 'Dickson', 'ComplyAdvantage', 'bash')
dev2 = Developer1('Adam', 'Murrey', 'Wipro', 'go')


dev1.printFullName()
dev1.printJobDetails()
dev1.printProgrammingLanguage()
print("*"*30)
dev2.printFullName()
dev2.printJobDetails()
dev2.printProgrammingLanguage()
