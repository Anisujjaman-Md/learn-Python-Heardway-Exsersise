class Parent(object):
	
	def override(self):
		print("PARENT ovverride()")

class Childe(Parent):
	
	def override(self):
		print("CHILD ovverride()")

dad = Parent()
son = Childe()

dad.override()
son.override()