from tkinter import *

def gst_formula(original_cost, net_price):
    return ((net_price - original_cost) * 100 / original_cost)


win = Tk()                                                                                              #Creating a GUI window
win.title("GST Tax Finder Calculator")                                                                  #Setting the title
win.geometry("1x1")
win.minsize(height = "400", width = "400")
win.maxsize(height = "1080", width = "1080")
win.configure(bg="Beige")                                                                               #Setting background colour

#Heading
heading = Label(win, text = "GST Tax Finder Calculator", borderwidth = 0, background = "red", font = ("Montserrat ExtraBold",35))
heading.pack(pady = 10,fill = X, ipady = 10)

#Original Cost entry
enter_original_cost = Label(win, text = "Enter the original cost (in ₹)", background = "brown", font = ('lato',13))
enter_original_cost.place(relheight = 20/400, relwidth = 160/400, relx=0.06, rely=0.24)                 #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized


original_cost = DoubleVar(win, value = 0)
original_cost_entry = Entry(win, font = ('lato',13), justify="right", relief = "sunken", textvariable = original_cost, background = "light blue",fg="black")
original_cost_entry.place(relheight = 20/400, relwidth = 160/400, relx = 0.53, rely=0.24)

#Net Price entry
enter_net_price = Label(win, text = "Enter the net price (in ₹)", font = ('lato',13), background = "brown")
enter_net_price.place(relheight = 20/400, relwidth = 160/400, relx=0.06, rely=0.36)                     #These values are experimental (hit-and-trial) to maintain the aspect ratio of the box when the window is resized

net_price = DoubleVar(win, value = 0)
net_price_entry = Entry(win, font = ('lato',13), justify="right", relief = "sunken", textvariable = net_price, background = "light blue",fg="black")
net_price_entry.place(relheight = 20/400, relwidth = 160/400, relx = 0.53, rely=0.36)

#Calculate GST
def calculate_gst():
    global output
    value_gst = "%0.2f" % (gst_formula(original_cost.get(), net_price.get()))
    output = Label(win, text = value_gst+'%', font = ('lato',13))
    output.pack()
    clear_everything.configure(state = NORMAL)

gst_calculate = Button(win, text = "Calculate GST", font = ('lato',13), highlightbackground= "Beige", command = calculate_gst)
gst_calculate.place(relwidth = 100/400, relheight = 27/400, relx = 0.53, rely = 0.60)

#Clear all
def clear_all():
    original_cost_entry.delete(0,END)
    net_price_entry.delete(0,END)
    output.destroy()
    clear_everything.configure(state = DISABLED)

clear_everything = Button(win, text = "Clear", font = ('lato',13), highlightbackground= "Beige", state = DISABLED, command = clear_all)
clear_everything.place(relwidth = 64/400, relheight = 27/400, relx = 0.3, rely = 0.60)


win.mainloop()