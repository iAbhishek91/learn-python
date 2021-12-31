# scope is either local or global.
# Local scope are created within the function.
# Global scope is either defined outside any function or use "global" function.
# Scope are not bound by block, hence python do not have block scope. For example variable defined inside if or for block can be accessible outside.


## local scope
def my_func():
    local_var = "Abhishek"

my_func()
# print(local_var) # ERROR variable not declared


## global scope
a = 10

def my_second_func():
    a = 20 # IMP: this both "a" are completely different in memory. they never override each other
    print(a) # OUTPUT: 20

print(a) # OUTPUT: 10



## read a global variable within local scope
local_var2 = 40
def my_third_func():
    print(local_var2)

my_third_func() # OUTPUT: 10



## update a global variable within local scope
local_var3 = 999
def my_fourth_func():
    # NOT RECOMMENDED as it makes code difficult to read, confusing and not sure who is referencing it.
    # Reading or using it is OK.
    global local_var3 # explicitely need to declare that we are updating a global variable 
    local_var3 += 1 # this line ERROR if global is not declared
    local_var3 = 10 # this line will not ERROR without global, as this is treated as declaring a new variable.

my_fourth_func()
print(local_var3) # OUTPUT: 1000



## No block scope
if True:
    new_variable =  10

print(new_variable) # OUTPUT: 10
