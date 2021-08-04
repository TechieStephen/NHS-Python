import tkinter as tk

window = tk.Tk()
window.title('Main Window')

def openLoginScreen():
    login_screen = tk.Toplevel()
    login_screen.title("LOGIN")
    login_screen.iconbitmap("images/login.ico")

    tk.Label(login_screen,text="Login Here").pack()

    btn_close = tk.Button(login_screen,text="CLOSE", command=login_screen.destroy)
    btn_close.pack(padx=100, pady=100)

btn_login = tk.Button(text="LOGIN", command=openLoginScreen, state="disabled")
btn_login.pack(padx=100, pady=100)

window.mainloop()