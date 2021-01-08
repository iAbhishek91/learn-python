# FOR and WHILE are primitive loops available in Python

# WHILE
i = 1
while i < 6:
  print(i)
  i += 1
# OUTPUT:
#1
#2
#3
#4
#5


# FOR
## NOTE: Traditional for syntax is not available
## Run for a range
for x in range(6): # run from 0,1,..5
  pass
for x in range(10,16): # run from 10, 11, 12, 13, 14, 15
  pass
for x in range(0, 10, 2): # run from 0, 2, 4, 6, 8
  pass
for x in "abhishek": # run it for string, list, map, tuple, set
  pass

# FINALLY block: Execute a code when while or FOR execution is complete
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("WHILE EXECUTION COMPLETED")
# OUTPUT:
#1
#2
#3
#4
#5
#WHILE EXECUTION COMPLETED

# BREAK/CONTINUE a loop
## Break
i = 1
while i < 6:
  print(i)
  if i > 2:
    break # this will break the loop
  i += 1
# OUTPUT
#1
#2
#3
## Continue
i = 1
while i < 6:
  i += 1
  if i > 2:
    continue
  print(i)
# OUTPUT:
#2