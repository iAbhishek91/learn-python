from random import choice
from time import clock

names=['Rob', 'Bob', 'Dom', 'Tom']
subjects=['NodeJS', 'Python', 'Java']

def developer_list(n):
    developers = []
    for i in range(n):
        developer = {
            'name': choice(names),
            'subject': choice(subjects)
        }
        developers.append(developer)
    return developers


def developer_generator(n):
    for i in range(n):
        developer = {
            'name': choice(names),
            'subject': choice(subjects)
        }
        yield developer


tStart=clock() # start the clock
developers=developer_list(10000000)
tEnd=clock()

print('Time taken for list: ', tEnd - tStart, 'seconds')

tStart=clock() # start the clock
developers=developer_generator(10000000)
tEnd=clock()

print('*'*30)
print('Time taken for generator: ', tEnd - tStart, 'seconds')