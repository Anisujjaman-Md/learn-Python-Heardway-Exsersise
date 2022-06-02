x = "there are %d types of people." %10
binary = "Binary"
do_not = "Don't"
y = "Those who know %s and those who %s. " %(binary, do_not)

print(x)
print(y)

print("I said: %r ." %x)
print("i also said: '%s' ." %y)

hilirious = False
joke_evaluation = "isn't that joke so funy ?! %r"

print(joke_evaluation % hilirious)

w = "This is the left side off ...."
e = "a string with a right side."
print (w+e)