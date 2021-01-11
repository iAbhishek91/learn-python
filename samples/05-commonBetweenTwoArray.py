# find if there are any common element or NOT
# receive two array and return false.

def commonElementExist(arr1, arr2):
  set1 = set(arr1)
  set2 = set(arr2)
  if len(set1.intersection(set2)) > 0:
    return True
  return False


print(commonElementExist([0,1,2,3,4], [0])) # OUTPUT: True
print(commonElementExist([0,1,2,3,4], [0, 2])) # OUTPUT: True
print(commonElementExist([0,1,2,3,4], [])) # OUTPUT: False
print(commonElementExist([0], [0])) # OUTPUT: True
print(commonElementExist([], [])) # OUTPUT: False