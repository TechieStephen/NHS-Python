from tkinter import *
from tkinter import messagebox

import tkinter as tk

root = Tk()
root.title("SUPERMART 2.0")
root.geometry("400x400")

# #Positioning Using Pack
# lbl_welcome = Label(text='Welome To SuperMART', bg='red')
# # lbl_welcome.pack(side=LEFT)
# lbl_welcome.pack(anchor=W, padx=10, pady=30)
#
# btn_click = Button(text='Click Me', bg='green')
# # btn_click.pack(side=RIGHT)
# btn_click.pack(anchor=W)

#Positioning Using Grid
lbl_welcome = Label(text='Welome To SuperMART')
lbl_msg = Label(text='Get discount NOW')

lbl_welcome.grid(row=0, column=0)
lbl_msg.grid(row=0, column=1)

btn_click = Button(text='Click Me', bg='green')
btn_click.grid(row=1, column=0)





root.mainloop()