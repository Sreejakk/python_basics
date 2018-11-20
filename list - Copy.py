a = ['a','b','c','d','e','f']
#print(a[0:4])
#print(a[-2])
# for(int i=0;i<5;i++){
#     print(i)
# }
# list with position/index and value
for i,b in enumerate(a):
    print("index: {}, value : {}".format(i,b))

print("\n")

#list with index
for i in range(len(a)):
    if a[i] == 'c':
        a[i] = 'k'
print("index : {}".format(a))

print("\n")

#list with values/items
for i in a:
    print("value : {}".format(i))