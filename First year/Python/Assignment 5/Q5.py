from Q4 import quick_sort                                                                               #Using quick sort because it is faster and more efficient for smaller datasets

lst_in = eval(input("Input array: "))
sorted_list = quick_sort(lst_in)

print("\nSort the inputted array:")                                                                     #Q5(a)
print(sorted_list)

def binary_search(list,element):
    start = 0
    end = len(list) - 1
    mid = 0
    