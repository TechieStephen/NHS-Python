import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title('Main Window')
window.geometry('300x300')

def info():
    messagebox.showinfo("Your Password", "12345")

def error():
    messagebox.showerror("Invalid Pass Code", "Your pass code is invalid")

def okCancel():
    messagebox.askokcancel("Comfirm", "Are you sure you want to exit")

def askQuestion():
    messagebox.askquestion("Are Sure", "Are you sure you want to exit")


tk.Button(window, text='INFO', command=info).pack()
tk.Button(window, text='ERROR', command=error).pack()
tk.Button(window, text='OK Cancel', command=okCancel).pack()
tk.Button(window, text='Ask Question', command=askQuestion).pack()

window.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# window = tk.Tk()
# window.title('Main Window')
# window.geometry('300x300')

# def okCancel():
#     res = messagebox.\
#         askokcancel("Comfirm", "Are you sure you want to exit")
#     if res:
#         print("You clicked okay")
#     else:
#         print("You clicked Cancel")

# def askQuestion():
#     res = messagebox.askquestion("Are Sure", "Are you sure you want to exit")
#     if res == 'yes':
#         print("You clicked YES")
#     else:
#         print("You clicked NO")

# tk.Button(window, text='OK Cancel', command=okCancel).pack()
# tk.Button(window, text='Ask Question', command=askQuestion).pack()

# window.mainloop()