def triangle_row(spaces, num_list):
    n_list = []
    n_list.append(1)
    if len(num_list) >= 2:
        for i in range(len(num_list) - 1):
            n_list.append(num_list[i] + num_list[i + 1])
    if len(num_list) >= 1:
        n_list.append(1)

    print("{:>4}".format(" ") * spaces, end='')
    for num in n_list:
        print("{:^7}".format(num), end=" ")
    spaces -= 1
    print()
    if spaces >= 0:
        triangle_row(spaces, n_list)


rows = int(input("Enter number of rows: "))
num_list = []
triangle_row(rows - 1, num_list)