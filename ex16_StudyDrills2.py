from sys import argv

script, filename = argv

target = input("Which file do you want to truncate?")
target_file = open(target, 'w')

target_file.truncate()

print("Now start to write for your empty file")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Writing.......Please wait......")
target_file.write(line1)
target_file.write("\n")
target_file.write(line2)
target_file.write("\n")
target_file.write(line3)
