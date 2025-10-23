import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Configure appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# In-memory data
shoes = []
customers = []

def open_update_window():
    win = ctk.CTkToplevel()
    win.title("Update Records")
    win.geometry("900x700")
    win.grab_set()

    # Main container with tabs
    container = ctk.CTkFrame(win)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    tabs = ctk.CTkTabview(container)
    tabs.pack(fill="both", expand=True)
    tabs.add("Update Shoe")
    tabs.add("Update Customer")

    # === Shoe Update Tab ===
    shoe_frame = tabs.tab("Update Shoe")
    
    ctk.CTkLabel(
        shoe_frame, 
        text="Update Shoe Information",
        font=ctk.CTkFont(size=24, weight="bold")
    ).pack(pady=20)

    # Shoe selection
    select_frame = ctk.CTkFrame(shoe_frame)
    select_frame.pack(fill="x", padx=20, pady=10)
    ctk.CTkLabel(select_frame, text="Select Shoe:").pack(side="left", padx=10)
    shoe_names = [s.get('name', '') for s in shoes]
    shoe_select = ctk.CTkComboBox(select_frame, values=shoe_names, width=200)
    shoe_select.pack(side="left", padx=10)

    # Fields frame
    fields_frame = ctk.CTkFrame(shoe_frame)
    fields_frame.pack(fill="x", padx=20, pady=20)

    shoe_fields = {}
    labels = ["New Price", "New Size", "New Stock"]
    
    for i, label in enumerate(labels):
        row = ctk.CTkFrame(fields_frame)
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text=label, width=100).pack(side="left", padx=10)
        entry = ctk.CTkEntry(row, width=200)
        entry.pack(side="left", padx=10)
        shoe_fields[label] = entry

    def update_shoe():
        shoe = shoe_select.get()
        if not shoe:
            messagebox.showwarning("Select", "Please select a shoe to update")
            return
            
        updates = {
            'price': shoe_fields["New Price"].get(),
            'size': shoe_fields["New Size"].get(),
            'stock': shoe_fields["New Stock"].get()
        }
        
        if not any(updates.values()):
            messagebox.showwarning("Input", "Enter at least one new value")
            return
            
        for s in shoes:
            if s['name'] == shoe:
                if updates['price']: s['price'] = updates['price']
                if updates['size']: s['size'] = updates['size']
                if updates['stock']: s['stock'] = updates['stock']
                messagebox.showinfo('Success', f'Shoe "{shoe}" updated!')
                for entry in shoe_fields.values():
                    entry.delete(0, 'end')
                return
                
        messagebox.showerror('Error', 'Shoe not found!')

    ctk.CTkButton(
        shoe_frame,
        text="Update Shoe",
        command=update_shoe,
        fg_color="#2ecc71",
        hover_color="#27ae60"
    ).pack(pady=20)

    # === Customer Update Tab ===
    cust_frame = tabs.tab("Update Customer")
    
    ctk.CTkLabel(
        cust_frame,
        text="Update Customer Information",
        font=ctk.CTkFont(size=24, weight="bold")
    ).pack(pady=20)

    # Customer selection
    cust_select_frame = ctk.CTkFrame(cust_frame)
    cust_select_frame.pack(fill="x", padx=20, pady=10)
    ctk.CTkLabel(cust_select_frame, text="Select Customer:").pack(side="left", padx=10)
    cust_names = [c.get('name', '') for c in customers]
    cust_select = ctk.CTkComboBox(cust_select_frame, values=cust_names, width=200)
    cust_select.pack(side="left", padx=10)

    # Customer fields
    cust_fields_frame = ctk.CTkFrame(cust_frame)
    cust_fields_frame.pack(fill="x", padx=20, pady=20)

    cust_fields = {}
    cust_labels = ["New Phone", "New Address"]
    
    for i, label in enumerate(cust_labels):
        row = ctk.CTkFrame(cust_fields_frame)
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text=label, width=100).pack(side="left", padx=10)
        entry = ctk.CTkEntry(row, width=200)
        entry.pack(side="left", padx=10)
        cust_fields[label] = entry

    def update_customer():
        customer = cust_select.get()
        if not customer:
            messagebox.showwarning("Select", "Please select a customer to update")
            return
            
        updates = {
            'phone': cust_fields["New Phone"].get(),
            'address': cust_fields["New Address"].get()
        }
        
        if not any(updates.values()):
            messagebox.showwarning("Input", "Enter at least one new value")
            return
            
        for c in customers:
            if c['name'] == customer:
                if updates['phone']: c['phone'] = updates['phone']
                if updates['address']: c['address'] = updates['address']
                messagebox.showinfo('Success', f'Customer "{customer}" updated!')
                for entry in cust_fields.values():
                    entry.delete(0, 'end')
                return
                
        messagebox.showerror('Error', 'Customer not found!')

    ctk.CTkButton(
        cust_frame,
        text="Update Customer",
        command=update_customer,
        fg_color="#3498db",
        hover_color="#2980b9"
    ).pack(pady=20)

    # Try to load and display background image
    try:
        bg_path = os.path.join(".", "Images", "update_bg.png")
        if os.path.exists(bg_path):
            bg_image = Image.open(bg_path)
            bg_photo = ctk.CTkImage(
                light_image=bg_image,
                dark_image=bg_image,
                size=(200, 150)
            )
            bg_label = ctk.CTkLabel(container, image=bg_photo, text="")
            bg_label.place(relx=0.98, rely=0.98, anchor="se")
    except Exception as e:
        print(f"Failed to load background image: {e}")

    return win