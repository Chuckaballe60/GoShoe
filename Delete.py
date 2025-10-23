import os
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Configure appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# In-memory data
shoes = []
sales = []

def open_delete_window():
    win = ctk.CTkToplevel()
    win.title("Delete Records")
    win.geometry("900x700")
    win.grab_set()

    # Main container
    container = ctk.CTkFrame(win)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    # Header
    header = ctk.CTkLabel(
        container,
        text="Delete Records",
        font=ctk.CTkFont(size=28, weight="bold")
    )
    header.pack(pady=20)

    # Shoe Deletion Section
    shoe_frame = ctk.CTkFrame(container)
    shoe_frame.pack(fill="x", padx=20, pady=10)

    shoe_header = ctk.CTkLabel(
        shoe_frame,
        text="Remove Discontinued Shoe",
        font=ctk.CTkFont(size=20, weight="bold")
    )
    shoe_header.pack(pady=10)

    # Shoe selection
    shoe_select_frame = ctk.CTkFrame(shoe_frame)
    shoe_select_frame.pack(fill="x", padx=20, pady=10)
    
    shoe_names = [s.get('name', '') for s in shoes]
    shoe_select = ctk.CTkComboBox(
        shoe_select_frame,
        values=shoe_names,
        width=300,
        placeholder_text="Select shoe to delete"
    )
    shoe_select.pack(pady=10)

    def delete_shoe():
        shoe = shoe_select.get()
        if not shoe:
            messagebox.showwarning("Select", "Please select a shoe to delete")
            return
        
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete '{shoe}'?"):
            global shoes
            shoes = [s for s in shoes if s.get('name') != shoe]
            messagebox.showinfo('Success', f"Shoe '{shoe}' deleted!")
            shoe_select.configure(values=[s.get('name', '') for s in shoes])
            shoe_select.set("")

    ctk.CTkButton(
        shoe_frame,
        text="Delete Shoe",
        command=delete_shoe,
        fg_color="#e74c3c",
        hover_color="#c0392b",
        width=200
    ).pack(pady=10)

    # Sales Deletion Section
    sale_frame = ctk.CTkFrame(container)
    sale_frame.pack(fill="x", padx=20, pady=20)

    sale_header = ctk.CTkLabel(
        sale_frame,
        text="Delete Sales Entry",
        font=ctk.CTkFont(size=20, weight="bold")
    )
    sale_header.pack(pady=10)

    # Sales form
    sale_form = ctk.CTkFrame(sale_frame)
    sale_form.pack(fill="x", padx=20, pady=10)

    # Shoe in sale
    shoe_sale_frame = ctk.CTkFrame(sale_form)
    shoe_sale_frame.pack(fill="x", pady=5)
    ctk.CTkLabel(shoe_sale_frame, text="Shoe Name:").pack(side="left", padx=10)
    sale_shoe = ctk.CTkEntry(shoe_sale_frame, width=200)
    sale_shoe.pack(side="left", padx=10)

    # Customer in sale
    cust_sale_frame = ctk.CTkFrame(sale_form)
    cust_sale_frame.pack(fill="x", pady=5)
    ctk.CTkLabel(cust_sale_frame, text="Customer:").pack(side="left", padx=10)
    sale_cust = ctk.CTkEntry(cust_sale_frame, width=200)
    sale_cust.pack(side="left", padx=10)

    def delete_sale():
        shoe = sale_shoe.get().strip()
        customer = sale_cust.get().strip()
        
        if not shoe and not customer:
            messagebox.showwarning("Input", "Enter at least shoe name or customer")
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this sale?"):
            global sales
            sales = [s for s in sales if not (
                (shoe and s.get('shoe') == shoe) and 
                (customer and s.get('customer') == customer)
            )]
            messagebox.showinfo('Success', "Sale entry deleted!")
            sale_shoe.delete(0, 'end')
            sale_cust.delete(0, 'end')

    ctk.CTkButton(
        sale_frame,
        text="Delete Sale",
        command=delete_sale,
        fg_color="#f39c12",
        hover_color="#d35400",
        width=200
    ).pack(pady=10)

    # Try to load and display background image
    try:
        bg_path = os.path.join(".", "Images", "delete_bg.png")
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