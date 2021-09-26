"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
#TEXT
v_str = 'abhishek'
#NUMERIC
v_int = 10
v_float = 10.999
# format 10+20j(or 10.34+45.390j) print real and imaginary part; value of j is sqrt(-1). v_complex.real = 10.0, v_complex.imag = 20.0
# both real and imaginary part can be integer and float
# real part can be represented in binary, octal, decimal and hexadecimal, however imaginary part cant represent anything apart from decimal
# arithmetic operation(+-*/) are allowed 10+20j + 20+30j = 30+50j
v_complex = 1j
#SEQUENCE
# MUTABLE
# heterogenous
v_list = ['a', 'b', 'c']
# same as list
# they are IMMUTABLE, append, remove is not allowed
# Order, heterogenous, index, slice
# note one element in tuple is integer: t = (10), print(type(t)) # int; instead mention t = (10,)
# less memory to store, faster access
v_tuple = (10, 10.9, "mixed")
# most commonly used datatype
# its a sequence of number: like 0 to 200 or 40 to 99
# r1 = range(n) 0 to n-1; r2 = range(5,30) 5 to 29; r3 = range(begin, end, increment/decrement) begin to end-1 incremented/decremented by the third val eg range(20,1,-5)
# for i in r1: print(i)
# indexing and slicing is allowed as its a list of values, r = range(10); print(r[0]) # 0 | r1 = r[1:5] # 1,2,3,4 
# they are IMMUTABLE
v_range = range(6)
#MAP
# key value pair; 
# empty dict d = {}; add value d[100] = "hundred"
# duplicate keys are not allowed
# not ordered
# heterogenous
# MUTABLE
# indexing or slicing not available
v_dict = { 'name': "abhishek", 'age':"30" }
#SET
# no duplicate
# order is not required, hence no indexing or slicing
# heterogenous
# MUTABLE, add, remove
# empty set s = set()
v_set = {"apple", "banana", "cherry"}
v_frozenset = frozenset({"apple", "banana", "cheery"})
#BOOL
v_bool = True
#BINARY
# l = [10, 20, 30, 40]; b=bytes(l); type(b) # is bytes; for x in b: print(x)
# byte and bytearray are used mostly to handle audio, video, multimedia data
# values should be b/w 0 to 255 ie range(0,256)
# they are IMMUTABLE; l=[10, 20,30];b=bytes(l);b[0]=77 <== NOT ALLOWED, we fetch index and slice but no assignment
v_bytes = b"apple" # in this case a,p,l,e is converted charter coding to get the value 0 to 255
# bytearray is MUTABLE, this is the main difference between bytes and bytearray
# they are MUTABLE; l=[10, 20,30];b=bytes(l);b[0]=77 <== ALLOWED
# l = [10,20, 30]; br = bytearray(l)
v_bytearray = bytearray(5)
v_memoryview = memoryview(bytes(5))


# If you want to define a data-type of a variable you need to do using casting

v_str = str(3)
v_int = int('1')
v_float = float('4.5')

print(v_int) # OUTPUT: 1

# Get type of variable
print(type(v_str))  # OUTPUT: <type 'str'>
print(type(v_float))  # OUTPUT: <type 'float'>
print(type(v_int))  # OUTPUT: <type 'int'>


#check datatype
print(isinstance(v_list, list))  # OUTPUT: True