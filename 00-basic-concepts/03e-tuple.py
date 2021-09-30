# TUPLE is another in-build collection, apart from LIST, DICTIONARY, SET

# What is the difference between list and Tuple
## Same as list(ordered, allow duplicate), but the values are immutable
## Immutable means we cant add or delete element in a tuple. Nither change the or update the element.


# DEFINE a tuple
thisIsATuple = ("apple", "grape", "watermelon", "kiwi", "blueberry", "banana")



# TYPE and LENGTH
print(str(type(thisIsATuple)) + " of length " + str(len(thisIsATuple)))
## OUTPUT: <type 'tuple'> of length 6



# ACCESS TUPLE
print(thisIsATuple[0]) # OUTPUT: apple
print(thisIsATuple[3:5]) # OUTPUT: ('kiwi', 'blueberry')



# CHECK item exists
print("kiwi" in thisIsATuple) # OUTPUT: True



# UPDATE values
## Since they are immutable by nature, we cant directly change the values
## But there is a workaround: convert in list, do the modification and then convert back to tuple
thisIsAList = list(thisIsATuple)
thisIsAList[1] = "seedless grape"
thisIsATuple = tuple(thisIsAList)

print(thisIsATuple) # OUTPUT: ('apple', 'seedless grape', 'watermelon', 'kiwi', 'blueberry', 'banana')



# UNPACKING
## its similar to Javascript
## all, and remaining can go to other list
## * can be added in first, middle somewhere and at last
## (*others, banana) = thisIsATuple
#(apple, grape, *others) = thisIsATuple # this syntax is supported in Python 3

#print(apple + " " + grape + " " + others)



# ADD two tuple
fruits = ("kiwi", "banana", "apple")
color = ("green", "yellow", "red")

addedFruits = fruits + color
print(addedFruits) # OUTPUT: ('kiwi', 'banana', 'apple', 'green', 'yellow', 'red')



# MULTIPLY TUPLES
print(color * 3) # ('green', 'yellow', 'red', 'green', 'yellow', 'red', 'green', 'yellow', 'red')



# COUNT ELEMENT
## done with help of Inbuilt function
print(color.count("green")) # OUTPUT: 1
print(color.count("blue")) # OUTPUT: 0



# FIND INDEX OF ELEMEMT
print(color.index("red"))  # OUTPUT: 2





## Tuple comprehention
## is not possible, like list comprehention
t = (x for x in range(10))
print(t) ## this will create a generator, refer to generator concept in advance python