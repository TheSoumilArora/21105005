first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter third number : "))
if first_number >= second_number:
    if first_number >= third_number:
        print("The greatest number is %s\n" % first_number)
    else:
        print("The greatest number is %s\n" % third_number)
else:
    if second_number >= third_number:
        print("The greatest number is %s\n" % second_number)
    else:
        print("The greatest number is %s\n" % third_number)