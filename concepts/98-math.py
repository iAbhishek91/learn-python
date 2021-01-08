# there are some in-built math function available, and an extensive math library
minimum = min(1, -5, 8)
maximum = max(8, 99, 9)
absolute = abs(-7.7)
power = pow(2, 3)
print(str(minimum) + " " + str(maximum) + " " + str(absolute) + " " + str(power))
# OUTPUT: -5 99 7.7 8

import math

squareRoot = math.sqrt(25)
ceil = math.ceil(1.4)
floor = math.floor(1.9)
print(str(squareRoot) + " " + str(ceil) + " " + str(floor) + " " + str(math.pi))
# OUTPUT: 5.0 2.0 1.0 3.14159265359