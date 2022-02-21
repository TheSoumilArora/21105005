from math import comb
n = int(input("Enter the number of rows you want to print: "))                                      #Asking the user the number of rows he/she wants

#RECURSION
print("The Pascal's Triangle using recursion is:")
def pascaltriangle(num):
    lst_out = []
    if num == 0:
        print("topmost point = 1")
    else:
        for i in range(num+1):
            print(comb(num,i), end = " ")
        print()
        pascaltriangle(num-1)
pascaltriangle(n)


#ITERATION
print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                  #Outer loop is for the rows
    print((n-i)*" ",end="")                                                                         #This print() adds space before printing each row
    for j in range(n):                                                                              #Inner loop is for the individual elements to be printed
        if comb(i,j) != 0:                                                                          #Condition to ignore the cases when combination = 0 (when j>i)
            print(comb(i,j),end=" ")                                                                #This print() prints each element and adds space after printing each value
    print()                                                                                         #This print() is for changing line for next row
