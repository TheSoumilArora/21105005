import pandas as pd
names = []
marks = []
count = 1

#Taking the input from the user
number_of_students = int(input("\nYou want to fill data for how many students? "))
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