def loop(a):
	print(a)
	return loop(a+1)

b=1
loop(b)