user_num = int(input("What is the temperature?"))

user_temp = input("Fahrenheit or Celsius?")

def user_temperature(num, convert):
    if convert == "Fahrenheit":
        conversion = num * 1.8 + 32
        print(conversion)
    elif convert == "Celsius":
        conversion = (num - 32) * .5556
        print(conversion)

user_temperature(user_num, user_temp)
