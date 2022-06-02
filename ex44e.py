class Other(object):
	
	def override(self):
		print("OTHER ovverride()")
	
	def implicit(self):
		print("OTHER implicit()")
	
	def altered(sef):
		print("OTHIER altered()")


class Child(Other):
	
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE OTHER altered()")
		self.other.altered()
		print("CHILD, AFTER OTHER altered()")

son = Child()
son.implicit()
son.override()
son.altered()