# a tuple cannot be changed, added to, rmv items but there is a workaround
# it is converted toa list, modified and then converted back to a tuple

x = ("apple", "banana", "orange")
print(x)

# convert to list
y = list(x)
print(type(y)) # shows it's a list

# add to list
y.append("kiwi")
y.insert(0, "pineapple")


# remove from list
y.pop(1) # remove apple

new_tuple = tuple(y)
print(new_tuple) # pineappl and kiwi added, apple removed from tuple
print(type(new_tuple))