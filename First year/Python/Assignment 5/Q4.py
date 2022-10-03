lst_in = eval(input("Enter the list: "))

#Using quick sort algorithm
def quick_sort(list):
    if len(list) <= 1:                                                                                  #Base case
        return list
    else:
        left_arr = [x for x in list if x < list[0]]
        pivot = [x for x in list if x == list[0]]
        right_arr = [x for x in list if x > list[0]]
        return quick_sort(left_arr) + pivot + quick_sort(right_arr)                                     #Recursive call by taking pivot as the first element of the unsorted list
def merge_sort(list):
    pass

lst_out = quick_sort(lst_in)
print("The sorted list(using quick sort algorithm) is: ", lst_out)
lst_out2 = merge_sort(lst_in)
print("The sorted list(using merge sort algorithm) is: ", lst_out)