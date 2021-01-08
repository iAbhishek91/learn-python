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
v_complex = 1j
#SEQUENCE
v_list = ['a', 'b', 'c']
v_tuple = (10, 10.9, "mixed")
v_range = range(6)
#MAP
v_dict = { 'name': "abhishek", 'age':"30" }
#SET
v_set = {"apple", "banana", "cherry"}
v_frozenset = frozenset({"apple", "banana", "cheery"})
#BOOL
v_bool = True
#BINARY
v_bytes = b"apple"
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