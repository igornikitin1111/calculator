from tkinter import *

def button_click(number):
    # number_entry.delete(o, END)
    current = number_entry.get()
    number_entry.delete(0, END)
    number_entry.insert(0, str(current) + str(number))

def button_clear1():
    number_entry.delete(0, END)

def button_add1():
    first_number = number_entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    number_entry.delete(0, END)

def button_equal1():
    second_number = number_entry.get()
    number_entry.delete(0, END)

    if math == "addition":
        number_entry.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        number_entry.insert(0, f_num - int(second_number))

    if math == "multiplication":
        number_entry.insert(0, f_num * int(second_number))

    if math == "division":
        number_entry.insert(0, f_num / int(second_number))

def button_subtract1():
    first_number = number_entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    number_entry.delete(0, END)

def button_multiply1():
    first_number = number_entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    number_entry.delete(0, END)

def button_divide1():
    first_number = number_entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    number_entry.delete(0, END)

root = Tk()
root.title("Simple calculator")

number_entry = Entry(root, width=35, borderwidth=5)
number_entry.grid(row=0, column=0, 
    columnspan=3, #columnspan makes room for 3 columns lower
    padx=10, pady=10)
# number_entry.insert(0, "Type number: ")

# Define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add1)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal1)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear1)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract1)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply1)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide1)

# Put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()