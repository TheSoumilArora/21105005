string = input("Enter string: ")
string_out = ""
for i in string:
    value = ord(i)
    chr(value+28)
    string_out = string_out + chr(value-28)
print(string_out)