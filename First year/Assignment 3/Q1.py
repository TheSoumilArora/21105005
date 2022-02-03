input_value = input("Enter the string: ").lower().split()
if len(input_value) == 1:
    input_value = input_value[0]
occurences = {}
for i in input_value:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
print("The occurence(s) of:")
for i in occurences:
    print('\t"\033[1m%s\033[0m" is/are \033[1m%d\033[0m' % (i,occurences[i]))