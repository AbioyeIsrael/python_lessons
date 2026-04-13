#the code below is me assigning the value "100" to a variable "car"
cars = 100
a = cars
#here i applied the same principle as above, by assigning the value of 4.0 (a floating number) to the variable space_in_a_car
space_in_a_car = 4
b = space_in_a_car
#i assigned the value 30 to the variable drivers 
drivers = 30
c = drivers
#same applies as the above, i aasigned the value 90 to the cariable passengers
passengers = 90
d = passengers
#what is happeneing here is not just variable assigning, but also mathimatical calculation going on, using subtraction and calling the value of the named variales and substracting them'
cars_not_driven = cars - drivers
e = cars_not_driven
#similar mathimaticalcalculation as the above, here we are performing a calculation that assigns a value to a variable using another variable as the value 
cars_driven = drivers 
f = cars_driven
#here there is also assigning of value to a variable, via the multiplication of two variables 
carpool_capacity = cars_driven * space_in_a_car
g = carpool_capacity
#here value is assigned to another vabriable via mathimatical division of two named variables with assigned values 
average_passengers_per_car = passengers / cars_driven
h = average_passengers_per_car


#print("There are", cars, "cars available.")
print("THERE ARE", a, "CARS AVAILABLE.")
#print("There are only", drivers, "drivers available.")
print("THERE ARE ONLY", c, "DRIVERS AVAILABLE.")
#print("There will be", cars_not_driven, "empty cars today.")
print("THERE WILL BE", e, "EMPTY CARS TODAY.")
#print("We can transport", carpool_capacity, "people today.")
print("WE CAN TRANSPORT", g, "PEOPLE TODAY.")
#print("We have", passengers, "to carpool today")
print("WE HAVE", d, "TO CARPOOL TODAY.")
#print("We need to put about", average_passengers_per_car, "in each car")
print("WE NEED TO PUT ABOUT", h, "IN EACH CAR.")
#For exercise 4, i am supposed to explain this error;File "ex4.py", line 8, in <module> average_passengers_per_car = car_pool_capacity / passenger NameError: name 'car_pool_capacity' is not defined in my own words, use line numbers and explain why.
#well the above error indicates a name error that happens in line 8, that the car_pool_capacity variable was not defined, meaning in my understanding, that no value was given to the named variable 'car_pool_capacity

#more study drills; I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
#Answer = i dont think its necessary, correct me if i am wrong, if its just 4 instead of 4.0 the only difference is that instead of having 120.0 you have 120

#Remember that 4.0 is a “fl oating point” number. Find out what that means.
# so i had to research to juggle my memory back, floating point number are numbers with decimal and can also represent fractional values.

#Write comments above each of the variable assignments.
#Done

#Make sure you know what = is called (equals) and that it’s making names for things.
#so i think i know this already as it does, so far from my observation, it assigns values to variables.

#Remember that _ is an underscore character.
#yeah i do remember that 

#Try running Python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.