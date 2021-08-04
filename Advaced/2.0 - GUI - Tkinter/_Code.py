from tkinter import *

root = Tk()
root.title("CALCULATOR 2.0")
root.iconbitmap("images/calculator 2.0.ico")

#Variables
first_num = IntVar()
operator = StringVar()

#Functions
def click(num):
    old_num = txt_input.get()
    if len(old_num) != 11:
        clear()
        txt_input.insert(0, old_num + str(num))

def clear():
    txt_input.delete(0, END)

def add():
    first_num.set(txt_input.get())
    operator.set('+')
    clear()

def sub():
    first_num.set(txt_input.get())
    operator.set('-')
    clear()

def multipy():
    first_num.set(txt_input.get())
    operator.set('x')
    clear()

def divide():
    first_num.set(txt_input.get())
    operator.set('/')
    clear()

def equal():
    num1 = int(first_num.get())
    num2 = int(txt_input.get())

    if operator.get() == '+':
       result = num1 + num2
       clear()
       txt_input.insert(0, result)
    elif operator.get() == '-':
       result = num1 - num2
       clear()
       txt_input.insert(0, result)
    elif operator.get() == '/':
        result = num1 / num2
        clear()
        txt_input.insert(0, result)
    elif operator.get() == 'x':
        result = num1 * num2
        clear()
        txt_input.insert(0, result)

txt_input = Entry(width=40)
txt_input.grid(row=0, column=0, columnspan=3,
               padx=10, pady=10)

#Define buttons
button_1 = Button(
    text='1', padx=40, pady=20,
    command=lambda:click(1))

button_2 = Button(
    text='2', padx=40, pady=20,
    command=lambda:click(2))

button_3 = Button(
    text='3', padx=40, pady=20,
    command=lambda:click(3))

button_4 = Button(
    text='4', padx=40, pady=20,
    command=lambda:click(4))
button_5 = Button(
    text='5', padx=40, pady=20,
    command=lambda:click(5))

button_6 = Button(
    text='6', padx=40, pady=20,
    command=lambda:click(6))

button_7 = Button(text='7', padx=40, pady=20,
    command=lambda:click(7))

button_8 = Button(text='8', padx=40, pady=20,
    command=lambda:click(8))

button_9 = Button(
    text='9', padx=40, pady=20,
    command=lambda:click(9))

button_0 = Button(
    text='0', padx=40, pady=20,
    command=lambda:click(0))

button_add = Button(
    text='+', padx=39, pady=20,
    command=add
)

button_equal = Button(
    text='=', padx=86, pady=20,
    command=equal
)

button_clear = Button(
    text='clear', padx=77, pady=20,
    command=clear
)

button_subtract = Button(
    text='-', padx=40.2, pady=20,
    command = sub
)
button_multiply = Button(
    text='x', padx=40.2, pady=20,
    command = multipy
)
button_divide = Button(
    text='/', padx=40.2, pady=20,
    command = divide
)

#Put Button On Screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()