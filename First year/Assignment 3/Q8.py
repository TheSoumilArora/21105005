set1 = (1,2,3,4,5)
set2 = (2,4,6,8)
set3 = (1,5,9,13,17)
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")

set4 = list(set1 + set2)
for i in set4:
    if i in set1 and i in set2:
        set4.remove(i)
print(set4)

print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")

pass

print("c. Set of elements that are exactly two of the sets Set1, Set2 and Set3:",end=" ")

pass

print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")

pass

print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")

pass