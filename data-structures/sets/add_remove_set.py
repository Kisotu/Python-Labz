# once created a set cant be changed, but can be added into or items removed
# add() method is used
myset = {"apple", "avocado", "kiwi", "guava", "tomato"}
myset.add("orange")# orange added
print(myset)


# to add another set, we the update() method. it can add any iterable (set, list or dictionary)
set2 = {True, 567, "second"}
myset.update(set2)
print(myset)


# remove() -> raises error if item to remove does not exist
# discard() -> does not raise error if item to remove doesnt exist

myset.remove(567) # removes 567 integer
print(myset)

myset.discard(True) # remove True boolean
print(myset)


# pop() method will remove a random item due to no indexing

# clear() -> empties the set
# del() -> deletes the set completely