# FILE handling is an important module
## OPEN >> READ >> WRITE >> CLOSE
# Open a file
## modes
### r: read - default, opens a file for read. Err if do NOT exists.
### a: append - opens a file for appending. creates a file if NOT exists.
### w: write - opens a file for writing. creates a file if NOT exists.
### x: Create - creates a file. Err if exists.
### t: text - default, handles the file in text format
### b: binary - handles the file in binary format. Like images


# SYNTAX
# f = open("demofile.txt", "rt")

# OPEN, READ, UPDATE, WRITE JSON back to file
## open a file in read mode
## path should be relative from where python command is executed OR absolute
import json
fd = open('./concepts/95a-test.json')
## read the content of the file
jsonData = fd.read()
## close the file descriptor
fd.close()
## convert to JSON to python dictionary
myDictionary = json.loads(jsonData)
print(myDictionary) # OUTPUT: {'firstName': 'abhishek', 'age': 50}
## update the content
myDictionary["lastName"] = "das"
## convert from python dictionary to JSON
jsonData = json.dumps(myDictionary)
print(jsonData) # output: {"firstName": "abhishek", "age": 50, "lastName":"das"}
## open the same file in write mode
fd = open('./concepts/95a-test.json', 'w')
## write the data in the file
fd.write(jsonData)
## close the file descriptor
fd.close()





# CREATE and DELETE a file
## Below program, creates a file if do not exists
## and Delete the file if exists
import os

filePath = './concepts/95b-to-be-delete.json'
## check if file exists
if os.path.exists(filePath):
  os.remove(filePath)
else:
  open(filePath, 'x')