list_in = eval(input("Enter the list : "))
list_out = []
for i in list_in:
    list_out.append((i, i**2))
print("Output :", list_out)