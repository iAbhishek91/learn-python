def listComparator(arr1, arr2):
  i = 0
  result = []
  
  while(i < len(arr1)):
    if arr1[i] == arr2[i]:
      result.append(1)
    else:
      result.append(0)
    i += 1
  
  return result

print(listComparator([1,2],[1,2])) # OUTPUT: [1, 1]
print(listComparator([1,2],[3,4])) # OUTPUT: [0, 0]
print(listComparator([1,2,3],[4,6,3])) # OUTPUT: [0, 0, 1]