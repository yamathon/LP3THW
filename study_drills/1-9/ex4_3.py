# there are 100 cars total
cars = 100
# each car can hold 4 people
space_in_a_car = 4.0
# only 30 drivers can drive 30 cars
drivers = 30
# there are 30 drivers that can drive 90 passengers
passengers = 90
# 100-30=70 undriven cars
cars_not_driven = cars - drivers
# only 30 drivers can drive 30 cars
cars_driven = drivers
# 30 * 4.0 = 120.0 total passenger capacity
carpool_capacity = cars_driven * space_in_a_car
# 90 / 30 = 3.0 passengers per car on average
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars availible.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
