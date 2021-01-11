# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.


def findSingleNumber(arr):
  arr.sort()
  length = len(arr)
  for i in range(length):
    if arr[i-1] == arr[i] or arr[(i+1)%length] == arr[i]: continue
    return arr[i]


print(findSingleNumber([1,1,3,3,2,2,5])) # OUTPUT: 5
print(findSingleNumber([1,5,3,3,2,2,5])) # OUTPUT: 1
print(findSingleNumber([1,1,5,3,2,2,5])) # OUTPUT: 3
