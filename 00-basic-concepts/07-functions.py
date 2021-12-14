### POSITIONAL ARGUMENT
def functionName(arg1, arg2):  # function with positional argument
  pass

# INVOCATION
functionName(10, "string")




### KEYWORD ARGUMENT
def keywordArgument(a, b):
  print(a-b)

# INVOCATION
keywordArgument(b=2, a=3) # output: 1
keywordArgument(a=2, b=3) # output: -1




### DEFAULT PARAMETER (NOTE: PARAMETER and ARGUMENT are NEVER same thing)
def defaultParam(a=10): # "a" is a PARAMETER and | "10" is a argument
  print(a)

defaultParam() # OUTPUT: 10
defaultParam(1000) # OUTPUT: 1000





# Defining data type
def add(a:str, b:str):
  print(a+b)


add(2, 3)






# DYNAMIC NUMBER OF PARAMETER
## not sure how many parameter to pass
## args is passed as tuple | * is not pointer as in C 
def dynamicParam(*args):
  print(args)

dynamicParam("alpha", "beta", "theta", "omega") # OUTPUT: ('alpha', 'beta', 'theta', 'omega')






# PASS PARAMETER USING NAME
def substraction(a, b):
  return a - b

print(substraction(b=10, a=20)) # OUTPUT: 10






# PASS PARAMETER NAME AND VALUE, WHEN NUMBER OF PARAMETER IS NOT KNOWN
## kwargs is passed as dictionary
def knowNothing(**kwargs):
  print("First name is " + kwargs["firstName"])

knowNothing(firstName="abhishek", lastName="das") # OUTPUT: First name is abhishek







# HIGH ORDER FUNCTION - HOF
## A function is called Higher Order Function
## if it contains other functions as a parameter
## or returns a function as an output.
## Properties of HOF (same as Javascript functional programming)
## - function is treated as object
## - store function as a variable or other datastructure
#3 - pass function as a parameter
## - return function from a function

## NOTE: composition of function with lambda also creates HOF
## refer lambda for more details

## treating function as object
def x():
  print("hello")

y = x
y() # OUTPUT: hello
