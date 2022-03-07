from tkinter import *
from turtle import width

root=Tk()
root.title("Simple Calculator")


#For taking input from the user
e=Entry(root, width=40, borderwidth=5, justify='right')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global maths
    maths ="addition"
    f_num=int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number=e.get()
    global f_num
    global maths
    maths ="subtraction"
    f_num=int(first_number)
    e.delete(0,END)

def button_multiplication():
    first_number=e.get()
    global f_num
    global maths
    maths ="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def button_division():
    first_number=e.get()
    global f_num
    global maths
    maths ="division"
    f_num=int(first_number)
    e.delete(0,END)

def button_equals():
    second_number=e.get()
    e.delete(0,END)
    if(maths=="addition"):
        e.insert(0,f_num + int(second_number))

    if(maths=="subtraction"):
        e.insert(0,f_num - int(second_number))

    if(maths=="multiplication"):
        e.insert(0,f_num * int(second_number))

    if(maths=="division"):
        e.insert(0,f_num / int(second_number))


#GIVING BUTTONS

button_1=Button(root, text="1",padx=40, command=lambda:button_click(1),bg="white" )
button_2=Button(root, text="2",padx=40, command=lambda:button_click(2),bg="white" )
button_3=Button(root, text="3",padx=40, command=lambda:button_click(3),bg="white" )
button_4=Button(root, text="4",padx=40, command=lambda:button_click(4),bg="white" )
button_5=Button(root, text="5",padx=40, command=lambda:button_click(5),bg="white" )
button_6=Button(root, text="6",padx=40, command=lambda:button_click(6),bg="white" )
button_7=Button(root, text="7",padx=40, command=lambda:button_click(7),bg="white" )
button_8=Button(root, text="8",padx=40, command=lambda:button_click(8),bg="white" )
button_9=Button(root, text="9",padx=40, command=lambda:button_click(9),bg="white" )
button_0=Button(root, text="0",padx=40, command=lambda:button_click(0),bg="white")
button_add=Button(root, text="+",padx=39, command=button_add , bg="white")
button_subtract=Button(root, text="-",padx=40, command=button_subtract,bg="white")
button_multiply=Button(root, text="*",padx=40, command=button_multiplication,bg="white")
button_divide=Button(root, text="/",padx=40, command=button_division,bg="white")
button_clearall=Button(root, text="Clear All",padx=21, command=button_clear,bg="white")
button_equals=Button(root, text="=",padx=40, command=button_equals,bg="white")
#PUTTING BUTTONS ON SCREEN
button_1.grid(row=3, column=0, ipadx=50, ipady=50)
button_2.grid(row=3, column=1, ipadx=50, ipady=50)
button_3.grid(row=3, column=2, ipadx=50, ipady=50)

button_4.grid(row=2, column=0, ipadx=50, ipady=50)
button_5.grid(row=2, column=1, ipadx=50, ipady=50 )
button_6.grid(row=2, column=2, ipadx=50, ipady=50 )

button_7.grid(row=1, column=0, ipadx=50, ipady=50 )
button_8.grid(row=1, column=1, ipadx=50, ipady=50 )
button_9.grid(row=1, column=2, ipadx=50, ipady=50 )

button_0.grid(row=4, column=1, ipadx=50, ipady=50)

button_add.grid(row=1, column=4, ipadx=50, ipady=50)
button_subtract.grid(row=2, column=4, ipadx=50, ipady=50)
button_multiply.grid(row=3, column=4, ipadx=50, ipady=50)
button_divide.grid(row=4, column=4, ipadx=50, ipady=50)
button_clearall.grid(row=4, column=0, ipadx=50, ipady=50)
button_equals.grid(row=4, column=2, ipadx=50, ipady=50)
root.mainloop()