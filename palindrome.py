# r=0
# n=int(input("Enter the number "))
# t=n 
# while n > 0:
#     r = r*10
#     r = r + t%10
#     t = t/10
#     if n==r:
#         break
#         print("Number is palindrome")
#     else:
#         n = 0
#         print("Number is not a palindrome")

#121 

n = int(input("Enter number: "))
temp = n
rev = 0

while temp !=0:
    rev = (rev*10) +(temp %10)
    temp = temp // 10

    if n==temp:
        print("Palindrome")
    else:
        print("not palindrome")    


