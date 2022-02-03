dict1 = {}
while True:
    name = input("Enter the name of the student : ")
    SID = int(input("Enter the SID of %s : " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    more_data = input("Do you want to enter more data? ")
    if more_data in ("N","n","No","no","NO"):
        break
print("\na. ",end="")
for i in dict1:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict1[i],i), end = "\n   ")
print(dict1)