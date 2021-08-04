# import tkinter as tk
# from PIL import ImageTk, Image
#
# window = tk.Tk()
# window.title('Images')
# window.iconbitmap('images/calculator 2.0.ico')
#
# student_image = ImageTk\
#     .PhotoImage(Image.open('images/student.jpg'))
# img_label = tk.Label(image=student_image)
# img_label.pack()
#
# window.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

window = tk.Tk()
window.title('Main Window')
window.geometry('300x300')
window.configure(bg='#000000')


def showImage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir='/',
        title='Select an Image',
        filetypes=(('images', '*.png, *.jpg'), ('all files', '*.*')))

    user_image = Image.open(filename)
    user_image.thumbnail((200,200))
    user_image = ImageTk.PhotoImage(user_image)
    lbl_image.configure(image=user_image, bg='black')
    lbl_image.image = user_image
    lbl_image.pack()

    lbl_image_Name.configure(text=filename, bg='black', fg='white')
    lbl_image_Name.pack()

def exitApp():
    result = messagebox.askokcancel(
        'Exit App',
        'Are you sure you want to Exit App'
    )

    if result == True:
        window.destroy()

lbl_image = tk.Label(width=200, height=200)
lbl_image_Name = tk.Label()

# lbl_image = tk.Label(width=200, height=200)
bottomFrame = tk.Frame(window, bg='lightgrey' ,width=300, height=100)
bottomFrame.pack(side=tk.BOTTOM, fill=tk.X)

btn_browse = tk.Button(
    bottomFrame,
    text='Browse',
    command=showImage,
    font='trebuchet 13',
    bg='grey',
    fg='white',
    borderwidth=0
)
btn_browse.pack(padx=10, pady=10, side=tk.LEFT )
btn_close = tk.Button(
    bottomFrame,
    text='Exit',
    font='trebuchet 13',
    bg='grey',
    fg='white',
    bd=0,
    command=exitApp
)
btn_close.pack(padx=10, pady=10, side=tk.RIGHT)
window.mainloop()