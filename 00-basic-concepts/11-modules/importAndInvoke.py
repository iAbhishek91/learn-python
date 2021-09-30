# import everything
import definition

#specific import
from definition import person


definition.greeting("Abhishek") # OUTPUT: Hello, Abhishek


#Check all the variables and methods of a module
print(dir(definition))
## OUTPUT: ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'greeting', 'person']




print(person["name"]) # OUTPUT: Abhishek Das
