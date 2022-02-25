class Student:                                                                                          #Creating class Student
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print("Object Created\n")
    def __del__(self):
        print("Object destroyed")
name = input("Enter name of student: ").strip()                                                         #Inputting name and roll number from the user
roll_no = int(input("Enter SID of %s: " % (name)))
student1 = Student(name,roll_no)                                                                        #Creating object
print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))     #Printing the assigned values
del student1                                                                                            #Deleting the object