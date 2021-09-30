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