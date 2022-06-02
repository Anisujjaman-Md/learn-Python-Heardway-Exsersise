#create a mapping of state to abbreviation

states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New york' : 'NY',
	'Michigan' : 'MI'
}

#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    "NY": "New York",
    'OR': 'Portland'
}

#print out some cities

print ("-" * 10)
print("NY State has: ", cities ["NY"])
print("OR state has: ", cities["OR"])

#print some states
print('-' * 10)
print("Michigan,s abbreviation is: ", states['Michigan'])
print("Floria's abbreviation is : ", states['Florida'])

#do it by using the state then cities dict

print('-' *10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbriviation
print('-' * 10)
for state, abbrev in list (states.items()):
	print(f"{state} is abbreviated { abbrev}")

#print every cities in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
#now do borh at the same time
print('-' *10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and city {cities[abbrev]}")

print('-' * 10)

#dafely get a abbreviation by state that might not be there

state = states.get('Texas')

if not state:
	print("Sorry, no texas")

#get a city with defult value
city = cities.get('TX', 'Does not Exist')
print(f"The City for the state'TX' is : {city}")