dict1 = {}
while True:                                                                                                         #Loop for inputting values
    name = input("Enter the name of the student : ")
    SID = int(input("Enter the SID of %s : " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    more_data = input("Do you want to enter more data? ")
    if more_data in ("N","n","No","no","NO"):
        break
print("\na. Student Details:")                                                                                      #Q6(a)
for i in dict1:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         #Sorting the dictionary using student names
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       #Q6(b)
for i in dict2:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    #Sorting the dictionary using SIDs
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        #Q6(c)
for i in dict3:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict3[i],i))
