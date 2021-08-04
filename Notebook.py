from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x500')

style = ttk.Style(root)
style.configure("lefttab.TNotebook", tabposition='wn')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')
notebook.pack(fill='both', expand=1)

tab1 = Frame(notebook, bg="red")
tab2 = Frame(notebook, bg="green")
tab1.pack(fill='both', expand=1)
tab2.pack(fill='both', expand=1)

notebook.add(tab1, text=' Tab 1 ')
notebook.add(tab2, text=' Tab 2 ')


lbl_tab1 = Label(tab1,text='Tab 1')
lbl_tab1.pack()

lbl_tab2 = Label(tab2,text='Tab 2')
lbl_tab2.pack()
root.mainloop()