# remove() => removes specified item
cars = ["Rover", "Cruizer", "BMW", "Audi", "Mercedez", "Rivian","Tesla"]
print(cars)

cars.remove("BMW")
print(cars)


# pop() => removes item at spec index, or last item if not specified
cars.pop(1) # removes "Cruizer"
print(cars)
cars.pop() # removes 'Tesla"
print(cars)


# del keyword

names = ["Nisht", "Beth", "Puton", "Lingchen", "Xuan"]
print(names)

del names[2] # deletes "Puton"
print(names)

del names # deletes entire list // throws error if tried to access

# clear() => empties list
laptops = ["Vaio", "Mac", "HP", "Asus", "Dell", "Lenovo"]

laptops.clear()
print(laptops) # prints empty list []
