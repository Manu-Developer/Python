# Try Yourself

# Excercise 5.3
alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points")

if alien_color == "red":
    print("You have earned nothing")

# Excercise 5.4
alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points")

if alien_color != "green":
    print("You have earned 10 points")

if alien_color == "green":
    print("You have earned 5 points")
elif alien_color == "red":
    print("You have earned 10 points")

# Excercise 5.5
alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points")
elif alien_color == "yellow":
    print("You have earned 10 points")
elif alien_color == "red":
    print("You have earned 15 points")

# Excercise 5.6
person_age = 20
if person_age < 2:
    print("You are a baby")
elif person_age >= 2 and person_age < 4:
    print("You are a toddler")
elif person_age >= 4 and person_age < 13:
    print("You are a kid")
elif person_age >= 13 and person_age < 20:
    print("You are a teen")
elif person_age >= 20 and person_age < 65:
    print("You are an adult")
else:
    print("You are an elder")

# Excercise 5.7
favorite_friuts = ["apple", "banana", "mango"]
if "apple" in favorite_friuts:
    print("You really like apples")

# Excercise 5.8
usernames = ["juan", "manuel", "seba", "rafa", "fer", "admin"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + " thanks for login in again.")

# Excercise 5.9
usernames = ["juan", "manuel", "seba", "rafa", "fer", "admin"]

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + " thanks for login in again.")
else:
    print("We need to find more users")

# Excercise 5.10
current_users = ["joha", "Nacho", "Daniel", "Yoel", "Gonzalo"]
new_users = ["Joha", "Nacho", "Tatiana", "Jessica", "Agustina"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You will need to enter a different user name")
    else:
        print("This username is available")

# Excercise 5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
