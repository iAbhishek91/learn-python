# Is array and list same
## No, Python do not have support of array.
## However, list is used as array.

# What is the diff between array and list
## all array are list, but all list are not array.
## array holds only one data-type but list holds any type data.

# Basic characteristics are same for List and Array
## LIST and ARRAY are ORDERED, MUTABLE, allow DUPLICATE(else refer Set)

# DESTRUCTURE array

array = ["apple", "banana", "grape"]
apple , banana, grape = array
print(apple + " " + banana + " " + grape) # OUTPUT: apple banana grape 

# LENGTH
print(len(array))  # OUTPUT: 3

# TYPE
mixed = [10, True, 'a']
print(type(mixed))  # OUTPUT: <type 'list'>

# INSERT,REPLACE,DELETE value
## replace and insert if range is less than values provided
array[1:2] = ["watermelon", "strawberry"]
print(array) # OUTPUT: ['apple', 'watermelon', 'strawberry', 'grape']
## replace only if accurate values are provided
array[1:3] = ["blueberry", "blackberry"]
print(array) # OUTPUT: ['apple', 'blueberry', 'blackberry', 'grape']
## relace and delete if range is greater than values provided
array[1:4] = ["kiwi", "Jackfruit"]
print(array) # OUTPUT: ['apple', 'kiwi', 'Jackfruit']

# INSERT ONLY
array.insert(2,"mango")
print(array) # OUTPUT: ['apple', 'kiwi', 'mango', 'Jackfruit']

# APPEND
array.append("orange")
print(array) # OUTPUT: ['apple', 'kiwi', 'mango', 'Jackfruit', 'orange']

# ADD another array
salad = ["Tomato", "Cucumber", "Lettuce"]
array.extend(salad)
print(array) # OUTPUT: ['apple', 'kiwi', 'mango', 'Jackfruit', 'orange', 'Tomato', 'Cucumber', 'Lettuce']
# ADD another tuple(it can be any iterable)
topping = ('salt', 'pepper')
array.extend(topping)
print(array) # OUTPUT: ['apple', 'kiwi', 'mango', 'Jackfruit', 'orange', 'Tomato', 'Cucumber', 'Lettuce', 'salt', 'pepper']
empty_arr = []
print(empty_arr) # []
[].append('abhishek')
print(empty_arr) # None
array_of_dic = [{'name': 'sutapa'}, {'name': 'malpa'}]
array_of_dic.append({'name': 'subho'})
print(array_of_dic) # [{'name': 'sutapa'}, {'name': 'malpa'}, {'name': 'subho'}]
array_of_dic.extend([{'name': 'dinesh'},{'name': 'tanvi'}])
print(array_of_dic) # [{'name': 'sutapa'}, {'name': 'malpa'}, {'name': 'subho'}, {'name': 'dinesh'}, {'name': 'tanvi'}]

# example of list
active_policy_statements = "XXXXXXXXXXXXXX"
resources = 'YYYYYYYY'
credential_expiry = 'ZZZZZZZZZ'
iam_policy_statement_1 = [{   
            "Sid": "test" + str(len(active_policy_statements)),
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": resources,
            "Condition": {
                "DateLessThan": {"aws:CurrentTime": credential_expiry}
            },
        }]
iam_policy_statement_2 = [{   
            "Sid": "test" + str(len(active_policy_statements)),
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": resources,
            "Condition": {
                "DateLessThan": {"aws:CurrentTime": credential_expiry}
            },
        }]
print([].extend(['abhishek', 'sutapa'])) # ERR

# REMOVE
array.remove('mango')
print(array) # OUTPUT: ['apple', 'kiwi', 'Jackfruit', 'orange', 'Tomato', 'Cucumber', 'Lettuce', 'salt', 'pepper']

# POP
## remove last item by default, else the mentioned index
array.pop()
print(array) # OUTPUT: ['apple', 'kiwi', 'Jackfruit', 'orange', 'Tomato', 'Cucumber', 'Lettuce', 'salt']
array.pop(0) # same as del
print(array) # OUTPUT: ['kiwi', 'Jackfruit', 'orange', 'Tomato', 'Cucumber', 'Lettuce', 'salt']

# DELETE: delete mention item, or the entire array
del array[0]
print(array) # OUTPUT: ['Jackfruit', 'orange', 'Tomato', 'Cucumber', 'Lettuce', 'salt']



# LOOP through
## LOOP items
for x in array:
  print(x)
## LOOP index
for i in range(len(array)):
  print(array[i])
## shorthand: Support latest version of python only
# [print(x) for x in array]

# COMPARISION
## newlist = [expression for item in iterable if condition == True]
## the condition is optional and can be skipped.
newlist1 = [x for x in array if x != "apple"]
# map operation (but only one line is allowed)
mapArray = [x.upper() for x in array]

# ITERABLE
## iterable can be list, tuple, set
newlist2 = [x for x in range(10)]
newlist3 = [x for x in range(10) if  x < 5]

# SORT
## ascending
array.sort()
print(array)
## decending
array.sort(reverse = True)
print(array)
## custom logic
## define sort function, the sort function should return a number which will be used for sort.
## (lower return value first)
# array.sort(key = sortFunction)
## case insensitive (by default its case sensitive)
array.sort(key = str.lower)

# REVERSE
array.reverse()

# COPY: arr1 = arr2 will not work as it makes reference
## to make true copy use the inbuilt function
trueCopy = array.copy() # this work with Python 3

# JOIN
joined = array + trueCopy
## else use append() or extend()




print('*'*30)
## LIST comprehention
l1 = [x for x in range(10)]
l2 = [x*x for x in range(20)]
print(l1)
print(l2)