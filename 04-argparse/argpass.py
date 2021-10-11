import argparse


#
# define arguments
#
parser = argparse.ArgumentParser(description="trying out with argument parser")

parser.add_argument('-f','--firstName', help="Enter your first name", required=True)
parser.add_argument('-l', '--lastname', help="Enter your last name", required=True)
parser.add_argument('--gender', help="Enter your gender", default=None)

#
# process the argument
#
args = parser.parse_args()

first_name = args.firstName
lastname = args.lastname
gender = args.gender

print('*'*30)
print(f'Name: {first_name} {lastname}, and he is {gender}')
