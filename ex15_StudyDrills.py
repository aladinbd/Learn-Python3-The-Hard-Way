from sys import argv

script, filename = argv

file_name = input("Which file do you want to check?")
file_text = open(file_name)
print(file_text.read())
