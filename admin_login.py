from tkinter import *
from tkinter import messagebox


def login(entry_username, entry_password):
    password = entry_password.get()
    username = entry_username.get()
    root.destroy()
 
    if username == "" or password == "":
        messagebox.showerror("Error", "Blank Not Allowed")
    elif username == "admin" and password == "admin":
        from counter import dashboard
        dashboard()
    else:
        messagebox.showerror("Error", "Incorrect username and password")

root = Tk()
root.title("Login")
root.geometry("900x900")
root.config(bg="#53d1df")
Label(root, text="Username", font=('georgia', 12, 'bold'), bg="#53d1df", fg="white").place(x=20, y=20)
Label(root, text="Password", font=('Arial', 12, 'bold'), bg="#53d1df", fg="white").place(x=20, y=70)
 
entry_username = Entry(root, font=('georgia', 12), bd=5)
entry_password = Entry(root, show="*", font=('georgia', 12), bd=5)
 
entry_username.place(x=140, y=20)
entry_password.place(x=140, y=70)
 
login_button = Button(root, text="Login", command=lambda: login(entry_username, entry_password), height=2, width=13, font=('Arial', 12, 'bold'), bg="#E74C3C", fg="white")
login_button.place(x=100, y=120)
 
root.mainloop()
