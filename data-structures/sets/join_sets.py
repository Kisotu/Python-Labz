# ways to join 2 or more sets together
# union() and update() methods joins all items from both sets. excludes duplicates
# intersection() method keeps ONLY the duplicates.
# difference() method keeps the items from the first set that are not in the other set(s).
# symmetric_difference() method keeps all items EXCEPT the duplicates.

#union()
set1 = {"A", "B", "C", "D"}
set2 = {45, 67, 8, "B"}
newset = set1.union(set2)
print("newset", newset)

# can also use the | operator

set3 = set1 | set2
print(set3)

set4 = {"x", "test", True}

set5 = set4.union(set1, set2, set3) # joins multiple sets
print(set5)





#intersection() and & operator-> returns a new set, keeps ONLY the duplicates

set6 = {45, 56, 87}
set7 = {56, False, "Hello"}

set8 = set6.intersection(set7) # same as set8  = set6 & set7
print(set8)


#intersection_update() -> keeps only the duplicates but will change original set instead of returning a new set

myset = {23, 45, 53}
yourset = {53, False, "nginx"}

myset.intersection_update(yourset)
print(myset)










#difference() -> returns a new set containing only the items from first set not present in the other set
diff1 = {"apple", "banana", "cherry"}
diff2 = {"google", "mirosoft", "apple"}

diff3 = diff1.difference(diff2)
print(diff3)





#difference_update() ->  keeps items from first set not present in the second set. modifies first set
set10 = {"apple", "banana", "cherry"}
set11 = {"google", "mirosoft", "apple"}

set10.difference_update(set11)
print(set10)



# symmetric_difference() -> keep only elements NOT present in both sets

st1 = {"orange", "red", "black"}
st2 = {"banana", "orange", "cherry"}

st3 = st1.symmetric_difference(st2)  # also same as st3 = st1 ^ st2
print(st3)



#symetric_difference_update() -> keep items not present in both but modifies original set
st4 = {"apple", "banana", "cherry"}
st5 = {"google", "microsoft", "apple"}

st4.symmetric_difference_update(st5)

print(st4)

# more set methods

"""
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""