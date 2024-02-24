from tkinter import *
import tkinter as tk

def display_vehicle():
    from display import fetch_all_info
    fetch_all_info()

def add_vehicles():
    from Slots import add_vehicle
    add_vehicle()

root = Tk()
root.geometry("900x900")
root.config(bg="#2da380")
root.title("Dashboard")
   
button_frame = tk.Frame(root, bg="#2da380")
button_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

button1 = tk.Button(button_frame, text="Home", bg="#53d1df", width=15, height= 7, font=('georgia', 12, 'bold'))
button1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

button2 = tk.Button(button_frame, text="Add vehicle", command=add_vehicles, bg="#53d1df", width=15, height= 7, font=('georgia', 12, 'bold'))
button2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

button3 = tk.Button(button_frame, text="Manage Vehicle", command=display_vehicle, bg="#53d1df", width=15, height= 7, font=('georgia', 12, 'bold')  )
button3.grid(row=2, column=0, padx=10, pady=5, sticky="w")

root.mainloop()