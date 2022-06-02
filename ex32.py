the_count = [1,2,3,4,5]
fruits= ['apples', 'oranges','pears','apricots']
change = [1, 'penneis', 2, 'dimes', 3 , 'quarters']
# this first kind of forr-loop goes through a list

for number in the_count:
	print(f"This is count {number}")

# same as above

for fruit in fruits:
	print(f"This is count: {fruits}")

#also we can go through mixed lists too
for i in change:
	print(f"I got {i}")

#we can also built lists, first start with an empty one

elements = []

#then use the range function to do 0 to 10 counts

for i in range (0, 10):
	print(f"Adding{i} to the list.")
	
	#append is the fuction that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print(f"Elements was: {i}")