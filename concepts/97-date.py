# Like java, date is NOT a data type in Python
# Its a module

import datetime


# CURRENT DATE/TIME
now = datetime.datetime.now()
print(now) # OUTPUT: 2021-01-08 03:55:20.134297


# CREATE AN OBJECT
dob = datetime.datetime(1991, 1, 9)
print(dob)


# FORMAT and FILTER out parts from datetime there are several format
## strftime takes only one paramater: format
print(dob.strftime("%B"))