with open('/etc/mime.types', 'r') as f:
    lines = f.readlines() # use readline as oppose to readlines as it will put everything on memory
    #print(lines[0:10])
    for line in lines[0:10]:
        print(line, end='')

# can be used as class, and create other operation like Tail, grep etc and use it using Intreface
# remember that we are using class can be bit expensive in memory
## TDL below