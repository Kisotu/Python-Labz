# items can be accessed using for loop
myset = {"apple", 45, "67", "banana", 890, "cherry"}

for x in myset:
	print(x)


# can also use the in keyword to ask if specified value is present

print(890 in myset) # return true as the value exists in the set

# can also use the NOT IN to check if an item is not present

print("apple" not in myset) # returns False because it is present
print("pineapple" not in myset) # returns true cox it is not present