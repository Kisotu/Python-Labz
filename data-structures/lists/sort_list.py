# uses sort() to sort alphanumerically. Ascening by default

mylist = [64, 34, 25, 12, 22, 11, 90, 7, 5, 3]
print(mylist)

mylist.sort()
print(mylist)

list2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(list2)

list2.sort()
print(list2)

print("Sort in DESCENDING")

list3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list3.sort(reverse = True)
print(list3)

# custom sort function
# can be set using the keyword argument key = function

def myfunc(n):
    return abs(n - 40)


list4 = [100, 50, 65, 82, 23]
list4.sort(key = myfunc)
print(list4) # sorts list based on which number is closest to 40
# reverse() reverses the order of a list regardless of the alphabet

list5 = ["banana", "Orange", "Kiwi", "cherry", "pineapple", "mango", "avocado"]
print(list5)

list5.reverse()
print(list5)
