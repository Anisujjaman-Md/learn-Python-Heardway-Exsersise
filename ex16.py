from sys import argv

script, filename = argv

print("We're going to erase %r." %filename)
print("If you won't do that, hit CTRL -C (^C).")
print ("If you do want that, hit ENTER.")

input("?")
print("Opening the file")
target = open(filename,'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lin.")

line1 = input("Line 1: ")
line2 = input ("Line 2: ")
line3 = input ("Line 3: ")

print("I'm going to write these to the file")
target.write(line2)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And Finally, we close it.")
target.close()