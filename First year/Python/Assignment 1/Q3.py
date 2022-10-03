#Taking input from the user
SID = int(input("\nEnter the SID of the student\n"))
name = input("\nEnter the name of the student\n")
while True:
    gender = input("\nEnter the gender of the student\n(Enter F for female, M for male and U for unknown)\n")
    gender=gender.upper()
    if gender in ("M","F","U"):
        break
    else:
        print("\nPlease enter the gender in correct format")
while True:
    course_name = input("\nEnter the course name of the student\n(out of EE, ECE, CSE, Aero, Prod, Civil, Mech, Metta)\n")
    course_name = course_name.upper()
    if course_name in ("EE","ECE","CSE","AERO","PROD","CIVIL","MECH","METTA"):
        break
    else:
        print("\nPlease enter the course name in correct format")
while True:
    cgpa = round(float(input("\nEnter the CGPA of the student\n")),1)
    if cgpa >= 0 and cgpa <= 10:
        break
    else:
        print("\nThe CGPA should be less than 10\n")

#Creating the list
Student = [SID, name, gender, course_name, cgpa]

#Printing the required list
print(Student, "\n")