def hanoitower(n,present,future,midway,count=0):
    if n==2:
        print(f"Shift disc 1 from {present} to {midway}")
        print(f"Shift disc 2 from {present} to {future}")
        print(f"Shift disc 1 from {midway} to {future}")
        count+=3
        return count
        
    else:
        count+=hanoitower(n-1,present,midway,future)
        print(f"Shift disc {n} from {present} to {future}")
        count+=1
        count+=hanoitower(n-1,midway,future,present)
        return count

number_of_discs = int(input("Number of discs : "))
count = hanoitower(number_of_discs,'A','C','B')
print(f"\nMinimum number of shifts required to move the arrangement of {number_of_discs} from 'A' to 'C'  is  {count}")