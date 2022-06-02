def add(a, b):
	print("Adding %d + %d" %(a, b))
	return a + b

def substract(a, b):
	print("Substracting %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("Multipling %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("Dividing %d / %d" % (a, b))
	return a / b

print("Let's do some math using this function!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d " %(age, height, weight, iq))

#A puzzle for extra credit, type it anyway

print("here is a puzzle")

what = add(age, substract(height,multiply(weight, divide(iq, 2))))

print(f"That becomes: {what} can do it by hand?")

print(f"multiply {multiply(5, 2)}")