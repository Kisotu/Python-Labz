# offers a short syntax to create list from existing values based on a condition
# offers for loop short syntax

fruits = ["apple", "kiwi", "orange", "pineapple", "appricot", "avocado", "cherry"]

fruit_has_p = [x for x in fruits if "p" in x]
print(fruit_has_p)

length_less_6 = [sh for sh in fruits if len(sh) < 6]
print(length_less_6)


# range() to create iterable

newlist = [x for x in range(10) if x % 2 == 0]
print(newlist)

# the expression is current item in iteration, but also the outcome
# can be manipulated before ending up in the new list

new_fruits = ["Banana", "APPLE", "APpricot", "Mango", "Lemon"]

fruits2 = [x.upper() for x in new_fruits]
print(fruits2)
