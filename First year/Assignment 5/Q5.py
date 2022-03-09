# Importing tkinter library.
from tkinter import *
from tkinter import messagebox
import calendar

# Defining main window.
main = Tk()

# Fixing size of main window.
main.minsize(width = 1000, height = 600)
main.maxsize(width = 1000, height = 600)

# Giving title to the main window.
main.title("Assigment 5 by Ayush Kansal(21105049)")
main.config(background = "pink")



# Question 1.
def ques_1():
    # Defining ques 1 window.
    ques_1 = Toplevel(main)

    # Fixing size of the window.
    ques_1.minsize(width = 1000, height = 600)
    ques_1.maxsize(width = 1000, height = 600)

    # Giving title to window.
    ques_1.title("GST rate calculator.")
    ques_1.config(background ="darkgreen")


    # Making head label. 
    head_label = Label(ques_1, text = "GST calculator.", fg = "black",bg = "#fdd017", font = ("allura",50,"bold"), relief = "sunke", bd = 5)
    head_label.pack(pady = 30)

    # funtion for first question.
    def gst_calculator():

        # Taking out values entered by user. 
        original_cost = float(original_cost_enter.get())
        net_prize = float(net_prize_enter.get())

        # calculating gst
        gst = ((net_prize - original_cost) * 100) / original_cost

        # Printing appropiate result.
        if original_cost < 0 or net_prize < 0:
            gst = "Original cost and net prize can't be a negative value."
            mess_box = messagebox.showwarning("GST tax finder.", f"{gst}", parent = ques_1)
        elif original_cost > net_prize:
            gst = "Net prize must be greater than or equal to original cost."
            mess_box = messagebox.showwarning("GST tax finder.", f"{gst}", parent = ques_1)
        else:
            mess_box = messagebox.showinfo("GST tax finder.", f"Gst rate: {gst}", parent = ques_1)



    # Making labels for original cost and net prize.
    original_cost_label = Label(ques_1, text = "Original cost", bg = "#fdd017", fg = "black", font = ('calibre',20,"italic"), relief = 'raised', width = 11, padx = 10, bd = 5)
    original_cost_label.place(x = 250, y = 150)

    net_prize_label = Label(ques_1, text = "Net price", bg = "#fdd017", fg = "black", font = ('calibre',20,"italic"), relief = 'raised', width = 11, padx = 10, bd = 5)
    net_prize_label.place(x = 250, y = 210)


    # Making entry for original cost and net prize.
    original_cost_enter = Entry(ques_1, textvariable = DoubleVar(), justify = "right", bg = "white", fg = "black", font = ("Arial", 15), relief = "sunken", width = 24, bd = 10 )
    original_cost_enter.place(x = 475, y = 150)

    net_prize_enter = Entry(ques_1, textvariable = DoubleVar(), justify = "right", bg = "white", fg = "black", font = ("Arial", 15), relief = "sunken", width = 24, bd = 10 )
    net_prize_enter.place(x = 475, y = 210)


    # Submit button.
    submit_button = Button(ques_1, command = gst_calculator, text = "Calculate", font = ('Calibre', 20, "bold"), bg = "#fdd017", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
    submit_button.place(x = 400, y = 290)

    # Exit button.
    exit_button = Button(ques_1, command = ques_1.destroy, text = "EXit", font = ('Calibre', 20, "bold"), bg = "#fdd017", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
    exit_button.place(x = 435, y = 370)

    # Running question 1 loop.
    ques_1.mainloop()



# Question 2
def ques_2():

    # defining window for question 2.
    ques_2 = Toplevel(main)

    # Giving title to the window.
    ques_2.title("Calender")
    ques_2.config(background ="darkgreen")

    # Fixing size of the window.
    ques_2.minsize(width = 1000, height = 600)
    ques_2.maxsize(width = 1000, height = 600)

    # Making head label.
    head_label = Label(ques_2, text = "Calender.", fg = "black",bg = "#fdd017", font = ("allura",50,"bold"), relief = "sunke", bd = 5)
    head_label.pack(pady = 30)

    # function for second question.
    def calendar_1():

        # Taking out values entered by user.
        year = int(year_entry.get())

        # Printing appropiate result.
        if year < 0:
            msg_box = messagebox.showwarning("Calendar", "Year can't be negative. Please a positive integer.", parent = ques_2)
        
        else:
            # Defining a widget to show the calendar.
            calender_windown = Toplevel(ques_2)
            calender_windown.title(f"Calendar {year}" )
            calender_windown.minsize(width = 550, height = 400)

            # Generating calender label.
            text = calendar.calendar(year, 2,1,5,4)
            calendar_label = Label(calender_windown, text = text, font = "Consolas 9 bold", justify = LEFT)
            calendar_label.pack(padx = 20)

    # Making a Label for year.
    year_label = Label(ques_2, text = "Year", bg = "#fdd017", fg = "black", font = ('calibre',20,"bold"), relief = 'sunke',bd = 6, width = 5, padx = 10)
    year_label.place(x = 340, y = 150)

    # Creating a entry widget to take year as input.
    year_entry = Entry(ques_2, textvariable = IntVar(), justify = "right", bg = "white", fg = "black", font = ("Arial", 15), relief = "sunken", width = 15, bd = 10)
    year_entry.place(x = 473, y = 150)

    # print button.
    print_button = Button(ques_2, command = calendar_1, text = "Print calendar", font = ('Calibre', 20, "bold"), bg = "#fdd017", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
    print_button.place(x = 390, y = 230)

    # Exit button.
    exit_button = Button(ques_2, command = ques_2.destroy, text = "EXit", font = ('Calibre', 20, "bold"), bg = "#fdd017", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
    exit_button.place(x = 450, y = 320)

    ques_2.mainloop()



# Question 3 
def ques_3():

    # Defining ques 3 window.
    ques_3 = Toplevel(main)

    # Fixing size of the window.
    ques_3.minsize(width = 1000, height = 600)
    ques_3.maxsize(width = 1000, height = 600)

    # Giving title to window.
    ques_3.title("Calculator.")
    ques_3.config(background ="darkgreen")

    # Making head label. 
    head_label = Label(ques_3, text = "Calculator.", fg = "black",bg = "#fdd017", font = ("allura",50,"bold"), relief = "sunke", bd = 5)
    head_label.pack(pady = 30)


    # function for third question.
    def calculator():
        # Taking out values for which is to be performed.
        task = int_var.get()

        # performing task entered by the user.
        if task == 1:
            result = int_1.get() + int_2.get()
        elif task == 2:
            result = int_1.get() - int_2.get()
        elif task == 3:
            result = int_1.get() * int_2.get()
        else:
            result = int_1.get() / int_2.get()

        # Printing the result of the performed.
        result_label = Label(ques_3, bg = "#fdd017", fg = "black", font = ('calibre',20,"italic"), relief = 'raised', width = 11, padx = 10, bd = 5)
        result_label.place(x = 250 , y = 475)
        result_label.config(text = f"Result : {result}")


    # Making variables for numbers.
    int_1 = IntVar()
    int_2 = IntVar()

    # Making labels for original cost and net prize.
    first_num_label = Label(ques_3, text = "First number", bg = "#fdd017", fg = "black", font = ('calibre',20,"italic"), relief = 'raised', width = 11, padx = 10, bd = 5)
    first_num_label.place(x = 250, y = 150)

    second_num_label = Label(ques_3, text = "Second number", bg = "#fdd017", fg = "black", font = ('calibre',20,"italic"), relief = 'raised', width = 11, padx = 10, bd = 5)
    second_num_label.place(x = 250, y = 210)


    # Making entry for original cost and net prize.
    first_num_enter = Entry(ques_3, textvariable = int_1, justify = "right", bg = "white", fg = "black", font = ("Arial", 15), relief = "sunken", width = 24, bd = 10 )
    first_num_enter.place(x = 475, y = 150)

    second_num_enter = Entry(ques_3, textvariable = int_2, justify = "right", bg = "white", fg = "black", font = ("Arial", 15), relief = "sunken", width = 24, bd = 10 )
    second_num_enter.place(x = 475, y = 210)


    # Printing info about what to do next.
    info_label = Label(ques_3, text = "What you want to do?", bg = "#fdd017", fg = "black", font = ('calibre',20,"italic"), relief = 'raised', width = 24, padx = 10, bd = 5)
    info_label.place(x = 250, y = 265)


    # creating a variable.
    int_var = IntVar()

    # Creating radio button for taking input about what to do.
    add_radio = Radiobutton(ques_3, variable = int_var, value = 1  , command = calculator, text = "Addition", bg = "dark green", fg = "#fdd017", font = ('calibre',20,"italic"), relief = 'flat', padx = 10)
    add_radio.place(x = 250, y = 315)

    sub_radio = Radiobutton(ques_3, variable = int_var, value = 2  , command = calculator, text = "Subtraction", bg = "dark green", fg = "#fdd017", font = ('calibre',20,"italic"), relief = 'flat', padx = 10)
    sub_radio.place(x = 250, y = 350)

    mul_radio = Radiobutton(ques_3, variable = int_var, value = 3  , command = calculator, text = "Multiplication", bg = "dark green", fg = "#fdd017", font = ('calibre',20,"italic"), relief = 'flat', padx = 10)
    mul_radio.place(x = 250, y = 385)

    div_radio = Radiobutton(ques_3, variable = int_var, value = 4  , command = calculator, text = "Division", bg = "dark green", fg = "#fdd017", font = ('calibre',20,"italic"), relief = 'flat', padx = 10)
    div_radio.place(x = 250, y = 420)

    
    # Exit button.
    exit_button = Button(ques_3, command = ques_3.destroy, text = "EXit", font = ('Calibre', 20, "bold"), bg = "#fdd017", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
    exit_button.place(x = 500, y = 475)

# Making welcome label.
welcome_label = Label(main, text = "Welcome", bg = "orange", fg = "white", font = ('calibre',50,"bold"), relief = 'raised', width = 15, padx = 10, bd = 10)
welcome_label.pack(pady = 20)

# Selection label.
select_label = Label(main, text = "Please select one of the options given below.", bg = "pink", fg = "black", font = ('calibre',20,"bold"), relief = 'raised', width = 35, padx = 10, bd = 5)
select_label.pack()

# Making button on main window to move through question.
ques_1_button = Button(main, command = ques_1, text = "GST rate calculator.", font = ('Calibre', 20, "bold"), bg = "orange", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
ques_1_button.place(x = 185, y = 220)

ques_2_button = Button(main, command = ques_2, text = "Calender.", font = ('Calibre', 20, "bold"), bg = "orange", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
ques_2_button.place(x = 185, y = 300)

ques_3_button = Button(main, command = ques_3, text = "Calculator.", font = ('Calibre', 20, "bold"), bg = "orange", relief = "raised", bd = 5, activeforeground = "black", activebackground = "yellow")
ques_3_button.place(x = 185, y = 380)

# Exit button.
exit_button = Button(main, command = main.destroy, text = "Exit", font = ('Calibre', 20, "bold"), bg = "pink", relief = "raised", bd = 5, activeforeground = "white", activebackground = "pink")
exit_button.place(x = 425, y = 450)

# Running main loop.
main.mainloop()



# # # # # # # # # # # # # # # # # # # # # # # # # # 
# Question 4.
print("\n\t Question 4 \n")

# Inputed array.
inp_arr = []
count = 1

def input_arr():
    # Asking for the array to sort.
    while True:

        # Asking user whether he/she want to enter a arr in one go or as a whole.
        print("Do you want to enter the list as a whole or element by element.")
        ask = int(input("Enter 0 if you want to enter list in one go else 1: "))
        print()

        # Condition appropiate to user input.
        if ask == 0:
            tmp_arr = list(input("Please enter the whole list in coma(,) seperated list without brackets: \n").split(","))
            for ele in tmp_arr:
                inp_arr.append(int(ele))
            break

        elif ask != 1:
            print("Please enter a valid number(1 or 0)\n")

        else:
            # Asking user whether he/she want to enter more or not.
            check = input("\nDo you want to enter the element?(Y or N): ")

            # If user want to enter the element.
            if check == "Y":

                # Asking user for element and adding it in the imput arr list.
                temp = int(input(f"Enter the {count}th element (only integers): "))
                count += 1
                inp_arr.append(temp)

            # If user do want to enter more than exiting the loop.
            elif check == "N":
                break

            # If user input donot match
            else:
                print("Please enter a valid input(Y or N)")


# Defining recursive function for quick sort.
def quick_sort(inp_arr):
    
    # Base condition for recursive function.
    if len(inp_arr) <= 1:
        return inp_arr
    
    # doing recurrsion to sort arr.
    else:
        small_arr = [ele for ele in inp_arr if ele < inp_arr[0]]
        equal_arr = [ele for ele in inp_arr if ele == inp_arr[0]]
        large_arr = [ele for ele in inp_arr if ele > inp_arr[0]]

        return (quick_sort(small_arr) + equal_arr + quick_sort(large_arr))


# Calling our functions.
input_arr()
sorted_arr = quick_sort(inp_arr)

# Print the input arr.
print(f"\nYour inputted array is: {inp_arr}")

# Printing the sorted the list.
print(f"\nSorted arr of the arr inputed by you is {sorted_arr}")



# # # # # # # # # # # # # # # # # # # # # # # # # #
# Question 5.
print("\n\t Question 5 \n")

# Inputed array.
inp_arr = []
count = 1

# Calling our functions.
input_arr()
sorted_arr = quick_sort(inp_arr)

# Print the input arr.
print(f"\nYour inputted array is: {inp_arr}")

# printing the sorted list.
print(f"\nSorted list of the list entered by you: {sorted_arr}\n")

# Taking a element to search from user.
search = int(input("Enter the element you want to search: "))
print()

# Binary search algo.
found = -1
start = 0
end = len(sorted_arr) - 1

while start <= end:

        mid = (start + end)//2

        if sorted_arr[mid] == search:
            found = mid
            break
            
        elif sorted_arr[mid] < search:
            start = mid + 1
            
        else:
            end = mid - 1

# Printing the result.
if found == -1:
    print(f"{search} is not present in the input list.")
else:
    print(f"{search} is present in the list.")



# Part C.
# checking if element is in arr or not.
if found != -1:

    # definig some variables.
    lowest = -1
    highest = -1
    start = 0
    end = len(inp_arr) - 1

    # Calculating the loweest index of the number entered by user.
    while start <= end:

        mid = (start + end)//2

        if sorted_arr[mid] == search:
            lowest = mid
            end = mid - 1
            
        elif sorted_arr[mid] < search:
            start = mid + 1
            
        else:
            end = mid - 1


    start = 0
    end = len(inp_arr) - 1

    # Calculating the loweest index of the number entered by user.
    while start <= end:

        mid = (start + end)//2

        if sorted_arr[mid] == search:
            highest = mid
            start = mid + 1
            
        elif sorted_arr[mid] < search:
            start = mid + 1
            
        else:
            end = mid - 1

    # Calculating and printing the occurance.
    occurance = highest - lowest + 1
    print(f"\n{search} is found {occurance} times.")