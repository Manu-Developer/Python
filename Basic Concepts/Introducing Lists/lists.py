bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

bicycles[0] = "sth"
print(bicycles)

bicycles.append("4x4")
print(bicycles)

bicycles.insert(1, "GSAC")
print(bicycles)

del bicycles[3]
print(bicycles)

last_element = bicycles.pop()
print(bicycles)
print(last_element)

bicycles.remove("cannondale")
print(bicycles)


cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
