msg = "Hello World!"
print(msg)
print("---------")

#Variables
print("Variables")
number1 = 10
number2 = 30
result = number1 + number2
print(result)
print("{} + {} = {}".format(number1, number2, result))
print("---------")

#Strings
print("Strings")
greeting = "Hello"
print(len(greeting))
print(greeting[2])
greetingInPart = greeting[0:3]
print(greetingInPart)
noReason = "    asddd ff c     "
print(noReason)
print(noReason.strip())
title = "me, myself and Irene"
print(title.capitalize())
print(title.upper())
print(title.lower())
print(title.replace('e', 'h'))
titleToArray = title.split(' ')
print(titleToArray)
print("---------")

#If condition
print('IF')
age1 = 20
age2= 30
if age1 < age2:
    print("{} is minor than {}".format(age1, age2))
else:
    print("{} is bigger than {}".format(age1, age2))

#Input
print("Inputs")
name = input("Your name: ")
print('Your name is {}'.format(name))