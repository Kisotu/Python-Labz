# for loop can be used to iterate
my_tuple = (1, 2, 3, 4, 5)
for x in my_tuple:
	print(x)


# loop using range() and len() methods

b = (78, "hello", 3.14, True)
for i in range(len(b)):
	print("b :", b[i])

# using the while loop
txt = ("Hello", "morning", "habari", "karibu", "salutation")
i = 0
count = len(txt)
while i < count:
	print(txt[i])
	i = i + 1