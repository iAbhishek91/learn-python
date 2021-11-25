convert_to_int = lambda s : int(s)
sum = lambda a,b: a + b

array = ['1','2','3']
map(convert_to_int, array)
print(array)


reduce(sum, array)
