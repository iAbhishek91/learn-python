def reveseString(string):
  reverse = []
  for x in string:
    reverse.insert(0, x)
  return ''.join(reverse) # str(x) for x in reverse


print(reveseString("madam")) # OUTPUT: madam
print(reveseString("AbhisheK")) # OUTPUT: KehsihbA