dict_b =	{
  "brand": "audi",
  "model": "A4",
  "year": 1995
}
# print(dict_b)

# #referring to its key name 
# x = dict_b["model"]
# print(x)

# #referring to its key name by get()
# x = dict_b.get("model")
# print(x)

# #Change the "year" to 2015
# dict_b["year"]=2015

# #looping with keys
# for x in dict_b:
#  print(x)

# #values in the dictionary
# for x in dict_b:
#  print(dict_b[x])

# # #values() function to return values of a dictionary
# for x in dict_b.values():
#  print(x)

# #both keys and values, by using the items() function
# for x,y in dict_b.items():
#    print(x,y)

# #if a specified key is present in a dictionary use the in keyword
# if "model" in dict_b:
#   print("yes")

#   #add item to the dictionary is done by using a new index key and assigning a value to it
# dict_b["colour"]="red"
# print(dict_b)

# #delete
# del dict_b["model"]
# print(dict_b) 

# #pop
# dict_b.pop("brand")
# print(dict_b) 

# #It is also possible to use the dict() constructor to make a dictionary
dict_b =	dict(brand="audi",model="A4",year=1995)
print(dict_b)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment

x = dict_b.setdefault("color", "white")
print(x)
