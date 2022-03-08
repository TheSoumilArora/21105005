from tkinter import *

def gst(original_cost, net_price):
    return ((net_price - original_cost) * 100 / original_cost)


win = Tk()                                                                                              #Creating a GUI window
win.title("GST Tax Finder Calculator")                                                                  #Setting the title
win.geometry("1x1")
win.minsize(height = "400", width = "400")
win.maxsize(height = "1080", width = "1080")
win.configure(bg="Beige")                                                                               #Setting background colour

#Heading
heading = Label(win, text = "GST Tax Finder Calculator", borderwidth = 0, background = "red", font = ("Montserrat ExtraBold",36))
heading.pack(pady = 10,fill = X, ipady = 10)

#Original Cost entry
enter_original_cost = Label(win, text = "Enter the original cost (in ₹)", background = "brown", font = ('lato',13))
enter_original_cost.place(relheight = 20/400, relwidth = 160/400, relx=0.06, rely=0.24)                 #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized


original_cost = IntVar(win, value = 0)
original_cost_entry = Entry(win, font = ('lato',13), justify="right", relief = "sunken", textvariable = original_cost, background = "light blue",fg="black")
original_cost_entry.place(relheight = 20/400, relwidth = 160/400, relx = 0.53, rely=0.24)

#Net Price entry
enter_net_price = Label(win, text = "Enter the net price (in ₹)", font = ('lato',13), background = "brown")
enter_net_price.place(relheight = 20/400, relwidth = 160/400, relx=0.06, rely=0.36)                     #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized

net_price = IntVar(win, value = 0)
net_price_entry = Entry(win, font = ('lato',13), justify="right", relief = "sunken", textvariable = net_price, background = "light blue",fg="black")
net_price_entry.place(relheight = 20/400, relwidth = 160/400, relx = 0.53, rely=0.36)



win.mainloop()
