# copy() => make a copy of another list

a = ["apple", 45, "78.5", 89.50, "Balance"]
print("a => ", a)
b = a.copy()
print("b => ", b)

# can also copy using the list() constructor

c = ["apple", "banana", "cherry"]
print("c : ", c)

d = list(c)
print("d : ", d)
