print ("let's practice everything.")

print ('You\'d need to know \'bout escapes withh \\ that do \n newlines and \t tabs.')

poem = """
	\tThe lovely world
	with logic so filmy planted
	cannot discern \n\tthe needs of love
	nor comprehend passion from intuition
	and requires an explanation
	\n\twhere there is none.
	"""
print ("-----------------")
print (poem)
print ("-----------------")

five = 10 - 2 + 3 - 6
print("Thhis should be five: %s" %five)

#Funtion for calculating jeally beans amount
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# First Way
start_points = 10000
beans, big_jars, small_crates = secret_formula(start_points)

print ("With a starting point of : %d " %start_points)
print ("We'd have %d beans, %d jars, and %d crates." %(beans, big_jars, small_crates))

#Second Way
start_point = start_points / 10

print ("We can also do that this way : ")
print("We'd have %d beans, %d jars and %d Crates." %secret_formula(start_points))