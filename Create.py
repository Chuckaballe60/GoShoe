import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Configure CustomTkinter appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# In-memory data
shoes = []
customers = []
sales = []

def open_create_window():
    win = ctk.CTkToplevel()
    win.title('Create Entries')
    win.geometry('1280x850')
    win.grab_set()

    # Main container
    container = ctk.CTkFrame(win)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    # Create tabs
    tabs = ctk.CTkTabview(container)
    tabs.pack(fill="both", expand=True)
    
    # Add tabs
    tabs.add("Add Shoe")
    tabs.add("Register Customer")
    tabs.add("Record Sale")

    # === Shoe Tab ===
    shoe_frame = tabs.tab("Add Shoe")
    
    ctk.CTkLabel(shoe_frame, text="Add New Shoe", 
                 font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    fields = {}
    for label in ["Shoe Name", "Size", "Price", "Stock", "Brand"]:
        frame = ctk.CTkFrame(shoe_frame)
        frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(frame, text=label, width=100).pack(side="left", padx=10)
        entry = ctk.CTkEntry(frame, width=200)
        entry.pack(side="left", padx=10)
        fields[label] = entry

    def add_shoe():
        data = {
            'name': fields["Shoe Name"].get(),
            'size': fields["Size"].get(),
            'price': fields["Price"].get(),
            'stock': fields["Stock"].get(),
            'brand': fields["Brand"].get()
        }
        if not all(data.values()):
            messagebox.showwarning("Validation", "All fields are required!")
            return
        shoes.append(data)
        messagebox.showinfo('Success', 'Shoe added successfully!')
        for entry in fields.values():
            entry.delete(0, 'end')

    ctk.CTkButton(shoe_frame, text="Add Shoe", 
                  command=add_shoe,
                  fg_color="#2ecc71", 
                  hover_color="#27ae60").pack(pady=20)

    # === Customer Tab ===
    cust_frame = tabs.tab("Register Customer")
    
    ctk.CTkLabel(cust_frame, text="Register New Customer", 
                 font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    cust_fields = {}
    for label in ["Customer Name", "Age", "Phone", "Address"]:
        frame = ctk.CTkFrame(cust_frame)
        frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(frame, text=label, width=100).pack(side="left", padx=10)
        entry = ctk.CTkEntry(frame, width=200)
        entry.pack(side="left", padx=10)
        cust_fields[label] = entry

    def add_customer():
        data = {
            'name': cust_fields["Customer Name"].get(),
            'age': cust_fields["Age"].get(),
            'phone': cust_fields["Phone"].get(),
            'address': cust_fields["Address"].get()
        }
        if not all(data.values()):
            messagebox.showwarning("Validation", "All fields are required!")
            return
        customers.append(data)
        messagebox.showinfo('Success', 'Customer registered successfully!')
        for entry in cust_fields.values():
            entry.delete(0, 'end')

    ctk.CTkButton(cust_frame, text="Register Customer", 
                  command=add_customer,
                  fg_color="#3498db", 
                  hover_color="#2980b9").pack(pady=20)

    # === Sales Tab ===
    sale_frame = tabs.tab("Record Sale")
    
    ctk.CTkLabel(sale_frame, text="Record Sales Transaction", 
                 font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

    sale_fields = {}
    for label in ["Shoe Name", "Customer Name", "Quantity", "Amount"]:
        frame = ctk.CTkFrame(sale_frame)
        frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(frame, text=label, width=100).pack(side="left", padx=10)
        entry = ctk.CTkEntry(frame, width=200)
        entry.pack(side="left", padx=10)
        sale_fields[label] = entry

    def add_sale():
        data = {
            'shoe': sale_fields["Shoe Name"].get(),
            'customer': sale_fields["Customer Name"].get(),
            'quantity': sale_fields["Quantity"].get(),
            'amount': sale_fields["Amount"].get()
        }
        if not all(data.values()):
            messagebox.showwarning("Validation", "All fields are required!")
            return
        sales.append(data)
        messagebox.showinfo('Success', 'Sale recorded successfully!')
        for entry in sale_fields.values():
            entry.delete(0, 'end')

    ctk.CTkButton(sale_frame, text="Record Sale", 
                  command=add_sale,
                  fg_color="#e67e22", 
                  hover_color="#d35400").pack(pady=20)

    # Try to load and display background image
    try:
        bg_path = os.path.join(".", "Images", "create_bg.png")
        if os.path.exists(bg_path):
            bg_image = Image.open(bg_path)
            bg_photo = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, 
                                  size=(300, 200))
            bg_label = ctk.CTkLabel(container, image=bg_photo, text="")
            bg_label.place(relx=0.99, rely=0.99, anchor="se")
    except Exception as e:
        print(f"Failed to load background image: {e}")

    return win