input_string = input("Enter the string : ").lower().split()
if len(input_string) == 1:
    input_string = input_string[0]
occurences = {}
for i in input_string:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
print("The occurence(s) of :")
for i in occurences:
    print('\t"\033[1m%s\033[0m" is/are \033[1m%d\033[0m' % (i,occurences[i]))