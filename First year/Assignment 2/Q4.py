entered_numbers=input("Enter the numbers : ").split()
i=0
while i < len(entered_numbers):                                                                         #Converting all numbers into int format
    entered_numbers[i]=int(entered_numbers[i])
    i += 1
print("The greatest number among the entered numbers is %s\n" % max(entered_numbers))