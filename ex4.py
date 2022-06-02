#Toatal Number of cars
cars = 100
#Space in every car
space_in_a_car = 4.0
#Number of drivers
drivers = 30
#Total passenger
passenger = 90
#Free Car
car_not_drivens = cars - drivers
#Used_car
car_drivens = drivers
#How may passenger can go
carpool_capacity = car_drivens * space_in_a_car
#Average passenger in every car
avarage_passenger_per_car = passenger / car_drivens


print(f"There are {cars} Cars available")
print ("Thera are only" ,drivers, " Drivers available")
print(f"There will be {car_not_drivens} empty cars today")
print(f"We can transport {carpool_capacity} people today")
print(f"We have {passenger} to carpool today ")
print (f"We need to put out about {avarage_passenger_per_car} in each car")
