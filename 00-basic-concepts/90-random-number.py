# practically its impossible for a computer to generate a random number for ever.
import random

print(random.randint(0, 5))  # random number between 2 and 10
print(random.random())  # random float number b/w 0.00000000 0.99999999
random.seed(2) # choose the start of the randomness
print(random.randint(1, 10))  # it will always be same
