first_num = int(input("Please enter the first number:"))

operand = input("What math operation would you like to perform?")

second_num = int(input("Please enter the second number:"))

def do_math(first_number, sign, second_number):
    if operand == '*':
        result = first_number * second_number
    elif operand == '+':
        result = first_number + second_number
    elif operand == '-':
        result = first_number - second_number
    elif operand == '/':
        result = first_number / second_number
    return result


do_math(first_num, operand, second_num)
