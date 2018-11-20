a = []
print("items in a {}".format(a))
for i in range(10):
    a.append(i)
a.insert(5,20)
print("items in a {}".format(a))

b = [i  for i in range(1,10,2)]
print(b)
#b = [(0,1),(1,3),]