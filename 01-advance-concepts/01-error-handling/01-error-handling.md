# Exception handling

## Flow of exception (Default exception handling in Python)

- All exception are class in Python(for example ZeroDivisionError)
- Whenever exception is raised, an object of that error class is raised.
- If there is no exception handling code is available:
  - Python Virtual Machine(PVM) will print the error object information is printed.
  - then program is terminated there.
- If exception handling code is available,
  - first match except block is executed
  - NOTE default except block should be defined at last only(else SYNTAX ERROR)
- If finally block is defined, it will be executed every time, even if match except block is not available.

## Exception hierarchy

- Top most class **BaseException**
  - Many child class of BaseException for eg: **Exception**, **SystemExit**, **GeneratorExit**, **KeyboardInterrupt**
    - Many child class of Exception for eg: **AttributeError**, **ArithmeticError**, **LookUpError**, **OSError**, **AttributeError**, **EOFError**
      - Many child class of ArithmeticError for eg **ZeroDivisionError**, **OverflowError**, **FloatingPointError**
      - Many child class of LookUpError for eg: **IndexError**, **KeyError**
      - Many child class of OSError for eg: **FileNotFound**, **InterruptedError**, **TimeOutError**, **PermissionError**

## Key words used for exception handling

- try
  - write risky code(keep it as small as possible)
- except
  - write alternative code or handling code
- else
  - if try is succuss, other code can come to else
- finally
  - clean up code or resource de-allocation code like db.close(), file.close()
- raise
  - similar to throw

- only try or except or finally CANT exists
- try should be with except or finally or both
- else should be with except, and except should be with try, hence for else both try and except is required.
- multiple except is valid, however multiple finally or else is INVALID
- Order is also important, before except else cant exists. similarly finally cant exist before except and else.

## Type of exception in python

- Pre-defined/In built/PVM exception exceptions
- User defined exceptions
