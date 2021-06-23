# Like java, date is NOT a data type in Python
# Its a module

import datetime
import re


# CURRENT DATE/TIME
now = datetime.datetime.now()
print(now) # OUTPUT: 2021-01-08 03:55:20.134297


# CREATE AN OBJECT
dob = datetime.datetime(1991, 1, 9)
print(dob)


# FORMAT and FILTER out parts from datetime there are several format
## strftime takes only one paramater: format
print(dob.strftime("%B"))



# Compare timezone
## datetime: 2021-06-22T09:10:51Z
## current date time;
tz = "2021-06-22T15:02:51Z"
match_date = re.search(r'\d{4}-\d{2}-\d{2}', tz)
time = (re.search(r'\d{2}:\d{2}:\d{2}', tz).group()).split(":")
print(match_date.group())
print(time)
date = datetime.datetime.strptime(match_date.group(), '%Y-%m-%d')
date_final = date + datetime.timedelta(hours=int(time[0]),minutes=int(time[1]),seconds=int(time[2]))
print(date_final)

if date_final > datetime.datetime.now():
    print(True)
else:
   print(False)