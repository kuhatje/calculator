import tkinter

root = tkinter.Tk()
root.title("Calculator")

entry_box = tkinter.Entry(root, width=35, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def enter_number(number):
    current_value = entry_box.get()
    entry_box.delete(0, tkinter.END)
    entry_box.insert(0, str(current_value) + str(number))


# Clear the entry box.
def clear():
    entry_box.delete(0, tkinter.END)


def add():
    global first_number
    global operation
    operation = "add"
    first_number = int(entry_box.get())
    clear()


def subtract():
    global first_number
    global operation
    operation = "subtract"
    first_number = int(entry_box.get())
    clear()


def multiply():
    global first_number
    global operation
    operation = "multiply"
    first_number = int(entry_box.get())
    clear()


def divide():
    global first_number
    global operation
    operation = "divide"
    first_number = int(entry_box.get())
    clear()


def equal():
    second_number = entry_box.get()
    clear()
    if operation == "add":
        entry_box.insert(0, first_number + int(second_number))
    elif operation == "subtract":
        entry_box.insert(0, first_number - int(second_number))
    elif operation == "multiply":
        entry_box.insert(0, first_number * int(second_number))
    elif operation == "divide":
        entry_box.insert(0, first_number / int(second_number))


# Buttons for the numbers
button_1 = tkinter.Button(root, text="1", padx=40, pady=20, command=lambda: enter_number(1))
button_2 = tkinter.Button(root, text="2", padx=40, pady=20, command=lambda: enter_number(2))
button_3 = tkinter.Button(root, text="3", padx=40, pady=20, command=lambda: enter_number(3))
button_4 = tkinter.Button(root, text="4", padx=40, pady=20, command=lambda: enter_number(4))
button_5 = tkinter.Button(root, text="5", padx=40, pady=20, command=lambda: enter_number(5))
button_6 = tkinter.Button(root, text="6", padx=40, pady=20, command=lambda: enter_number(6))
button_7 = tkinter.Button(root, text="7", padx=40, pady=20, command=lambda: enter_number(7))
button_8 = tkinter.Button(root, text="8", padx=40, pady=20, command=lambda: enter_number(8))
button_9 = tkinter.Button(root, text="9", padx=40, pady=20, command=lambda: enter_number(9))
button_0 = tkinter.Button(root, text="0", padx=40, pady=20, command=lambda: enter_number(0))

# Buttons for the operators
button_add = tkinter.Button(root, text="+", padx=39, pady=20, command=lambda: add())
button_subtract = tkinter.Button(root, text="-", padx=41, pady=20, command=lambda: subtract())
button_multiply = tkinter.Button(root, text="*", padx=40, pady=20, command=lambda: multiply())
button_divide = tkinter.Button(root, text="/", padx=41, pady=20, command=lambda: divide())
button_equals = tkinter.Button(root, text="=", padx=91, pady=20, command=lambda: equal())
button_clear = tkinter.Button(root, text="Clear", padx=79, pady=20, command=lambda: clear())

# Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equals.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
