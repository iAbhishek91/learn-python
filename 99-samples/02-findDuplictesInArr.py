def findDuplicateExists(arr):
  noDuplicate = set(arr)
  if list(noDuplicate) == arr:
    return False
  return True


print(findDuplicateExists([1,2,3,4,5,6,7,7])) # OUTPUT: True
print(findDuplicateExists([1,2,3,4,5,6,7])) # OUTPUT: False