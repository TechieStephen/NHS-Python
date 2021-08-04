from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("SUPERMART 2.0")
root.geometry("400x400")

Entry().pack()
Text(width=50, height=5).pack()

result = ''

Radiobutton(
    text='Option 1',
    value='1',
    variable=result
).pack()

Radiobutton(
    text='Option 2',
    value='2',
    variable=result
).pack()

Radiobutton(
    text='Option 3',
    value='3',
    variable=result
).pack()

Checkbutton(
    text='Option 1',
    variable=result
).pack()
Checkbutton(
    text='Option 2',
    variable=result
).pack()





root.mainloop()


def do(num1, num2, num3, num4, num5):
    print(num1 + num2)

do(56,56,34,34,465) #positional Argument

do(num5= 70, num3=60, num1=5, num2=6) #named argument

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stud = Student('james', 60)
stud2 = Student(age=60, name=90)