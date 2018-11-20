tuple_a = ("science", "social", "maths","physics","science","economics","science","english")
# print(tuple_a)

# ##value
# print(tuple_a[7])

# ##values are unchangable
# tuple_a[3]= "Hindi"
# print(tuple_a)


# #loops
for x in tuple_a:
 print(x)

#length
print(len(tuple_a))

# #delete gives error, since tuple is unchangable
del tuple_a
print(tuple_a)

#no. times value is present in the list
x=tuple_a.count("science")
print(x)

#Search for the first occurrence of the value and return its position
x=tuple_a.index("english")
print(x)