from tkinter import *

root = Tk()
root.title("SUPERMART 2.0")
root.geometry("400x400")

def do():
    name = txt_name.get()
    if name == "":
        print("Erro enter your name")
    else:
        print(txt_name.get())

def clear():
    txt_name.delete(0, END)

Label(text="Welcome to SuperMART", fg="red", bg="grey").pack()
Button(text="Click Me", command=do, fg="white", bg="grey").pack()

txt_name = Entry()
txt_name.pack()

lbl_msg = Button(text="Clear", command=clear)
lbl_msg.pack()

root.mainloop()