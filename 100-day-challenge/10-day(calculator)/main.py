import math

def add(a:float, b:float):
    return a + b

def sub(a:float, b:float):
    return a - b

def mul(a:float, b:float):
    return a * b

def div(a:float, b:float):
    return a / b

def squareRoot(a:float):
    return math.sqrt(a)


# easily extendable to any operation
unary_operations = {
    'sqrt': squareRoot,
}

# easily extendable to any operation
binary_operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def calc():
    result = 0

    num1 = float(input("first number: "))
    print(', '.join([x for x in binary_operations] + [ y for y in unary_operations]))

    while True:
        operator = input("enter any operator from above list: ")

        # UNARY operation
        if [x for x in unary_operations if operator == x ]:
            result = unary_operations[operator](num1)

        # BINARY operation
        if [x for x in binary_operations if operator == x ]:
            num2 = float(input("second number: "))
            result = binary_operations[operator](num1, num2)
        
        # Output the result
        print(result)

        # Consider previous result for next iteration
        num1 = result

         # RESET the calculator
        reset = input("want to reset: yes or no: ").lower()
        if reset == 'yes': calc()
            

calc()