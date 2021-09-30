# 1 * 2 * 3 * ... n; n is the input of the function

def factorial(n):
  if n < 0: return -1
  if n == 0: return 0
  result = 1
  while(n >= 1):
    result *= n
    n -= 1
  return result

print(factorial(3)) # OUTPUT: 6
print(factorial(10)) # OUTPUT: 3628800
print(factorial(100)) # OUTPUT: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
