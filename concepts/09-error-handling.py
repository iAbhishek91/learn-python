# try - except - finally
try:
  print(notDefined)
except: # same as except BaseException:
  print("some error occurred")
# if no exception in try: try finally
# if exception in try, and handled: try catch finally
# if exception in try, and not handled: try finally, abnormal termination
# if exception in catch: try, catch, finally abnormal termination
# if exception in finally: try , finally abnormal termination

finally:
  print("finally block")
## OUTPUT:
## some error occurred
## finally block



print("*" * 20)
# Multiple catch
try:
  print(a)
except NameError: # aware of hierarchy, if we use higher level class, then all the child class is taken care
  print("a is NOT defined")
except: # default except block, should be last except block - else SYNTAX ERROR
  print("something else went wrong")
## OUTPUT:
## a is NOT defined



print("*" * 20)
# NESTED TRY catch
try:
  try:
    print(a1) # Used case: when we use have too much risky code
  except:
    print("nested try catch in try")
  finally:
    print("nested try catch in try")
except:
  try:
    print(a1) # Used case: when we use alternative solution
  except:
    print("nested try catch in except")
  finally:
    print("nested try catch in except")
finally:
  try:
    print(a1)
  except:
    print("nested try catch in finally")
  finally:
    print("nested try catch in finally")




print("*" * 20)
# Multiple exception in single except block
try:
  print(10/0)
except (ZeroDivisionError, ValueError) as err: # internally this are considered as tuple, hence first bracket
  print("Exception occurred: ", err)
  print("Name of the error:", err.__class__.__name__)




print("*" * 20)
# ELSE BLOCK
## else block is executed IF AND ONLY IF there is no error raised
## finally will be executed no matter what,
## else block can help you to write small try blocks
## else can be defined only if except is defined, else SYNTAX error
try:
  pass # example: open a file
except:
  print("Something went wrong") # example: handle the error FileNotExists
else: # 
  print("Nothing went wrong") # example: read the file and print
finally:
  print("Execute irrespective of anything happens") # example: close the file
## OUTPUT:
## Nothing went wrong



print("*" * 20)
## Throw is same as raise
class Foo(Exception):
  pass

try:
  raise Foo()
except(Foo): #except Fp as e:
  print("caught") # pass will ignore




print("*" * 20)
## PRINT exception information
try:
  print(10/0)
except ZeroDivisionError as e:
  print("Error message:",e)
  print("The type of exception:", type(e))
  print("The alternative type of exception:", e.__class__)
  print("The name of the exception class:", e.__class__.__name__)





print('*'*20)
## user defined exception
## should inherits from BaseException or child exception, generally "Exception" is used
class InsufficientfundsException(Exception):
  def __init__(self, msg):
    self.msg = msg

withdrawAmount = 20000
balance = 10000

try:
  if withdrawAmount > balance:
    print("Withdraw is invalid")
    raise InsufficientfundsException("insufficient fund available")
  else:
    print("Withdraw is valid")
except InsufficientfundsException as e:
  print("error message: ", e)
  print("The alternative type of exception:", e.__class__)
  print("The name of the exception class:", e.__class__.__name__)




print("*" * 20)
## os.exit()
## THERE IS ONE SCENARIO, WHEN FINALLY BLOCK IS NOT EXECUTED
## when PVM is exited manually for example during power off.
import os
try:
  print('try')
  os._exit(0) # PVM exits manually, 0 is status code, 0 is normal termination, !0 is abnormal termination
except:
  print('except')
finally:
  print('finally')


## finally BLOCK: meant for cleanup code
## Destructor BLOCK: meant for cleanup code
# finally block is meant to closed all resources opened within try block
# destructor is meant to close resources related to object
