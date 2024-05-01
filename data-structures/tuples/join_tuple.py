# can join two or more tuples using the + operator
tup1 = ("a", "b", "c")
tup2 = (1, 2, 4)
tup3 = tup1 + tup2
print(tup3)

# can multiple contents of a tuple by a number of times using the * operator
by_two = (2, 4, 8)
res = by_two * 2
print(res) # returns a double number of items


# tuple built in methods
# count() -> returns the number of times a specified value occurs in a tuple
print(res.count(4)) # appears twice

fruits = ("apple", "orange", "kiwi", "orange", "banana", "orange", "dragonfruit")
how_many = fruits.count("orange")
print("number of oranges: ", how_many)

# index() -> searches tuple for specified value and returns its position
print("kiwi is at index:", fruits.index("kiwi"))