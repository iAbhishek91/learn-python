# methods in class
# must have a self parameter for all method

class MethodsClass:
    def __init__(self):
        self.start = 0

    def add_number(self, num):
        self.start += num
        return self.start


my_calc = MethodsClass()
print(my_calc.add_number(5))
