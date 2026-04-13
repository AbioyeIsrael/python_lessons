#i am supposed to select a random number (75)
integer = input("Input Integer: ")
integer = int(integer)
#print(type(integer))

if integer % 3 == 0 and integer % 5 == 0:
    print("Fizzbuzz")
elif integer % 3 == 0:
    print("Fizz")
elif integer % 5 == 0:
    print("Buzz")
else:
    print(integer)
