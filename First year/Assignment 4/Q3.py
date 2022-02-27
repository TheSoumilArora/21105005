val1 = int(input("Enter first integer value(dividend): "))
while True:                                                                                             #Loop to make sure val2 != 0(i.e. denominator must not be 0)
    val2 = int(input("Enter second integer value(divisor): "))
    if val2 != 0:
        break
    else:
        print("\nDivisor must not be 0\nPlease enter the divisor again")
result = divmod(val1,val2)
print("\nQuotient:",result[0],"\nRemainder:",result[1])

print("\na. Check whether the function (divmod()) is callable or not:")
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(", which means it is callable")
else:
    print(", which means it is not callable")

print("\nb. Check whether all the values are zero or not:")
no_of_zero = 0
for i in result:
    if i == 0:
        no_of_zero += 1
if no_of_zero == 0:
    print("All values in result(i.e. quotient and remainder) are non-zero")
else:
    print("All values in result(i.e. quotient and remainder) are not non-zero(i.e. one of them is 0)")

print("\nc. Add (4,5,6) to the result and filter out values greater than 4:")
c_part = result + (4,5,6)
c_part_output = sorted(list((x for x in c_part if x>4)))
print("Values greater than 4 are: ", end="")
for i in c_part_output:
    print(i, end=" ")

print("\nd. Convert the above result into a set datatype:")
d_part = set(c_part_output)
print("The output of previous part in set datatype would be:", d_part)

print("\ne. Make the set immutable:")
