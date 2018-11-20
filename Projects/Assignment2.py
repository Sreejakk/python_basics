import re
import time

def Menu(): 
    try:
       Student_Details=open('Details.txt','r')
       Fee_Details=open('Fee.txt','r')
       Marks_Details=open('Marks.txt','r')

    except:
       Student_Details=open('Details.txt','w')
       Fee_Details=open('Fee.txt','w')
       Marks_Details=open('Marks.txt','w')
    print("\n*********************Welcome*************************")
    print("<S> Students \n<P> Parents \n<F> Faculty \n<Q> Quit")  

    opt=None  
    while opt==None:
        opt=str(input("Enter your option: "))
        opt = opt.lower()
        print(opt)
        if opt=="s":
            print("The selected option is student")
        elif opt=="p":
            print("The selected option is parents")
        elif opt=="f":
            print("The selected option is faculty")
            Faculty()
        elif opt=="q":
            #quits the program
            quit()
        else:
            print("Invalid input,Try again!")
            opt=None

def Student():
     """Function to double the value kadkaskd"""
    print("Please select your choice")
    print("1-View Marks\n2-View fee\n3-Faculty details\n4-Exit to main menu\n5-Quit")
    option=None
    while option is None:
        try:
            option=int(input("Enter your choice-"))
            if option==1:
                print("View marks")
            elif option==2:
                print("fee details-")
                search_student()
            elif option==3:
                Menu()
            elif option==4:
                exit()
        except:
           print("Invalid option please try again")
           option=None

def Faculty():
    print("Please select your choice from the below")
    print("1-Add Student\n2-Search student\n3-Add Marks\n4-Exit to main menu\n5-Quit")
    choice=None
    while choice is None:
        try:
            choice=int(input("Enter your Choice-"))
            if choice==1:
                print("Please add student")
                add_student()
            elif choice==2:
                print("Please search student")
                search_student()
            elif choice==3:
                print("Please add marks of student")
                add_student_marks()
            elif choice==5:
                print("helllo")
                quit()
            elif choice==4:
                Menu()
            else:
                print("Invalid option please try again")
                choice=None
        except:
           print("Invalid option please try again")
           choice=None
def Parent():
    print("Please select your choice from the below")
    print("1-View Student Marks\n2-View Fee\n3-pay fee\n4-Exit to main menu\n5-Quit")
    select=None
    while select is None:
        try:
            select=int(input("Enter your Choice-"))
            if select==1:
                print("student marks details-")
                valid_student_marks()
            elif select==2:
                print("student fee details-")
                search_student()
            elif select==3:
                print("Pay fee")
            elif select==4:
                Menu()
            elif select==5:
                exit()
        except:
            print("invalid input, Try again!")
            select=None
def pay_fee():
    start_time = time.time()
    student_id=None
    while student_id is None:
        try:
            student_id=int(input("Enter student ID-"))
            if len(str(student_id))!=8:
                print("Id must be only 8 digits")
                student_id=None
            else:
                if valid_student(student_id) == None:
                    print("Student ID does not exists please try again")
                    student_id = None
        except:
            print("invalid input, Try again!")
            student_id=None
    student_fee = valid_student(student_id)[4]
    print("Remaining Fee",student_fee)
    fee=None
    while fee is None:
        try:
            stu_fee=int(input("Enter student fee-"))
            print(stu_fee)
            if stu_fee<0 or stu_fee>int(student_fee):
                print("Student fee should be greater than 0 and lessthan {}".format(student_fee))
                fee=None
            else:
                fee = int(student_fee) - stu_fee
        except:
            print("invalid input, try again")   
            fee=None      
    print(fee)
    print("--- %s seconds ---"%(time.time()-start_time))

    # for student in student_data:
    #     print(student)
            
def add_student():
    student_id=None
    while student_id is None:
        try:
            student_id=int(input("Enter student ID-"))
            if len(str(student_id))!=8:
                print("Id must be only 8 digits")
                student_id=None
            else:
                if valid_student(student_id) != None:
                    print("Student ID exists please try again")
                    student_id = None
        except:
            print("invalid input, Try again!")
            student_id=None
    student_year=None
    while student_year is None:
        try:
            student_year=int(input("Enter student year-"))
            if student_year not in range(1,5):
                print("invalid input,Try again!")
                student_year=None   
        except:
            print("invalid input,Try again!")
            student_year=None
    student_fee=None
    while student_fee is None:
        try:
            student_fee=int(input("Enter student fee-"))
            if student_fee not in range(50000,500001):
                print("Fee should be in between 50000 & 500000 only")
                student_fee=None   
        except:
            print("invalid input,Try again!")
            student_fee=None

    branches = ["cse","mech","ece","eee","civil"]
    print("Available branches",branches)
    student_branch=None
    while student_branch==None:
        try:
            student_branch=str(input("Select the branch-"))
            student_branch=student_branch.lower()
            if student_branch not in branches:
                print("Please select only from the available branches")
                student_branch=None
        except:
            print("Invalid iput,Try again!")
            student_branch=None
    student_name=None
    while student_name==None:
        try:
            student_name=str(input("Enter students Name-"))
            student_name=student_name.lower()
            if student_name.replace(' ','').isalpha()==False or len(student_name)<=4:
                print("Name should only be a sting,and. should be given as space")
                student_name=None
        except:
            print("Invalid input,Try again!")
            student_name=None
    with open('Details.txt','a+') as student:
        student.write("{} {} {} {} {}\n".format(student_id,student_name,student_branch,student_year,student_fee))
    
    print("{} {} {} {} {}".format(student_id,student_name,student_branch,student_year,student_fee))

def add_student_marks():
    subjects= {
        "ece":{
        1:['phy','chem','m1','MM'],
        2:['EDC','EC','STLD'],
        3:['VLSI','ADC'],
        4:['EE','NT']},

        "cse":{
            1:['chem','c','english'],
            2:['bee','c++','java'],
            3:['ppl','flat','cd'],
            4:['lp','ooad']}
        }
    student_id=None
    while student_id is None:
        try:
            student_id=int(input("Enter student ID-"))
            if len(str(student_id))!=8:
                print("Id must be only 8 digits")
                student_id=None
            else:
                if valid_student(student_id) == None:
                    print("Student ID does not exists, please add student")
                    student_id = None
                if valid_student_marks(student_id) != None:
                    print("Marks already added")
                    student_id=  None
        except ValueError as err:
            print(err)
            print("invalid input, Try again!")
            student_id=None
    student_data = valid_student(student_id)
    student_sub = subjects[student_data[2]][int(student_data[3])]
    
    marks_students = []
    # marks_students.append(student_id)
    for sub in student_sub:
        marks=None
        while marks is None:
            try:
                marks=int(input("Enter {} Marks-".format(sub)))
                if marks <0 or marks >100:
                    print("Marks should be only between 0 to 100")
                    marks=None
                else:
                    # sub_marks={sub:marks}
                    marks_students.append(sub+"-"+str(marks))
            except ValueError as err:
                print(err)
                marks=None
    print(marks_students)
    with open("Marks.txt",'a+') as Marks:
        Marks.write("{} {}\n".format(student_id,marks_students))
    # student_branch,student_year = student_data[3],student_data[4]
    # print(student_branch,student_year)
def get_marks():
    student_id=None
    while student_id is None:
        try:
            student_id=int(input("Enter student ID-"))
            if len(str(student_id))!=8:
                print("Id must be only 8 digits")
                student_id=None
            else:
                if valid_student(student_id) == None:
                    print("Student Does not exist")
                    student_id = None
        except:
            print("invalid input, Try again!")
            student_id=None
    student_marks=valid_student_marks(student_id)
    print(student_marks)

def valid_student_marks(stu_ID):
    found = None
    with open("Marks.txt", 'r') as marks:
        for mark in marks:
            mark = mark.replace('[','')
            mark = mark.replace(']','')
            mark = mark.replace(',','')
            mark = mark.split()
            for i in mark:
                if i == str(stu_ID):
                    found = mark
    return found


def valid_student(stu_ID):
    found = None
    with open("Details.txt", 'r') as students:
        for student in students:
            stue = student.split()
            for i in stue:
                if i ==  str(stu_ID):
                    found = stue
    return found

def search_student():
    student_id=None
    while student_id is None:
        try:
            student_id=int(input("Enter student ID-"))
            if len(str(student_id))!=8:
                print("Id must be only 8 digits")
                student_id=None
            else:
                if valid_student(student_id) == None:
                    print("Student ID does not exists, please add student")
                    student_id = None
        except:
            print("Invalid input try again")
            student_id=None
    student_details = valid_student(student_id)
    print(student_details)

    # print(str(stu_ID) in open("Details.txt", 'r').read())
    # if str(stu_ID) in open("Details.txt", 'r').read():
    #     return True        
    # else:
    #     return False
# valid_student_marks(12345678)
# add_student_marks()
#Menu()
#pay_fee()
get_marks()