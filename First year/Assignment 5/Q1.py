#Importing required modules
from tkinter import *


#Defining all the required functions
def add(x,y):
    return (x+y)

def subtract(x,y):
    return (x-y)

def multiply(x,y):
    return (x*y)

def divide(x,y):
    return (x/y)

def gst(original_cost, net_price):
    return ((net_price - original_cost) * 100 / original_cost)

win = Tk()                                                                                              #Creating a GUI window
win.title("GST Tax Finder Calculator")                                                                  #Setting the title
win.geometry("300x300")
win.minsize(height = "300", width = "300")
win.maxsize(height = "1080", width = "1080")
win.configure(bg="Beige")


win.mainloop()
