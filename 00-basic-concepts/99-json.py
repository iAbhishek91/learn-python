# JSON library: convert safely python object into JSON and vice versa
import json

# CONVERT FROM JSON >> PYTHON OBJECT
## some JSON
x = '{ "fName":"abhishek", "lName":"das"}'
y = json.loads(x) # Y is a python dictionary (similar to Javascript object)

print(y["fName"]) # OUTPUT: abhishek


# CONVERT FROM PYTHON OBJECT >> JSON
## NOTE we can pass any python data to json.dump.
a = {
  "fName":"Abhishek",
  "lName":"Das"
}
b = json.dumps(a) # pass "indent = 4" as second parameter for prettier look.

print(b) # OUTPUT: {"lName": "Das", "fName": "Abhishek"}