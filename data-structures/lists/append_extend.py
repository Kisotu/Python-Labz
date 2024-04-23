# adding item to end of list using append() and extend()

cities = ["Nairobi", "Narok", "Nakuru", "Kisumu", "Mombasa"]
print(cities)

cities.append("New York")
print(cities)

cities2 = ["Lagos", "Durban", "Dodoma", "London"]
print(cities2)

cities.extend(cities2)
print(cities)

# insert(0 method adds item at specific index

names = ["Oloo", "Felix", "Jeff", "Rex"]
print(names)

names.insert(1, "James")
print(names)


# can also add other iterable objects (tuples, sets, dictionaries)

set1 = {"Kuwinda", "Bosco", "Meru"}
print(set1)

names.extend(set1)
print(names)
