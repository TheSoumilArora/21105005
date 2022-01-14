#Question 1
import numbers


print("\nThe solution of Question 1 is :\n")
#Taking input from the user
numbers = input("Enter the numbers whose average is to be calculated: ")

numbers = numbers.split()
sum = 0
number_of_terms = 0
for i in numbers:
    numbers[numbers.index(i)] = int(i)        #Converting string input to integer
    number_of_terms += 1                  #Counting the number of terms
    sum += int(i)
average = sum/number_of_terms             #Calculating the average

#Making the output presentable
if average == int(average):
    average = int(average)
else:
    average = round(average, 2)

#Printing the average
print("\nThe average of the given", number_of_terms, "numbers is", average ,"\n")

#Question 2
print("\nThe solution of Question 2 is :\n")
#Given constants
rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000

#Taking input from the user
gross_income = float(input("Enter your gross income : "))
number_of_dependents = int(input("Enter number of dependents : "))

#Calculation tax
taxable_income = round(gross_income-standard_deduction-(dependent_deduction*number_of_dependents), 1)
tax = taxable_income*rate
if tax <0 :
    tax = 0

#Output
print("\nYour tax is $",tax,"\n")

#Question 3
print("\nThe solution of Question 3 is :\n")
#Taking input from the user
SID = int(input("Enter the SID of the student\n"))
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
print("\n",Student, "\n")

#Question 4
print("\nThe solution of Question 4 is :\n")
import pandas as pd
names = []
marks = []
count = 1

#Taking the input from the user
number_of_students = int(input("You want to fill data for how many students? "))
while count <= number_of_students:
    while count == 1:
        print("\nThe name and marks are to be inputted separated by a \" - \". For example : \" Soumil Arora - 99 \"\n")
        break
    input_value = input("Enter name and marks of Student " + str(count) + " : ")
    input_value = input_value.split("-", 1)
    names.insert(count-1, input_value[0].strip())
    marks.insert(count-1, int(input_value[1]))
    count += 1

#Creation of series
data = pd.Series(marks, index=names)

#Sorting the data
while True:
    asc_or_dsc = int(input("\nEnter 1 for ascending, 2 for descending : "))
    if asc_or_dsc == 1:
        data=data.sort_values()
        break
    elif asc_or_dsc == 2:
        data=data.sort_values(ascending=False)
        break
    else:
        print("Please enter the correct input")

#Output
print("\nThe marks of students in required format are as follows :\n")
count=1
while count <= number_of_students:
    print("Marks of",data.index[count-1],"are",data[count-1],"\n")
    count += 1

#Question 5(a)
print("\nThe solution of Question 5(a) is :\n")
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print(color,"\n")

#Question 5(b)
print("\nThe solution of Question 5(b) is :\n")
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print(color,"\n")