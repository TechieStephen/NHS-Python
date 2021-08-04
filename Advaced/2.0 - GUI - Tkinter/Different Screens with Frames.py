from tkinter import *

window = Tk()
my_menu= Menu(window)
window.configure(menu=my_menu)
window.title('Main Window')
# window.geometry('600x500')




loginFrame = Frame(window, width=400, height=400, bg='red')
homeFrame = Frame(window, width=400, height=400, bg='green')


def loginScreen():
    hideFrames()
    loginFrame.pack(fill='both', expand=1)


def homeScreen():
    hideFrames()
    homeFrame.pack(fill='both', expand=1)


def hideFrames():
    loginFrame.pack_forget()
    homeFrame.pack_forget()

#create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label='Login', command=loginScreen)

#create a menu item
home_menu = Menu(my_menu)
my_menu.add_cascade(label='Home', menu=home_menu)
home_menu.add_command(label='Home', command=homeScreen)


btn1 = Button(text='Login', command=loginScreen).pack()
btn3 = Button(text='Home', command=homeScreen).pack()

loginScreen()

#
# topFrame = Frame(bg='red', padx=10, pady=10)
# topFrame.pack(fill=X)
#
# btn1 = Button(topFrame,text='Button 1')
# btn2 = Button(topFrame,text='Button 2')
# btn3 = Button(topFrame,text='Button 3')
# btn1.pack(side=LEFT)
# btn2.pack(side=LEFT)
# btn3.pack(side=RIGHT)
#
#
# bottomFrame = Frame(bg='green', padx=10, pady=10)
# bottomFrame.pack(anchor=W, side=BOTTOM, fill=X)
#
# btn4 = Button(bottomFrame,text='Button 4')
# btn4.pack()

window.mainloop()
