# data structures used to store data in key:value pairs
# collection that is ordered, changeable and does NOT allow duplicates
# written in curly brackets

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)






# dictionary items
# presented in key:value pairs and can be referred to using key name

print(mydict["brand"]) # prints Ford


#values in dictionary items can be any data type

dict1 = {
	"name": "XVH89G",
	"status": "Green",
	"isON": True,
	"value": 7500,
}
print(dict1)

# can also be creted using the dict() constructor
thisdict = dict(name="Test", age=45, country="USA")
print(thisdict)

