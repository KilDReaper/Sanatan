from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def raise_frame(frame):
    frame.tkraise()

def create_buttons(parent, labels, frames):
    button_style = {'font': ('Helvetica', 14), 'bg': "#2C3E50", 'fg': "white", 'padx': 10, 'pady': 5, 'width': 15, 'height': 2}
    buttons = []
    for label in labels:
        button = Button(parent, text=label, command=lambda l=label: raise_frame(frames[l]))
        button.configure(**button_style)
        buttons.append(button)
    return buttons

def submit_reservation(vehicle_number_entry, owner_name_entry, contact_number_entry, vehicle_type_entry, tree, slot_buttons):
    vehicle_number = vehicle_number_entry.get().strip()
    owner_name = owner_name_entry.get().strip()
    contact_number = contact_number_entry.get().strip()
    vehicle_type = vehicle_type_entry.get().strip()
    
    if vehicle_number and owner_name and contact_number and vehicle_type:
        entry_time = datetime.now().strftime("%H:%M:%S")
        data = (len(tree.get_children()) + 1, vehicle_number, contact_number, owner_name, entry_time)
        tree.insert("", "end", values=data)
        
        # Change the color of the first available slot button to indicate the occupied slot
        for slot_button in slot_buttons:
            if slot_button["bg"] == "#2C3E50":  # Check if the slot is available
                slot_button.config(bg="red")   # Change color to indicate occupied slot
                break

        messagebox.showinfo("Reservation Submitted", "Your parking slot has been reserved successfully!")
        vehicle_number_entry.delete(0, END)
        owner_name_entry.delete(0, END)
        contact_number_entry.delete(0, END)
        vehicle_type_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

def dashboard(root, tree, slot_buttons):  # Pass tree and slot_buttons as arguments
    root.title("Dashboard")
    root.geometry("800x600")  

    frame1 = Frame(root, bg="#398376", width=200, height=600)
    frame1.grid(row=0, column=0, sticky="ns")

    frame_dashboard = Frame(root, bg="#2C3E50", bd=2, relief="solid")
    frame_complain = Frame(root, bg="#2C3E50", bd=2, relief="solid")  
    frame_reserve = Frame(root, bg="#2C3E50", bd=2, relief="solid") 

    frames = {"Dashboard": frame_dashboard, "Complain": frame_complain, "Reserve": frame_reserve}

    for frame in frames.values():
        frame.grid(row=0, column=1, sticky="nsew")

    labels = ["Dashboard", "Complain", "Reserve"]
    buttons = create_buttons(frame1, labels, frames)
    for i, button in enumerate(buttons, 1):
        button.grid(row=i, pady=10)

    Label(frame_dashboard, text="Dashboard Content", font=('Helvetica', 24), bg="#2C3E50", fg="white").pack(pady=20)

    Label(frame_complain, text="Submit a Complaint", font=('Helvetica', 20), bg="#2C3E50", fg="white").pack(pady=10)

    complaint_entry = Text(frame_complain, height=5, width=50, font=('Helvetica', 14))
    complaint_entry.pack(pady=10)

    submit_button = Button(frame_complain, text="Submit", font=('Helvetica', 16), bg="#2C3E50", fg="white")
    submit_button.pack(pady=10)

    Label(frame_reserve, text="Reserve Parking Slot", font=('Helvetica', 24), bg="#2C3E50", fg="white").pack(pady=20)

    Label(frame_reserve, text="Vehicle Number:", font=('Helvetica', 16), bg="#2C3E50", fg="white").pack(pady=5)
    vehicle_number_entry = Entry(frame_reserve, font=('Helvetica', 14))
    vehicle_number_entry.pack(pady=5)

    Label(frame_reserve, text="Owner Name:", font=('Helvetica', 16), bg="#2C3E50", fg="white").pack(pady=5)
    owner_name_entry = Entry(frame_reserve, font=('Helvetica', 14))
    owner_name_entry.pack(pady=5)

    Label(frame_reserve, text="Contact Number:", font=('Helvetica', 16), bg="#2C3E50", fg="white").pack(pady=5)
    contact_number_entry = Entry(frame_reserve, font=('Helvetica', 14))
    contact_number_entry.pack(pady=5)

    Label(frame_reserve, text="Vehicle Type:", font=('Helvetica', 16), bg="#2C3E50", fg="white").pack(pady=5)
    vehicle_type_entry = Entry(frame_reserve, font=('Helvetica', 14))
    vehicle_type_entry.pack(pady=5)

    submit_button = Button(frame_reserve, text="Submit", font=('Helvetica', 16), bg="#2C3E50", fg="white",
                           command=lambda: submit_reservation(vehicle_number_entry, owner_name_entry, contact_number_entry, vehicle_type_entry, tree, slot_buttons))
    submit_button.pack(pady=20)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

root = Tk()
# Create the treeview and slot_buttons here and pass them to the dashboard function
tree = ttk.Treeview(root)
slot_buttons = []  # Define the slot_buttons here
dashboard(root, tree, slot_buttons)
root.mainloop()