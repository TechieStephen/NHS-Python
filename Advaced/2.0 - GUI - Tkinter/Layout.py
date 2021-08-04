from tkinter import *

root = Tk()
root.title("SUPERMART 2.0")
root.geometry("400x400")

frame1 = Frame(root, bg='red', padx=20, pady=20)
# frame1.pack(anchor=W, side=BOTTOM)
frame1.pack(anchor=W, side=LEFT, fill=Y)

frame2 = Frame(root, bg='green', padx=20, pady=20)
frame2.pack(anchor=E, side=RIGHT, fill=Y)

btn1 = Button(frame1, text='Click Me')
btn1.pack()
btn2 = Button(frame1, text='Click Me 2')
btn2.pack()

btn3 = Button(frame2, text='Click Me 3')
btn3.pack()
btn4 = Button(frame2, text='Click Me 4')
btn4.pack()

btn5 = Button(root, text='Click Me 5')
root.mainloop()