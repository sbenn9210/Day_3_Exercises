user_input = int(input("Choose your number"))

def check_user_input(num):
    if num % 2 == 0:
        print('Your number is even.')
    else:
        print('Your number is odd.')

check_user_input(user_input)
