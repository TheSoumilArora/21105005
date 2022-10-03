input_str = "Python is a case sensitive language"
print("(a)\tThe length of the given string is : %s" % len(input_str))                                       #Printing the length of the string
reversed_str = input_str[ : : -1 ]                                                                          #Creating reversed string
print("(b)\tThe string in reverse would be : %s" % reversed_str)
new_str = input_str[10:26]                                                                                  #Creating a new string              
print("(c)\tThe new string becomes : %s" % new_str)
dup_input_str = input_str.replace("a case sensitive", "object oriented")                                    #Creating a duplicate input string for replaced value
print("(d)\tThe replaced substring will be : %s" % dup_input_str)
substr = "a"
indx = input_str.find(substr)                                                                               #Finding the index value of the given substring
if indx == -1:
    print("(e)\tThe given substring was not found in the inputted string")
else:
    print("(e)\tThe first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))   #Printing the index value
no_white_spaces_str=input_str.replace(" ","")                                                               #Removing white spaces
print("(f)\tThe inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)