'''a is first number, b is second number and c is the extra variable used for adding and reassigning the values'''
a = 0
b = 1
sum = 0
while True:                                                                                                         #While loop is just for asking the user to input the value again if user enters a -ve value
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break