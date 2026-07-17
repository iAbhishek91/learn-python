# LAMBDA are SMALL ANONYMOUS FUNCTION
# Take ONLY ONE expression
# but can take any number of arguments
# SYNTAX: lambda arguments: expression (evaluated and returned)

addTwenty = lambda x : x + 20
print(addTwenty(20)) # OUTPUT: 40 

add = lambda a,b : a + b
print(add(10, 30)) # OUTPUT: 40


# Function composition: Creating HOF
def addX(n):
  return lambda x : x + n

addFive = addX(5)
addFour = addX(4)

print(addFive(14)) # OUTPUT: 19
print(addFour(16)) # OUTPUT: 20 

# another bit more complex
hashmap = {
  "auth": 2,
  "sec": 3,
  "logout": 1
} # dictionary

print(hashmap.items())

print((lambda hm: hm[1])(list(hashmap.items())[0])) # this is what hashmap calls it
print(sorted(hashmap.items(), key=lambda hashmap: hashmap[1], reverse=True))
