   

def menu():
    print("** Welcome **")
    print("** Please select your Option **")  
    print("\n1 Teachers View \n2 Parents View \n3 Students View \n0 Quit \nEnter the option -")
    n=int(input(""))
    print(n)
    # if n==1:
    #     print("Hii Teachers")
    #     studentdetails()
    # elif n==2:
    #     print("Hii Parents")
    # elif n==3:
    #     print("Hii Students")
    # elif n==0:  
    #     exit()
    # else:
    #     print("You must select either 1,2 or 3")
    #     print("Please select again")
    #     menu()

# def studentdetails():
#     print("Enter Batch Details")
#     print("Select your option")
#     Batch_S=None
#     while Batch_S==None:
#         try:
#             Batch_S=int(input())
#             if Batch_S < 2001 or Batch_S >2010:
#                 print("Sorry , Data is unavailable")
#                 Batch_S=None
#         except:
#             print("Kindly select from the options only")
#             Batch_S=None
#     print("Enter Roll_No")
#     Roll_No=None
#     while Roll_No==None:
#         try:
#             Roll_No=int(input())
#         except ValueError as err:
#             print ("Not a number,Try again!",err)
#             Roll_No=None
#     print("Enter full name of student")
#     Full_Name=(input())
#     print("Name of the student is",Full_Name)
#     Class_S=None
#     print("Enter class of student")
#     while Class_S==None:
#         try:
#             Class_S=int(input(""))
#         except ValueError as err:
#             print ("Not a number,Try again!",err)
#             Class_S=None
#     print("Enter section of student: ")
#     Section_S=input("")
#     if Section_S=="A" or Section_S=="a":
#     #Section_S.upper():
#         print("Below is list of Students for",Class_S, Section_S)
#         with open("student.txt","a+") as Register:
#             print(Register.readlines())
#             Register.write("\nMoniiiiii")
#             print("Find the below updated list")
#         with open("student.txt","r") as Register:
#             print(Register.readlines())
# menu()