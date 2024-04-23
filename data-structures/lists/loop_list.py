# looping thru a list
# using for loop
mylist = ["Pan", "Spoon", "Jewel", "Plate"]
for item in mylist:
    print(item)


# using index, range() and len()
print("\n")
print("Using range() and len()")
for x in range(len(mylist)):
    print(mylist[x])


print("\n")

# using while loop
print("Using while loop")

i = 0

while i < len(mylist):
    print(mylist[i])
    i += 1


# using list comprehensions/ short syntax form
print("\n")
print("Using list comprehensions")

[print(m) for m in mylist]

