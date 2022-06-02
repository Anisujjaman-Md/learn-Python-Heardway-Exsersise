#import argv from sys

from sys import argv

# declear argv
script, filename = argv

#open file
txt = open (filename)


print ("Here,s your filename again: %s" %filename)
#Print the element of file
print (txt.read())

#Doing the process again by input file name by keyboard
print ("Type of filename again:")

file_again = input(">")
txt_again = open (file_again)
print (txt_again.read())