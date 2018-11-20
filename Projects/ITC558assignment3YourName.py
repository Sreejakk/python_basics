def menu():
 
    student_file = 'students.txt' 
    try:
        stu_file = open(student_file, 'r')              #reads students.txt file
    except IOError:
        stu_file = open(student_file, 'w')              #creates students.txt file if not exists

    assessment_file = 'assessments.txt'

    try:
        marks_file = open(assessment_file, 'r')              #reads assessments.txt file
    except IOError:
        marks_file = open(assessment_file, 'w')              #creates assessments.txt file if not exists

    option = None                   #sets option none

    print("\n------------------------------------\nWelcome to the Student and Assessment Management System \n")
    print("select operation from below options...")
    print(" <A>add details of a student. \n <I>insert assignment marks of a student. \n <S>search assessment marks for a student. \n <Q>quit.\n------------------------------------\n")

    while option is None:
        option = input("Enter Option : ")                #gets option from user
        option = option.lower()                 #converts option to lower

        if option == "a":
            add_student()                        #calls add_student fuction for adding student

        elif option == "i":
            insert_marks()                      #calls insert_marks fuction for adding student marks

        elif option == "s":
            search_student()                    #call search_student fuction for searching student

        elif option == "q":
            quit()                              #exists the program
        else:
            print("Invalid Option! Try again")
            option = None

def add_student():

    student_id = 0
    while student_id is 0:              #loops until student_id is not 0
        student_id = input("Please Enter Student ID: ")
        try:
            student_id = int(student_id)
            if student_id > 0:
                if len(str(student_id)) > 8 or len(str(student_id)) < 8:        #checks student_id length
                    print("Student Id lenght should be 8 digits...")
                    student_id = 0
            else:
                print("Invalid Input,try again..! (ex:11111111)")
                student_id = 0

            if str(student_id) in open("students.txt", 'rt').read():           #checks student_id exists in students.txt file
                print("Student Id already exist")
                student_id = 0

        except:
            print("Invalid Input,try again..! (ex:12345678)")
            student_id = 0


    valid_name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

    student_name = None
    while student_name is None:
        student_name = input("Please Enter Student Name: ")

        if all(let in valid_name for let in student_name):          #checks name is valid or not
            break
        else:
            print("Invalid input...! (ex: Tony Stark)")
            student_name = None

    valid_course = 'IMT0123456789'
    course = None

    while course is None:

        course = input("Please Course Code: ")
        course = course.upper()

        if all(let in valid_course for let in course):          #checks couse is valid or not
                if len(course) > 5 or len(course) < 5:
                    print("Course lenght should be 5 letters")
                    course = None
                else:
                    if course[0:3] == "MIT" and course[4:5].isdigit():  #checks first 3 letter and last 3 letters
                        break
                    else:
                        print(
                            "Couse code should start with MIT and end with numbers (ex: MIT01)")
                        course = None
        else:
            print("Invalid Couse Code...! (ex: MIT01)")
            course = None

    with open("students.txt", "a+") as students:        #writes student data to students.txt file 
        students.write("{} {} {}\n".format(
            student_id, student_name, course))

    print("Thank You")
    print("The details of the student you entered are as follows:\n------------------------------------")

    students_data = get_students()      #gets students data

    new_student = (students_data[-1]).split()       #gets last recordfrom students.txt file

    print("Student Id: {}".format(new_student[0]))
    print("Student name: {}".format(' '.join(new_student[1:-1])))
    print("Course : {}".format(new_student[-1]))
    print("------------------------------------")

    another_student = None
    while another_student is None:
        another_student = input("Do you want to enter details for another student (Y/N)?")      #gets user input for another student
        another_student = another_student.lower()
        if another_student == "y":
            add_student()           #calls add_student function
        elif another_student == "n":
            menu()              #class menu  function
        else:
            print("Invalid input,Please try again!")
            another_student = None

#inserts marks 
def insert_marks():

    student_id = 0

    while student_id is 0:
        student_id = input("Please Enter Student ID: ")
        try:
            student_id = int(student_id)
            if len(str(student_id)) > 8 or len(str(student_id)) < 8:        #checks for valid length
                print("Student Id lenght should be 8 digits...")
                student_id = 0
        except:
            print("Invalid Input,try again..! (ex:12345678)")
            student_id = 0

    #checks valid student or not
    if valid_student(student_id):
        student_id = student_id
    else:
        print("\n*** Student Id does not exist,insert valid id *** \n")
        insert_marks()

    valid_subjectCode = 'CIT0123456789'
    subject_code = None

    while subject_code is None:
        subject_code = input("Please Subject Code: ")
        subject_code = subject_code.upper()

        if all(let in valid_subjectCode for let in subject_code):
            if len(subject_code) > 6 or len(subject_code) < 6:      #checks for subject_code length
                print("Subject Code lenght should be 6 letter")
                subject_code = None
            else:
                #checks first 3 and last 3 letters
                if subject_code[:3] == "ITC" and subject_code[-3:].isdigit() and int(subject_code[-3:]) > 0:
                    break
                else:
                    print(
                        "Subject code should start with ITC and end with numbers (ex: ITC001)")
                    subject_code = None
        else:
            print("Invalid Subject Code...! (ex: ITC001)")
            subject_code = None

    assessment_number = 0

    assessment_data = get_assessment()          #gets assessments from assessments.txt file

    while assessment_number is 0:
        assessment_number = input("Please enter the assessment number: ")
        try:
            assessment_number = int(assessment_number)
            #checks assessment_number valid or not
            if assessment_number == 1 or assessment_number == 2 or assessment_number == 3:
                for assessment in assessment_data:
                    assessment = (assessment).split()
                    #checks valid assessments already or not
                    if assessment[0] == str(student_id) and assessment[1] == subject_code and assessment[2] == str(assessment_number):
                        print(
                            "The student Assessment marks already exist.Try again!")
                        assessment_number =0
            else:
                print("Invalid Assessment Number ex(1,2,3)")
                assessment_number = 0
        except:
            print("Invalid Assessment Number ex(1,2,3)")
            assessment_number = 0

    marks = None
    while marks is None:
        marks = input("Please enter assessment marks:") #gets marks from user
        try:
            marks = int(marks)
            if marks > 100 or marks < 0:        #cheks marks between 0 to 100
                print("Marks should between 0 to 100,Try Again!")
                marks = None
        except:
            print("Invaild marks,Try Again!")
            marks = None

    #inserts marks to assessments.txt file
    with open("assessments.txt", "a+") as assessments:
        assessments.write("{} {} {} {}\n".format(
            student_id, subject_code, assessment_number, marks))

    print("Thank You")
    print("------------------------------------\nThe details of the student you entered are as follows:\n")

    new_assessment = (get_assessment()[-1]).split()         #gets last record from assements.txt file

    #prints students marks
    print("Student Id: {}".format(new_assessment[0]))
    print("Subject Code: {}".format(new_assessment[1]))
    print("Assessment Number: {}".format(new_assessment[2]))
    print("Marks: {}".format(new_assessment[3]))
    print("------------------------------------")

    option = None
    while option is None:
        temp_data = input(
            "Do you want to insert another student marks(Y/N)?")        #gets user input
        option = temp_data.lower()
        if option == "y":
            insert_marks()      #calls insert marks function
        elif option == "n":
            menu()          #calls menu function
        else:
            print("Invalid input,Please try again!")
            option = None

#search student
def search_student():

    student_id = 0

    while student_id is 0:          #loops until student_id is not 0
        student_id = input("Please Enter Student ID: ")
        try:
            student_id = int(student_id)        #converts student_id to int
            if len(str(student_id)) > 8 or len(str(student_id)) < 8:        #checks for student_id length
                print("Student Id lenght should be 8 digits...")
                student_id = 0

            if valid_student(student_id) == False:          #checks student_id exists or not 
                print("\n*** Student Id does not exist,insert valid id *** \n")
                student_id = 0

        except:
            print("Invalid Input,try again..! (ex:12345678)")
            student_id = 0

    assessment_marks = get_assessment()     #gets assements 
    students = get_students()       #gets students
    for student in students:
        student = (student).split()
        if student[0] == str(student_id):       #orints marks if student_id matches
            print("\n+++ Student Found +++\n")
            print("Student Id: {}".format(student[0]))
            print("Student name: {}".format(' '.join(student[1:-1])))
            print("Course : {}".format(student[-1]))
            print("---------------")

    print("\nSubject Code   Assessment Number   Marks\n-----------------------------------------")

    for marks in assessment_marks:          #loops through marks 
        marks = (marks).split()
        if marks[0] == str(student_id):
            print(marks[1]+"            "+marks[2] +
                    "                  "+marks[3])          #prints marks

    print("\n")

    new_search = None
    while new_search is None: #loop until new_search not None
        temp_data = input(
            "Do you want to search another student marks(Y/N)?")        #user input for search another student or not
        new_search = temp_data.lower()      #convert input data to lower case

        if new_search == "y":
            search_student()        #calls search_students function
        elif new_search == "n":
            menu()      #calls menu
        else:
            print("Invalid input,Please try again!")
            new_search = None

#quits the programs
def quit():
    exit()

#gets assessment from assessments.txt file
def get_assessment():
    assessment_data = []

    with open('assessments.txt') as assessments:
        for assessment in assessments:              #loops through assessments
            assessment_data.append(assessment)      #appends current marks 
    return assessment_data      #returns available student marks

#gets available students in students.txt file
def get_students():
    students_data = []
    with open('students.txt') as students:      #reads file as students
        for student in students:
            students_data.append(student)       #appedns stduent current student data

    return students_data        #returns available students

def valid_student(student_id):
    #checks student id exists in students.txt file
    if str(student_id) in open("students.txt", 'rt').read():
        return True         #returns True
    else:
        return False # returns False
menu()