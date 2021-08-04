from tkinter import *
from tkinter import ttk

root = Tk()
root.title("MENU")

style = ttk.Style()
style.configure(
    "lefttab.TNotebook",
    tabposition='nw'
)
menu = ttk.Notebook(root, style='lefttab.TNotebook')
menu.pack(fill='both', expand=1)

Home = Frame(menu, bg='red')
Products = Frame(menu, bg='green')
About = Frame(menu, bg='white')
Home.pack()
Products.pack()
About.pack()

menu.add(Home, text='Home')
menu.add(Products, text='Products')
menu.add(About, text='About')

lbl1 = Label(Home,text='Welcome')
lbl1.pack()

lbl2 = Label(Products,text='Products')
lbl2.pack()

lbl3 = Label(About,text='About')
lbl3.pack()
root.mainloop()