# ####Factorial

n=int(input("Enter the number to calculate factorial "))
fact=1
if n<0:
   print("Fact does not exist for -ve numbers")
elif n==0:
    print("fact of 0 is 1")
for i in range(1,n+1):
    fact=fact*i
print("factorial of number",n,"is",fact)



###
# n = int(input("enter fact number-"))
# fact_num = 1
# temp = n
# while temp == n:
#     a = temp *(temp-1)
#     fact_num = fact_num * a
#     temp = temp - 1
# print(fact_num)