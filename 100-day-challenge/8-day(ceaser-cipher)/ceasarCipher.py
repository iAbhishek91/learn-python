print("CEASAR CIPHER")

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def ceasar(op: str, msg: str, sft: int):
    result_string = ''

    if op == 'decode': sft *= -1

    for char in msg:
        if char.isalpha():
            result_string += alphabets[(alphabets.index(char) + sft) % 26]
        else: result_string += char

    return result_string


# keep asking user prompt, until they say "no"
def encrypt_decrypt():
    start = 'yes'

    while start == 'yes':
        operation_type = input("Type 'encode' or 'decode': ")
        message = input("Type your message: ").lower()
        shift_number = input("Type the shift number: ")

        print(ceasar(op=operation_type, msg=message, sft=int(shift_number)))

        start = input("Do you want to continue? 'yes' or 'no': ").lower()

    print("GOODBYE")


encrypt_decrypt()
