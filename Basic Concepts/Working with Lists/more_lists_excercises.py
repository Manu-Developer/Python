# Try yourself

# Excercise 4.1
pizzas = ["Muzzarela", "Pepperoni", "Cheddar"]

for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza")

# Excercise 4.2
animals = ["dog", "cat", "aligattor"]
for animal in animals:
    print(animal.title())
    print("A " + animal + " would make a great pet.")

print("All of this animals have four legs")

# Excercise 4.3
for number in range(1, 21):
    print(number)

# Excercise 4.4
# for number in range(1, 1000001):
# print(1)

# Excercise 4.5
numbers = list(range(1, 1000001))
# print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Excercise 4.6
for number in range(1, 21, 2):
    print(number)

# Excercise 4.7
multiple_three = [multiple * 3 for multiple in range(1, 11)]
print(multiple_three)

# Excercise 4.8 & 4.9
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

# Excercise 4.10
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list_length = int(len(number_list) / 2) - 1

for number in number_list[:3]:
    print("The first 3 numbers in the list are: " + str(number))

for number in number_list[number_list_length : number_list_length + 3]:
    print("The first 3 numbers from the middle of the list are: " + str(number))

for number in number_list[-3:]:
    print("The last 3 numbers in the list are: " + str(number))

# Excercise 4.11 & 4.12
pizzas = ["Muzzarela", "Pepperoni", "Cheddar"]
friend_pizzas = pizzas[:]
pizzas.append("Romania")
friend_pizzas.append("Four Cheese")
print(pizzas)
print(friend_pizzas)

for pizza in pizzas:
    print("My favourite pizzas are: " + pizza)

for friend_pizza in friend_pizzas:
    print("My friend favourite pizzas are: " + friend_pizza)

# Excercise 4.13
simple_foods = ("Salad", "Fries", "Barbecue", "Pasta", "Banana")
for food in simple_foods:
    print(food)

simple_foods = ("Salad", "Fries", "Barbecue", "Soup", "Camarone")
for food in simple_foods:
    print(food)
