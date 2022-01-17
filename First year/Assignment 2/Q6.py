while True:
    sides = sorted(input("Enter the dimensions to check whether triangle possible or not : ").split())  #Sorting the inputted values in a list
    if len(sides) == 3:                                                                                 #Making sure only 3 values are entered
        break
    else:
        print("\nA triangle has only 3 sides!\nPlease enter only 3 values")
if int(sides[2]) > (int(sides[0]) + int(sides[1])):
    print("No\n")
else:
    print("Yes\n")