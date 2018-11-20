# a = 2
# b = 'dgja'

# try:
#     print(a/b)
# except:
#     print("oops..!")

# n = None
# while n == None:
#     try:
#         n = int(input("Enter nuber -"))
#         print("the numer is: ",n)
#     except ValueError as err:
#         print(err)
#         print("not a number, try again!")
#         n = None 

a = [21,3,243]
try:
    print(a[1])
except IndexError as err:
    print(err)
# n = int(input("enter num"))
# print(n)