def myGen():
    yield 'A'
    yield 'B'
    yield 'C'


g = myGen()

## TYPE of the function
print(type(g)) # since yield is used the function will of type <class 'generator>


## Print the value of g
print(g) # itself is a generator object, however we can use it with loop as below
for i in g: print(i)


print('*'*30)
## Fetch each values manually
# print(next(g)) # this will error as generator function have finished StopIteration