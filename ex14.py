from sys import argv

script, user_name = argv

promt = '>'

print ("Hi %s, I'm the %s script." %(user_name, script))

print ("I'd like to ask you a few  question.")
print (" Do you like me %s ?" %user_name)

like = input(promt)

print (" Where do you live %s?" % user_name)

lives = input(promt)

print ("What kind of computer do you have ?")

computer = input (promt)

print ("""
	Alright, so you said %r about liking me.
	You live in %r . Not sure where that is.
	And you have %r comuter. Nice,
""" %(like, lives,computer))