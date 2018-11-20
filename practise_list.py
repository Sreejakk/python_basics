fruit = ["pineapple", "banana", "cherry","apple"]
# fruit[1] = "blackcurrant"
# print(len(fruit))


# fruit.insert(1, "orange")
# print(fruit)

# fruit.remove("cherry")
# print(fruit)

#length
b=len(fruit)
print(b)

fruit.pop()
print(fruit)


del fruit[1]
print(fruit)

fruit.clear()
print(fruit)

fruit = list(("apple", "banana", "cherry")) # constructor
print(fruit)

fruit.append("guava")
print(fruit)

#Prints the Number of times value exist
a=fruit.count("banana")
print(a)

fruit.sort()
print(fruit)

fruit.extend("apple")
print(fruit)

fruit.index("apple")
print(fruit)

fruit.copy()
print(fruit)