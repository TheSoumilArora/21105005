#Taking input from the user
input = input("\nEnter the numbers whose average is to be calculated: ")

input = input.split()
sum = 0
number_of_terms = 0
for i in input:
    input[input.index(i)] = int(i)        #Converting string input to integer
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