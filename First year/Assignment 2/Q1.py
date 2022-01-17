input_str = input("Enter the string : ")                                                                #Taking input from user
print("The length of the given string is : %s" % len(input_str))                                        #Printing the length of the string
reversed_str = input_str[ : : -1 ]                                                                      #Creating reversed string
print("The string in reverse would be : %s" % reversed_str)
new_str = input_str[10:26]                                                                              #Creating a new string              
print("The new string becomes : %s" % new_str)
new_str = "object oriented"                                                                             #Replacing the value
substr = "a"
indx = input_str.find(substr)                                                                           #Finding the index value of the given substring
if indx == -1:
    print("The given substring was not found in the inputted string")
else:
    print("The first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))    #Printing the index value
no_white_spaces_str=input_str.replace(" ","")                                                           #Removing white spaces
print("The inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)