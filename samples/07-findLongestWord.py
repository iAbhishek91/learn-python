def findLongestString(sentence):
  arr = sentence.split(' ')

  biggestString = ''
  for x in arr:
    if len(x) > len(biggestString):
      biggestString = x
  return biggestString

print(findLongestString("")) # OUTPUT: 
print(findLongestString("Abhishek is leaning Python")) # OUTPUT: Abhishek
print(findLongestString("Abhishek knows Javascript")) # OUTPUT: Javascript