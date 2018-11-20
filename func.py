def myName():
    print("Hi kiran")

myName()

def sayHi(name):
    print("hi",name)

sayHi("kiran")

def say_hello_to_user():
    return "Hello"
mes = say_hello_to_user()
print(mes)

def addition(a,b):
    # c = a+b 
    return a+b    
add = addition(10,20)
print(add)


def calc(a,b):
    return a+b,a-b,a*b
add,sub,multi = calc(12,5)
print(add,sub,multi)

def retList():
    return [1,2,3,4]
a = retList()
print(a)