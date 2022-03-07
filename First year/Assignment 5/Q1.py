from tkinter import *

def gst(original_cost, net_price):
    return ((net_price - original_cost) * 100 / original_cost)


win = Tk()                                                                                              #Creating a GUI window
win.title("GST Tax Finder Calculator")                                                                  #Setting the title
win.geometry("400x400")
win.minsize(height = "400", width = "400")
win.maxsize(height = "1080", width = "1080")
win.configure(bg="Beige")

heading = Label(win, text = "GST Tax Finder Calculator", borderwidth = 0, background = "Red", font = ("Montserrat ExtraBold",36))
heading.pack(pady = 10,fill = X, ipady = 10)

enter_original_cost = Label(win, text = "Enter the original cost", background = "Black")
enter_original_cost.place(relheight = 20/400, relwidth = 140/400, relx=0.09, rely=0.24)                 #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized

original_cost = IntVar(win, value = 0)
original_cost_entry = Entry(win, justify="right", relief = "sunken", textvariable = original_cost, background = "Black")
original_cost_entry.place(relheight = 20/400, relwidth = 140/400, relx = 0.545, rely=0.24)

enter_net_price = Label(win, text = "Enter the net price", background = "Black")
enter_net_price.place(relheight = 20/400, relwidth = 140/400, relx=0.09, rely=0.36)                     #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized

net_price = IntVar(win, value = 0)
net_price_entry = Entry(win, justify="right", relief = "sunken", textvariable = original_cost, background = "Black")
net_price_entry.place(relheight = 20/400, relwidth = 140/400, relx = 0.545, rely=0.36)







win.mainloop()
