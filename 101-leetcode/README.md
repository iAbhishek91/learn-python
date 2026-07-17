# Lesson learnt

- in Python use // to ignore decimal
- use ** to times 10 **2 == 10 ^2(in other language)
- reverse an list [::-1]
- range(len(list)) to loop through index insted of index value
- read the qustion throughly
- sum of number: (num * (num+1))/2
- binary search has two pointer one left and another right we find the mid
- dont use `pop` method in list, as if you pop an element then all the element after it has to be shifted. **Good thing** is pop by defualt pops from end of the list.
- check if value and address is same using "is" operator. (e.g:nums1 is num2)
- If you have and array of string, lets say ["mango", "banana", "strawberry"], and you need to create a new string by concatenating, DONT do this. This is very very inefficient: terrible memory usage an dperformance as each iteration the summation will compute, store and then throw away.
```py
fruits=["mango", "banana", "strawberry"]
one_big_fruit = ""
for fruit in fruits:
    one_big_fruit += fruit
```
Instead: Does all the copy in one pass.
```py
result = ''.join(fruits)
```
- use "in" whereever possible. its generally faster and works with lists, tuples, sets and string(a list).

## Big O

- O(1) aka: constant time:
 - search random element from a list.
 - sum of an integer.
 - inserting beginning of a link list.
- O(log n) aka: logarithmetic time:
 - binary search
 - binary search tree
- O(n) aka: linear time:
 - many many problems
- O(n log n): quasilinear time:
 - sorts: quick, merge, heap
- O(n^2):
 - sorts: bubble, insertion, selection
