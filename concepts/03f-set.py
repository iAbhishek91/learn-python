# Set is UNORDERED and UN-INDEXED, IMMUTABLE, DUPLICATES are not allowed
## Immutable: in Set you can change the values that are already exist,
## but we can add/delete unique item to the set

# Create a set
mySet = {"apple", "grape"}

print("mySet is of type: " + str(type(mySet)) + "; of length: " + str(len(mySet)))



# ACCESSING SET element is different
## Unlike list or tuple, we can access set by index or by name
## its always accessed via loop
for x in mySet:
  print(x)



# CHECK item exists
print("grape" in mySet) # OUTPUT: True



# ADD Item
mySet.add("kiwi")
print(mySet) # OUTPUT: set(['kiwi', 'grape', 'apple'])


# ADD any iterable (set, list, tuple or dictionary)
## FIRST WAY: Update()
color = {"red", "blue", "green", "yellow"}
mySet.update(color)
print(mySet) # OUTPUT: set(['kiwi', 'blue', 'grape', 'apple', 'green', 'yellow', 'red'])
## SECOND WAY: union() it creates a new set
greek = {"alpha", "beta", "gamma", "theta"}
colorGreek = color.union(greek)
print(colorGreek) # OUTPUT: set(['blue', 'yellow', 'beta', 'green', 'gamma', 'alpha', 'theta', 'red'])
## THIRD WAY: intersection
colorModern = {"cyan", "neon", "red"}
commonColor = colorModern.intersection(color)
print(commonColor) # OUTPUT: set(['red'])
## FOURTH WAY: intersection_update: same as intersection with update
## FIFTH WAY: keep element that are NOT available in both the set
uncommonColor = colorModern.symmetric_difference(color) 
print(commonColor) # OUTPUT: set(['kiwi', 'blue', 'grape', 'apple', 'green', 'yellow'])
## SIXTH WAY: symmetric_difference_update: same as symmetric_difference with update

# REMOVE array from the list
mySet.remove("red")
print(mySet) # OUTPUT: set(['kiwi', 'blue', 'grape', 'apple', 'green', 'yellow'])


# POP
x = mySet.pop()
print(x + " " + str(mySet)) # OUTPUT: kiwi set(['blue', 'grape', 'apple', 'green', 'yellow'])