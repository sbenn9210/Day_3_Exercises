user_input = int(input('Please pick a number:'))

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('Fizz Buzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print("You got no Fizz or Buzz!")

fizz_buzz(user_input)
