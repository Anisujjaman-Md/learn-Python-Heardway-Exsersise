#this one is like your script with argv

def print_two(*argv):
	arg1, arg2 =argv
	print("arg1: %r, arg2: %r" %(arg1, arg2))

#ok, that * args is actually pointyless, we can just do this

def print_two_again(arg1,arg2):
	print("arg1: %r, arg2: %r" %(arg1, arg2))

# this just takes one argument

def print_one(arg1):
	print("arg1: %r "%arg1)

# this one takes no argument

def print_none():
	print("I got nothing")

print_two("Anis","Shamim")
print_two_again("Boro Anis","Choto Shamim")
print_one("Rabu")
print_none()

	