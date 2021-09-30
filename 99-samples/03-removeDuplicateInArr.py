# function a return a list with no duplicate
def removeDuplicate(arr):
  return list(set(arr))


print(removeDuplicate([0,0,0,0,1,1,2,2,2,2,3,4,6,9])) # OUTPUT:[0, 1, 2, 3, 4, 6, 9]
print(removeDuplicate([0,0,1,1,1,2,2,3,3,4])) # OUTPUT:[0, 1, 2, 3, 4]
print(removeDuplicate([])) # OUTPUT:[]