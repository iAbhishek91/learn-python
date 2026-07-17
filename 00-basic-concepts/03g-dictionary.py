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

# these are live views
# use list to explitely convert them
## GET LIST OF ALL KEYS
print(person.keys()) # OUTPUT: dict_keys (['city', 'age', 'name']) is a live view
## GET LIST OF ALL VALUES
print(person.values()) # OUTPUT: dict_values(['Mexico', 50, 'bob']) is a live view
## GET LIST OF ALL ITEMS
print(person.items()) # OUTPUT: ['Mexico', 50, 'bob']

## LOOP through dictionary
### can loop on person OR live views - person.values() OR person.keys() OR person.items()
print("loop though dictionary...")
for x in person:
  print(person[x])

## OUTPUT:
## Mexico
## 50
## bob

for x in person.keys():
  print(x)
for x in person.values():
  print(x)
for x in person.items():
  print(x)
print("end of loop though dictionary...")

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

# sort a dictionary
hashmap = {
  "auth": 2,
  "sec": 3,
  "logout": 1
} # dictionary
hashmap_sorted = sorted(hashmap.items(), key= lambda hashmap: hashmap[1])
