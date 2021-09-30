# 0, 1, 1, 2, 3, 5, 8

from time import sleep as s

def fibonacci(count):
    if count>0:
        n=0
        first_num,sec_num=0,1

        while n<count:
            yield first_num
            first_num,sec_num=sec_num, first_num+sec_num
            n+=1

values=fibonacci(10)

for i in values:
    print(i)