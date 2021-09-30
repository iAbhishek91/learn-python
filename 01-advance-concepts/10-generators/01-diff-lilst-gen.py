def myGen():
    yield 'A'
    yield 'B'
    yield 'C'


g = myGen() # gen


l = ['A', 'B', 'C'] # list

## What are DIFFERENCE between g and l

####### REMEMBER this below analogy ##########
## if you need 60 rice bags for 5 years, you have two options
## Option-1: store all 60 bag in house (this is list)
## Option-2: every month buy one 1 rice bag (this is generator)

## ADVANTAGE-1: Generator is always efficient in memory utilization, always recommended to use generator for large data
## Below LIST COMPREHENTION
#l = [x for x in range(10000000000000000000000000000000000000000000000000000000)] ## this will throw MemoryError; all will be stored in memory

## Below LIST COMPREHENTION
gen = (x for x in range(10000000000000000000000000000000000000000000000000000000)) ## in this case nothing is stored in memory, but yields as required
while True:
    print(next(gen))

## ADVANTAGE-2: Huge performance benifit: refer 04-example-handling-hugedata.py