# ITERATOR ARE OBJECT, WHICH CONTAIN COUNTABLE NUMBER OF VALUES.
# SPECIALTY OF ITERATOR IS THAT WE CAN TRAVERSE THROUGH THE VALUES IN MUCH MORE CONTROLLED FASHION
# PYTHON ITERATOR ARE VERY SIMILAR TO Javascript
## In Python, if a object implement __iter__() and __next__() function, then they are Iterable. 

# WHAT is Iterable?
## Iterable are inbuilt object which supports Iteration.
## They are List, Tuple, Dictionaries, Set
## String are under the hood list, hence string also can be iterated


# Example of Iterator
## Create a iterable object 
myTuple = ("apple", "pears", "banana")

myTupleIter = iter(myTuple)

print(next(myTupleIter)) # OUTPUT: apple
print(next(myTupleIter)) # OUTPUT: pears
print(next(myTupleIter)) # OUTPUT: banana



# Loop through iterator
## In Python, "for" loop is mainly used for iterator
for x in myTuple:
  print(x)
## OUTPUT:
## apple
## pears
## banana




# CREATE a user defined iterator
class MyFibonacci:
  def __iter__(self):
    self.a = 0
    self.b = 1
    return self

  def __next__(self):
    x = self.b
    temp_a = self.a
    self.a = self.b
    self.b = temp_a + self.b
    return x


fibonacci = MyFibonacci()
myIter = iter(fibonacci)

for x in range(5):
  print(next(myIter)) # 1,1,2,3,5