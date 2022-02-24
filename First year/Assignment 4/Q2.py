from math import comb
n = int(input("Enter the number of rows you want to print: "))                                      #Asking the user the number of rows he/she wants

#RECURSION
print("The Pascal's Triangle using recursion is:")
def pascaltriangle(num):
    if num == 1:                                                                                    #Base case
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                                              #Recursive call
        current_row = [1]                                                                           #The first element of each row, i.e. 1
        previous_row = result[-1]                                                                   #Taking the last row from the data of all rows
        for i in range(len(previous_row)-1):                                                        #Loop for adding the values of top 2 numbers for computing current number's value
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                                                          #The last element of each row, i.e. 1
        result.append(current_row)                                                                  #Adding the computed row to the data of all rows
    return result
for i in pascaltriangle(n):
    print(i)

#ITERATION
print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                  #Outer loop is for the rows
    print((n-i)*" ",end="")                                                                         #This print() adds space before printing each row
    for j in range(n):                                                                              #Inner loop is for the individual elements to be printed
        if comb(i,j) != 0:                                                                          #Condition to ignore the cases when combination = 0 (when j>i)
            print(comb(i,j),end=" ")                                                                #This print() prints each element and adds space after printing each value
    print()                                                                                         #This print() is for changing line for next row