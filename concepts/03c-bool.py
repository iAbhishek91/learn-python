# conditional operation lead to bool value
# VALID Values are True, or False

# All are true - same as Javascript
# 0, '', empty list, tuple, set, dictionary
print(bool(())) # tuple
print(bool([])) # list
print(bool({})) # dictionary
print(bool(0)) # zero
print(bool('')) # empty string
print(bool(None)) # None (this is not available in Javascript)

# all outputs to: False
