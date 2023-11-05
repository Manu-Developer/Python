magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

numbers = list(range(0, 11, 2))
print(numbers)

# List Comprehension: A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element
squares = [value**2 for value in range(1, 11)]
print(squares)

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players)

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
