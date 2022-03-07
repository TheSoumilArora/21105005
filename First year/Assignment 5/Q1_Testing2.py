# *********** Ans -1 ************

from tkinter import *
from tkinter import messagebox
win=Tk()
Label_1=Label(win,text='GST Tax Finder Calculator',bg='red',font=('Algerian',20))
Label_1.pack()
Label_2=Label(win,text='Enter Orignal Cost(+ Rational no.) : ',font=('Arial black',10))
Label_2.place(x=15,y=60)
Entry_1=Entry(win,width='20')
Entry_1.place(x=270,y=60)
Label_3=Label(win,text='Enter Net Price(+ Rational no.) : ',font=('Arial black',10))
Label_3.place(x=35,y=100)
Entry_2=Entry(win,width='20')
Entry_2.place(x=270,y=100)
Label_4=Label(win,text='GST (in %) : ',font=('Arial black',10))
Label_4.place(x=175,y=140)
def myclick():
    global Answer
    if(Entry_1.get()=='' or Entry_2.get()=='' or float(Entry_1.get())<0 or float(Entry_2.get())<0):
        messagebox.showwarning("Invalid input", "Enter all valid inputs (Can't zero or negative)")
        return
    Net_price=float(Entry_2.get())
    Orignal_cost=float(Entry_1.get())
    if(Orignal_cost==0):
        messagebox.showwarning("Invalid Original Cost", "Can't Zero or negative")
        return
    GST=(Net_price-Orignal_cost)*100/Orignal_cost
    if(GST<0):
        messagebox.showinfo("Invalid GST", "GST can't be in negative")
        return
    Answer=Label(win,text=str(GST))
    Answer.place(x=270,y=140)
    Answer_but['state']=DISABLED
    New_but['state']=NORMAL
def newinput():
    Answer_but['state']=NORMAL
    New_but['state']=DISABLED
    Answer.destroy()
Answer_but=Button(win,text='Calculate GST',font=('Arial black',10),bg='blue',command=myclick,activebackground='yellow',activeforeground='red')
Answer_but.place(x=220,y=180)
New_but=Button(win,text='New Input',font=('Arial black',10),bg='red',command=newinput,activebackground='yellow',activeforeground='red')
New_but.place(x=120,y=180)
New_but['state']=DISABLED
win.mainloop()

# *********** Ans -2 ************

from tkinter  import *
import calendar
from tkinter import messagebox
my_w = Tk()
my_w.maxsize(width=680,height=800)  
my_w.minsize(width=680,height=800)
lbl_0=Label(my_w,text='CALENDAR',font=('algerian 20 underline'),fg='red')
lbl_0.pack()
lbl_1=Label(my_w,text='ENTER YEAR (INTEGER) : ',font=('algerian 11'))
lbl_1.place(x=170,y=40)
Ent_1=Entry(my_w,width=13)
Ent_1.place(x=350,y=40)
def myclick():
    if(Ent_1.get()==''):
        messagebox.showerror('INVALID INPUT','Enter year in input')
        return
    n=int(Ent_1.get())
    if(n<=0) :
        messagebox.showerror('INVALID INPUT','Enter year can not be negative or zero')
        return
    calu=calendar.calendar(n)
    lbl_2=Label(my_w,text=calu,font=('algerian 13 bold'))
    lbl_2.place(x=20,y=70)
But_1=Button(my_w,text='Show Calendar',font='Agerian 10 bold',bg='blue',width=15,command=myclick)
But_1.place(x=450,y=40)
my_w.mainloop()


# *********** Ans -3 ************

from tkinter import *
expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))

		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="grey")
	gui.title("Simple Calculator")
	gui.maxsize(width=265,height=150)
	gui.minsize(width=265,height=150)
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg='white', bg='black',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='white', bg='black',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='white', bg='black',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='white', bg='black',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='white', bg='black',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='white', bg='black',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='white', bg='black',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='white', bg='black',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='white', bg='black',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='white', bg='black',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='white', bg='black',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='white', bg='black',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='white', bg='black',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='white', bg='black',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='white', bg='black',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='white', bg='black',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='white', bg='black',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	gui.mainloop()


# *********** Ans -4 ************

#  BY USING MERGE SORT 

def mergesort(l):
    if(len(l)==1):
        return l
    mid=len(l)//2
    left=mergesort(l[:mid])
    right=mergesort(l[mid:])
    i=0
    j=0
    sorted_list=[]
    while i < len(left) and j < len(right):
        if(left[i]<right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:]) 
    return sorted_list

l=[1,5,7,3,2,72,33,4,53,5234,234,1,124]
print(f'Unsorted List : {l}')
sorted_list=mergesort(l)
print(f'Sorted List : {sorted_list}')


# *********** Ans -5 ************

inputed_list=[]
n=int(input('Enter the list size (integer) : '))
i=1
while(i<=n):
    temp=int(input(f'Enter(integer) element-{i} : '))
    inputed_list.append(temp)
    i+=1

# part a
sorted_list=sorted(inputed_list)
print(f'Sorted array : {sorted_list}')

# part b
m=int(input('Enter the number to find occurences of that number (integer) : '))
start=0
end=n-1
founded=False
while(start<=end):
    mid=((end+start)//2)
    if(sorted_list[mid]==m):
        founded=True
        break
    elif(sorted_list[mid]<m):
        start=mid+1
    else:
        end=mid-1

# part c
if(founded):
    # mid is the index of element as array is sorted
    # same element is present in its (right or left(togther)) otherwise nowhere
    p=mid-1 # p is index checking leftward
    q=mid+1 # q is index checking rightward
    count=1 # count intially one because mid is also present
    while(q<n and sorted_list[q]==m):
        count+=1
        q+=1
    while(p>=0 and sorted_list[p]==m):
        count+=1
        p-=1
    print(f'Number of occurrences of element {m} is {count}')
else:
    print(f'Error - {m} NOT FOUNDED')
