f = open('./01-advance-concepts/04-file-handling/03a-readfile.txt', 'r')
try:
    data = f.read() ## read entire file
    line = f.readline() ## 
    print(data)
finally:
    f.close()




print("#"*30)
# with is special block
# same as try finally
# it will close the file
with open('./01-advance-concepts/04-file-handling/03a-readfile.txt', 'r') as f:
    data = f.read()
    print(data)