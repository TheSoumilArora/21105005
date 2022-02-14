list_in = eval(input("Enter the list of integers: "))
list_out = []
for i in list_in:
    list_out.append((i, i**2))                                                                                      #(i, i**2) is the tuple which is added in the list, i.e. list_out is list of tuples
print("Output:", list_out)