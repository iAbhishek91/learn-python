import numpy as np
import sys

l = [10,0,90,34,89,45,89,80,30]

a = np.array(l)

print(a)


print("*"*30)
# COMPARE memory
## this is because internal memory storage mechanism
print("size of np.array():", sys.getsizeof(l))
print("Size of List:", sys.getsizeof(a))

