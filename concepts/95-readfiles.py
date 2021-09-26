f = open('concepts/95-readfile.txt', 'r')
try:
    data = f.read() ## read entire file
    line = f.line() ## 
    print(data)
finally:
    f.close()

# with is special block
# same as try finally
# it will close the file
with open('concepts/95-readfile.txt', 'r') as f:
    data = f.read()
    print(data)