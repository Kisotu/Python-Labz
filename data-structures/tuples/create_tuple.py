# tuples are used to store multiple items in a single variable
# Tuples are ordered and unchangeable: cannot be changed, added or removed after creating
# tuples allow duplicates
# written in round brackets
my_tuple = ("apple", "bananas", "eggs", "milk")
one_item = ("single",)
print(my_tuple)
print(type(one_item))

# tuples are indexed and can be accessed using the [] notation
print(my_tuple[1]) # prints second item //bananas

#len() to determine length
print("Length :", len(my_tuple))

# can also be created using the tuple() constructor
tuple2 = tuple(("Jan", "Feb", "Marc", "Apr", "Monday"))
print(tuple2)