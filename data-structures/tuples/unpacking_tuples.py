# this is assigning values from the tuple collection to separate variables
# this is called tuple unpacking

my_tuple = ("Jan", "Feb", "Mar", "Apr", "May")

first, second, third, fourth, fifth = my_tuple
print(first)
print(second)
print(third)
print(fourth)
print(fifth)

# variables on the left must match the number of items in the tuple
# or use the *variable_name to assign the remaining items to a list

a, b, *c = my_tuple
print(a)
print(b)
print(c) #prints a LIST of remaining items