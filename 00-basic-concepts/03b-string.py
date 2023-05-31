# QUOTES

# Single and Double quotes are same

single = 'abhishek das'
double = "abhishek das"
multiline = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

# CONCATENATION

print(single + " " + double)   # OUTPUT: abhishek das abhishek das
print(multiline)  # OUTPUT: Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.

number = 10

#print(single + number) # this will throw err
print(single + " " + str(number))  # OUTPUT: abhishek das 10

# STRING AS ARRAY
print(multiline[1])  # OUTPUT: L
print(double[1])  # OUTPUT: b

#LOOP
for x in single:
  print(x)  # OUTPUT: a b h i s h e k   d a s

#LENGTH
print("Length of string " + str(len(double)))  # OUTPUT: Length of string 12


#CHECK STRING
#true
print("Lorem" in multiline)  # OUTPUT: True
#false
print("Loram" not in multiline)  # OUTPUT: True

#SLICING STRING
# in a position to b position
print(single[3:8])  # OUTPUT: ishek
# from start to b
print(single[:4])  # OUTPUT: abhi
# from number to end
print(single[9:])  # OUTPUT: das
# negative indexing
print(single[-3:])  # OUTPUT: das

#UPPER and LOWER
print(single.upper())  # OUTPUT: ABHISHEK DAS
print(single.lower())  # OUTPUT: abhishek das
print(single.title())  # OUTPUT: Abhishek Das

#STRIP (same as TRIM)
withSpace = " bla bla bla     "
print(withSpace.strip())  # OUTPUT: bla bla bla

#RELACE A CHAR
print(single.replace('a', 'A'))  # OUTPUT: Abhishek dAs

#SPLIT
print(single.split(' '))  # OUTPUT: ['abhishek', 'das']

#TEMPLATING (also called python formatted string)
template = "my name is {}"
complexTemplate = "my name is {0}, but I like it as {1}"
print(template.format("abhi"))  # OUTPUT: my name is abhi
print(complexTemplate.format("abhishek", "doctor D"))   # OUTPUT: my name is abhishek, but I like it as doctor D
print
# LIST of other string function
#https://www.w3schools.com/python/python_strings_methods.asp