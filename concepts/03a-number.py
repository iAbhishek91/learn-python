import random

# INT
#unlimited size
int1 = 9987098273049582734095872309847502983475
int2 = -2098374509827345
int3 = 0b1111 # in binary
int4 = 0o7654 # in octal
int5 = 0x9876 # in hexadecimal
print(int1)  # OUTPUT: 9987098273049582734095872309847502983475
print(-int2)  # OUTPUT: 2098374509827345
print(int3, int4, int5) # OUTPUT: 15, 4012 39030 they always output as decimal



#FLOAT
float1 = 1232347019837401928374.12398471029384710928347
float2 = 12234e2
float3 = 56.23e3
print(float1)  # OUTPUT: 1.23234701984e+21
print(float2)   # OUTPUT: 1223400.0
print(float3)  # OUTPUT: 56230.0



#COMPLEX
# always ends with imaginary j
complex1 = 2j
complex2 = 4.8j
print(complex1 + complex2)  # OUTPUT: 6.8j



#RANDOM
print(random.randrange(0,10))  # OUTPUT: 6