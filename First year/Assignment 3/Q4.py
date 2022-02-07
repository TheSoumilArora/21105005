'''given_table is a list of lists'''
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         #loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                               #i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))