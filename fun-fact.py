# MUST READ: https://web.archive.org/web/20170316131253id_/http://python.net/%7Egoodger/projects/pycon/2007/idiomatic/handout.html

# ZEN of python, execute >>>import this

# Whitespace rules 1 and 2.

# Naming

# Long lines and continuations

# Long string

# Compund statements

# Docstring and comments

# SWAP values

a = 10
b = 5
a, b= b, a # this example of packing and unpacking
print(f"Swapped value: {a}, {b}")
print("-"*30)

# Packing and Unpacking

## Packing and Unpacking are a concept of Tuple
## () is for readability, where comma "," is treated as syntax, dont forget the comma
## empty () is a shortcut to create a tuple.

# More examples
print("Packing and Unpacking")
l = ['Rob', 'Mr', '+44-7384120201']
name, title, phone = l

print(f"name: {name}, title: {title}, phone: {phone}")
people = [l, ["Bob", "Mr", "+44-6876876"]]
for (name1,title1,address1) in people:
    print(f"name1: {name1}, title1: {title1}, address1: {address1}")
print("-"*30)
print("Nested Unpacking")
rob, (bob_name, bob_title, bob_phone) = people
print(f"rob: {rob}, bob: {[bob_name, bob_title, bob_phone]}")
print("-"*30)

# More about tuple

a = 10, # comma automatically interprets the value as atuple
print(f"a: {a} is of type: {type(a)}")
b = () # round paranthesis is a shortcut of creating tuple
print(f"a: {b} is of type: {type(b)}")
print("-"*30)

# Interactive "_"

## Only works on interactive
## if a command do not output anything the value remains unchange.
## >>> 2+2
## 2
## >>> _
## 2

# String and Join

## NEVER use it
fruits=["Mango", "Banana", "Strawberry"]
## one_big_fruit = ""
## for fruit in fruits:
##     one_big_fruit += fruit

## Instead use Join
one_big_fruit = "".join(fruits)
print(f"One big fruit: {one_big_fruit}")
one_big_fruit = " ".join(fruits)
print(f"One big fruit: {one_big_fruit}")
one_big_fruit = ", ".join(fruits)
print(f"One big fruit: {one_big_fruit}")
print("-"*30)

## Use of function to generate a list of string
def fn(i: str):
    return i.lower()

result = ', '.join(fn(i) for i in fruits) # this is generator expression(will discuss later)
print(f"Result of joining strings generated using a function: {result}.")
