row=int(input("Enter number of rows:"))
if row<=16:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^90}".format(p=1)
            print(f)
            f = "{p:^90}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^90}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
elif row>16 and row<=20:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^120}".format(p=1)
            print(f)
            f = "{p:^120}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^120}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)
elif row>20 and row<=30:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^240}".format(p=1)
            print(f)
            f = "{p:^240}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^240}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)

else:
    def psum(list1, row):
        i1 = 0
        i2 = 1
        l = []
        for i1 in range(row - 1):
            l.append(list1[i1] + list1[i2])
            i1 = i1 + 1
            i2 = i2 + 1
        l.insert(0, 1)
        l.append(1)
        return (l)


    def ptriangle(rows):
        if rows == 1:
            print(1)
        elif rows == 2:
            print(f" 1\n1 1")
        else:
            f = "{p:^700}".format(p=1)
            print(f)
            f = "{p:^700}".format(p="1  1")
            print(f)
            l1 = [1, 1]
            row = 2
            for i in range(rows - 2):
                v = psum(l1, row)
                v2 = v.copy()
                v2 = list(map(str, v2))
                n = rows
                k = "  ".join(v2)
                f = "{p:^700}".format(p=k)
                print(f)
                row = row + 1
                l1 = v
    ptriangle(row)