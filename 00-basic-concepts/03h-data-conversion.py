# conversion is done using builtin function

print('*'*20)
num=0b111 # can be decimal, octal, hexadecimal or binary
print(bin(num))

print(oct(num))

print(hex(num))


print('*'*20)
integer=10
string='10'
string1='10j'
string2="True"
num=0

print(str(num))
print(int(string))
print(float(string))
print(complex(string1))
print(bool(num))
print(bool(string2))




print('*'*20)
# address of num
print(id(num))