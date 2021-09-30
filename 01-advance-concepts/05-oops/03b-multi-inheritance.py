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


class Manager(Employee):
    pass ## dont define anything


dev1 = Developer('Rob', 'Dickson', 'bash')
dev2 = Developer('Adam', 'Murrey', 'go')

manager1 = Manager('Manish', 'jain')

dev1.printProgrammingLanguage()
manager1.printFullName()

## two keywords in Python
## isinstance: # validate object instantiated from which class 
## issubclass: # self explanatory
print(isinstance(manager1, Manager)) ## True
print(isinstance(manager1, Employee)) ## True
print(isinstance(manager1, Developer)) ## False


print(issubclass(Developer, Employee)) ## True
print(issubclass(Manager, Employee)) ## True
print(issubclass(Developer, Manager)) ## False
