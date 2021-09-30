from time import sleep as s

# this is a generator function
def countDown(n):
  print('contdown started...')
  while n>0:
      yield n
      n = n-1
  print('time over!!!')

values=countDown(5) # this is the generator function

for n in values:
  print(n)
  s(1) # sleep for 1 sec, will act as clock
