# list all the files in directory

from os import walk

myPath = './concepts'
dirpath, dirnames, filenames = next(walk(myPath))

print(filenames)
print(dirnames)
print(dirpath)
