# try - except - finally
try:
  print(notDefined)
except:
  print("some error occurred")
finally:
  print("finally block")
## OUTPUT:
## some error occurred
## finally block



# Multiple catch
try:
  print(a)
except NameError:
  print("a is NOT defined")
except:
  print("something else went wrong")
## OUTPUT:
## a is NOT defined



# ELSE BLOCK
## else block is executed IF AND ONLY IF there is no error raised
## finally will be executed no matter what,
## else block can help you to write small try blocks
try:
  pass
except:
  print("v is not available")
else:
  print("Nothing went wrong")
## OUTPUT:
## Nothing went wrong