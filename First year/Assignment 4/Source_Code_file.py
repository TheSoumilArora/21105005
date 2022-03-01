#Question 1
print("The solution of Question 1 is:\n")




#Question 2
print("\nThe solution of Question 2 is:\n")

from math import comb
while True:                                                                                             #Loop for preventing -ve input of no. of rows (because they can't be -ve)
    n = int(input("Enter the number of rows you want to print: "))                                      #Asking the user the number of rows he/she wants
    if n >= 0:
        break
    else:
        print("Number of rows must be positive, please enter the value again!")

#RECURSION
print("The Pascal's Triangle using recursion is:")
def pascaltriangle(num):
    if num == 0:
        return [[0]]
    elif num == 1:                                                                                      #Base case
        return [[1]]
    else:
        result = pascaltriangle(num-1)                                                                  #Recursive call
        current_row = [1]                                                                               #The first element of each row, i.e. 1
        previous_row = result[-1]                                                                       #Taking the last row from the data of all rows
        for i in range(len(previous_row)-1):                                                            #Loop for adding the values of top 2 numbers for computing current number's value
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]                                                                              #The last element of each row, i.e. 1
        result.append(current_row)                                                                      #Adding the computed row to the data of all rows
    return result
for i in pascaltriangle(n):
    print((n-len(i))*" ",end="")                                                                        #This print() adds space before printing each row
    for j in i:
        if j != 0:
            print(j, end =" ")
    print()

#ITERATION
print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                      #Outer loop is for the rows
    print((n-i-1)*" ",end="")                                                                           #This print() adds space before printing each row
    for j in range(n):                                                                                  #Inner loop is for the individual elements to be printed
        if comb(i,j) != 0:                                                                              #Condition to ignore the cases when combination = 0 (when j>i)
            print(comb(i,j),end=" ")                                                                    #This print() prints each element and adds space after printing each value
    print()                                                                                             #This print() is for changing line for next row



#Question 3
print("\nThe solution of Question 3 is:\n")

val1 = int(input("Enter first integer value(dividend): "))
while True:                                                                                             #Loop to make sure val2 != 0(i.e. denominator must not be 0)
    val2 = int(input("Enter second integer value(divisor): "))
    if val2 != 0:
        break
    else:
        print("\nDivisor must not be 0\nPlease enter the divisor again")
result = divmod(val1,val2)
print("\nQuotient:",result[0],"\nRemainder:",result[1])

print("\na. Check whether the function (divmod()) is callable or not:")                                 #Q3(a)
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(", which means it is callable")
else:
    print(", which means it is not callable")

print("\nb. Check whether all the values are zero or not:")                                             #Q3(b)
if all(x != 0 for x in result):
    print("All values in result(i.e. quotient and remainder) are non-zero.")
else:
    print("All values in result(i.e. quotient and remainder) are not non-zero(i.e. one of them is 0).")

print("\nc. Add (4,5,6) to the result and filter out values greater than 4:")                           #Q3(c)
c_part = result + (4,5,6)
c_part_output = sorted(list((x for x in c_part if x>4)))
print("Values greater than 4(in list format) are:", c_part_output)

print("\nd. Convert the above result into a set datatype:")                                             #Q3(d)
d_part = set(c_part_output)
print("The output of previous part in set datatype would be:", d_part)

print("\ne. Make the set immutable:")                                                                   #Q3(e)
e_part = frozenset(d_part)
print("The immutable set would be:", e_part)

print("\nf. Evaluate the maximum value from the set and find out its hash value:")                      #Q3(f)
f_part = max(e_part)
print("The maximum value from the set is:", f_part)
print("The hash value of %d(considering it to be integer) is %d and its hash value is %d(if we consider %s as a string)." % (f_part,hash(f_part),hash(str(f_part)),str(f_part)))



#Question 4
print("\nThe solution of Question 4 is:\n")




#Question 5
print("\nThe solution of Question 5 is:\n")





#Question 6
print("\nThe solution of Question 6 is:\n")