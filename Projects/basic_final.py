# a = 10
# def b():
# if = 20
# print(a+if)
# a
# B
# a_B
# a_0
# a1
# a1=10
# A1 = 20
# print(a1,A1) 

# a = 10
# b =20
# c = 'birayni'

# a,b,c = 10,20,'birayani'

# z = "kiran"
# y = z
# x = y
# x = 20
# dgsagdjsg =10
# bigcat = 10
# my_age
# x = y = z = "kiran"
# print(x)
# int a,b,c;
# a =10,b=2

# a ="2"
# b = "2"
# print(a+b)
# a = [21,43,4,35,46,56,7,6876,78,532,4,214,46,76,8,79,7,8,23,4,123,254,4,76,8,97,97]
# print(len(a))
# print(a[28])
# print(a[-5])
# print(a[3:6])
# print(a[:-6])
# print(a[-6:])
# print(a[4])
# a[4] = 64
# print(a[4])

# a = (1,321,233,4,54,35,343)
# print(a[1])
# a[1]=21
# print(a[1])

#string
# name = "kiran budati"
# print(name[2:5])
# name[2]='a'
# print(name)

#set
# a = {1,456,2,2,"kiran","kiran",'budati'}
# print(a)

#dict
# a = {"name":"kiran","mobile":8008340884,"branch":"cse"}
# print(a["name"])
# for k,v in a.items():
#     print(k,v)
# a = '10'
# print(type(a))
# a = int(a)
# print(type(a))
# import math
# import haskjdadkashdkahdskjah as kk
# from math import pi

#operators
# print(2+2,2-1,2/2,2*2,100%7,100//9,3**3) #arthimatic
# print(3>10,10<100,8==3,12>=12,158<=170,5!=40)#comparision
# a,b=2,3
# print(a and b==2)
# print(a or b==2)
# print(not b)


#loops
# a = [21,43,4,35,46,56,7,6876,78,532,4,214,46,76,8,79,7,8,23,4,123,254,4,76,8,97,97]
# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(a[i])
# else:
#     print("No items left.")

# for i in a:
#     if i%2 == 0:
#         # print("even found,breaking operation")
#         # break
#         print("even found,comtinue operation")
#         continue
#     else:
#         print(i)

# def add_num(*a):
#     ar = []
#     print(a)
#     for i in range(len(a)):
#         ar.append({"a"+str(i+1):a[i]})
#     print(ar)
    # print(a)
    # return a
    # ad =a+b
    # su = a -b
    # mul = a*b
    # return ad,su,mul

# sum_rang = []

# for i in range(10):
#     a = i
#     b = i+1
#     add_num(a,b,i+2,i+3)
#     sum_rang.append(add_num(a,b))
# print(sum_rang)
# def my_func():
#     x = 10
#     print("Value inside function:",x)

# x = 20
# my_func()
# print("Value outside function:",x)

# def calc_factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         return (x * calc_factorial(x-1))

# num = 4
# print("The factorial of", num, "is", calc_factorial(num))
# calc_factorial(4)              # 1st call with 4
# 4 * calc_factorial(3)          # 2nd call with 3
# 4 * 3 * calc_factorial(2)      # 3rd call with 2
# 4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
# 4 * 3 * 2 * 1                  # return from 4th call as number=1
# 4 * 3 * 2                      # return from 3rd call
# 4 * 6                          # return from 2nd call
# 24                             # return from 1st call
# def fun(a):
#     if a == 0:
#         return "Yes"
#     else:
#         print("if is failed")
#         return fun(a-1)
# print(fun(5))

#lambda
# dou = lambda x,y:x*y
# print(dou(5,5)) 

#filter
a = [21,43,4,35,46,56,7,6876,78,532,4,214,46,76,8,79,7,8,23,4,123,254,4,76,8,97,97]
# b = []
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)
# b=filter(lambda x:x%2==0,[3213,213,12,324,3,4,453,4,43])
# print(list(b))

# a = list(filter(f,range(1,10)))
# print(a)

# def f(x): 
#     return x%2!=0 and x%3!=0
# b = filter(f,a)
# print(list(b))

# c = list(filter(lambda x: x%2!=0 and x%3!=0,a))
# print(c)
# d = map(f,range(0,10))
# print(list(range(0,10)))
# print(list(d))

#global
# x = 2
# def foo():
#     x = x * 2
#     print(x)
# foo()
#UnboundLocalError: local variable 'x' referenced before assignment

# def foo():
#     ada = 2
# foo()
# print(ada)
# #NameError: name 'ada' is not defined

# x = "global"

# def foo():
#     global x
#     y = "local"
#     x = x * 2
#     print(x)
#     print(y)
    
# foo()

# x = 5
# def foo():
#     x = 10
#     print("in",x)
# print("out",x)
# foo()

# def outer():
#     x = "local"
    
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
    
#     inner()
#     print("outer:", x)

# outer()

# c = 1 # global variable
# def add():
#     print(c)
# def ss():
#     print(c-c)
# add()
# ss()

# global variable
c = 1
def add():
    global c
    c = c + 2 # increment c by 2
    print(c)

add()