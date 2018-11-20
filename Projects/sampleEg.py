
####LCM of Numbers
# def lcm(x,y,z):
#     if x>y and x>z:
#         greater=x
#     elif y>x and y>z:
#         greater=y
#     else:
#         greater=z
#     while(True):
#         if((greater % x == 0) and (greater % y == 0)and (greater % z == 0)):
#                lcm = greater
#                break
#         greater += 1
#     return lcm
# x = 5
# y = 25
# z = 50
# print("LCM of ",x,",",y,"and",z,"is",lcm(x,y,z))


##Armstrong number
l = 100
u = 2000
for n in range(l, u + 1):
   order = len(str(n))
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
       if n == sum:
           print(n)
