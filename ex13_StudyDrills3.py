from sys import argv

script, first_name, last_name, age, weight = argv

first_name = input("What's your first name?")
last_name = input("What's your last name?")
age = input("How old are you?")
weight = input("Please tell us your weight:")

print("Your first name is", first_name)
print("Your last name is", last_name)
print("Your age is", age)
print("Your weight is", weight)
