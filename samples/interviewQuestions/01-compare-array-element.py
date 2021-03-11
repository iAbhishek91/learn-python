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
print(listComparator([1,-7,3,4,5,6,7,8,9,0,5,3,2,3,4,4,5,6,7,100000000000000,2323232323232323],[1,-7,3,4,5,6,7,8,9,0,5,3,2,3,4,4,5,6,7,100000000000000,2323232323232323]))
print(listComparator(['madam', True, '', '£$@£$'],['madam', 'True', '', '£$@£$']))