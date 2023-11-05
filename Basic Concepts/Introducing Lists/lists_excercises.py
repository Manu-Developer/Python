# Try Yourself

# Excercise 3.1
names = ["Juan", "Pedro", "Luis"]

# Excercise 3.2
message = "Hello "
print(message + names[0] + "!")
print(message + names[1] + "!")
print(message + names[2] + "!")

# Excercise 3.3
transportation_modes = ["motorcycle", "bus", "train"]
print("I would like to own a Honda " + transportation_modes[0])
print("I hate the " + transportation_modes[1])
print("I have never used the " + transportation_modes[2])

# Excercise 3.4
guests = ["Michel", "Anthonny", "James"]
print("Would you like to have some dinner " + guests[0] + "?")
print("Would you like to have some dinner " + guests[1] + "?")
print("Would you like to have some dinner " + guests[2] + "?")

# Excercise 3.5
guest_dont_make_it = guests[0]
print(guest_dont_make_it)

guests[0] = "Jose"
print("Would you like to have some dinner " + guests[0] + "?")
print("Would you like to have some dinner " + guests[1] + "?")
print("Would you like to have some dinner " + guests[2] + "?")

# Excercise 3.6
print("I have found a bigger table!")
guests.insert(0, "Matias")
guests.insert(2, "Fer")
guests.append("Rafael")

print("Would you like to have some dinner " + guests[0] + "?")
print("Would you like to have some dinner " + guests[1] + "?")
print("Would you like to have some dinner " + guests[2] + "?")
print("Would you like to have some dinner " + guests[3] + "?")
print("Would you like to have some dinner " + guests[4] + "?")
print("Would you like to have some dinner " + guests[5] + "?")

# Excercise 3.7
print("I will have to invite only two people")
first_removal = guests.pop()
print("I am so sorry " + first_removal + "!")
second_removal = guests.pop()
print("I am so sorry " + second_removal + "!")
third_removal = guests.pop()
print("I am so sorry " + third_removal + "!")
fourth_removal = guests.pop()
print("I am so sorry " + fourth_removal + "!")
print(guests)

print("Would you like to have some dinner " + guests[0] + "?")
print("Would you like to have some dinner " + guests[1] + "?")

del guests[1]
del guests[0]
print(guests)

# Excercise 3.8
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Excercise 3.9
print(len(guests))
print(cars[2332])
