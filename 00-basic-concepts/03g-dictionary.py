# Dictionary  are like javascript object
## UNORDERED - ordered from 3.6, MUTABLE, DUPLICATES NOT ALLOWED

person = {
  "name": "bob",
  "age": 50,
  "city": "Mexico"
}


# LENGTH AND TYPE
print(str(type(person)) + " " + str(len(person))) # OUTPUT: <type 'dict'> 3





# ACCESS dictionary
print(person.get("name")) # OUTPUT: bob
print(person["name"])# OUTPUT: bob
## print(person.name) # OUTPUT: ERROR This is not allowed

## GET LIST OF ALL KEYS
print(person.keys()) # OUTPUT: ['city', 'age', 'name']
## GET LIST OF ALL VALUES
print(person.values()) # OUTPUT: ['Mexico', 50, 'bob']

## LOOP through dictionary
### can loop on person OR person.values() OR person.keys()
for x in person:
  print(person[x])

## OUTPUT:
## Mexico
## 50
## bob


# ADD ELEMENT or UPDATE EXISTING ELEMENT
person["phone"] = "07384120202"
print(person.keys()) # OUTPUT: ['city', 'age', 'name', 'phone']
person["name"] = "rob"
print(person["name"]) # OUTPUT: rob



# REMOVE element
person.pop("phone")
print(person.keys()) # OUTPUT: ['city', 'age', 'name']



# EMPTY a dictionary
a = {"a":"a"}
a = {}
print(a) # a is now empty


# COPY dictionary
copyPerson = person.copy()
print(copyPerson) # OUTPUT: {'city': 'Mexico', 'age': 50, 'name': 'rob'}
