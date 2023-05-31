# constructor
# is called everytime a object is create from this class
# used for defining attributes for object

class ExampleConstructor:
    def __init__(self, u_id, name):
        self.u_id = u_id
        self.name = name
        self.company = "CA"  # default value


user_1 = ExampleConstructor(10, "Abhishek")  # exactly same as user1.name="Abhishek" unlike javascript
print(user_1.name)
