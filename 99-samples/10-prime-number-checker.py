def prime_number_checker(number: int): # best practice to define datatype(LOL typescript)
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    return is_prime


n = input("Enter a number to be checked as prime: ")

print(prime_number_checker(number=int(n)))
