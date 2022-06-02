## Animal is - a object (yes, sort of confusing) look at the extra credit

class Animal(object):
	pass

##Dog is-a  animall

class Dog(Animal):
	
	DEF__init__(self, name):
		##og has a name
		self.name = name

## Cat is-a  Animal

class Cat(Animal):
	def __init__(self,name):
		## Cat has-a name
		self.name = name

## Persion is a Object
class persion(Object):
	def __init__(self ,name):
		##person has-a name
		self.name = name
		
		##Person has a pet of some kind
		
		self.pet = None

##Eployee is-a persion

class Employee(person):
	def __inti__(self, name, salary):
		## Employee has-a name. hmm What is this strange magic	
		super (Employee, self).__init__(name)
		#employee has-a salary
		self.salary = salary

##A Fish is a animal
class Fish (object):
	pass
## A Salmon is a fish
class Salmon(Fish)

##A Halibut is a fish
class halibut(Fish):
	pass


##Rover is a dog
rover = Dog("Rover")

##satan is-a Cat
satan = Cat("Satan")

##Mary is-a person
mary = Person("Mary")

##Mary has-a pet 
mary.pet = satan

#frank is-a emplyee ("Frank" , 100000)

##frank has a pet
frank.pet = rover

#flipper is-a fish
flipper = Fish()

##Crouse  is a object
crouse = Salmon()

##
hary = Halibut()