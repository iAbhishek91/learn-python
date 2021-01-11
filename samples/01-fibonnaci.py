# 1 1 2 3 5 8 13 21
# input parameter n - value of the position to be returned

def fibonacci(n):
  fibonacciArr = [1,1]

  startIndex = 2
  while(n >= startIndex):
    fibonacciArr.append(fibonacciArr[startIndex-1] + fibonacciArr[startIndex-2])
    startIndex += 1
  
  return fibonacciArr[n-1]


print(fibonacci(6))