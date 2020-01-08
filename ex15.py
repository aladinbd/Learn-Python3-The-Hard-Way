from sys import argv # from sys module import function or parameter argv

script, filename = argv # unpacking argv

txt = open(filename) # we're opening the file

print(f"Here's your file {filename}:")
print(txt.read()) # Now we're reading our text from our file

print("type the filename again:")
file_again = input("> ") # User prompt to input filename again and assign to file_again variable

text_again = open(file_again) # Now we're opening our file_again file and assign to text_again variable

print(text_again.read()) # Output of user input
