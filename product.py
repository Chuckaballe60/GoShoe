from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# In-memory shoe data
shoes = []

def connect_to_product():
    # GUI part
    root = Toplevel()
    style = ttk.Style(root)
    style.theme_use("default")
    root.geometry("1400x750+65+15")
    root.title("Shoe Table")
    root.config(bg='whitesmoke')
    root.resizable(0,0)

    heading_label = Label(root, font=("Arial", 30,"bold"), pady=15, bg="whitesmoke")
    heading_label.pack()

    middleFrame = Frame(root, bg="white", highlightbackground='black', highlightthickness=1)
    middleFrame.place(x=50, y=100, width=1300, height=520)

    productTable = ttk.Treeview(middleFrame, columns=('id','name','price','brand','section'))
    productTable.pack(fill=BOTH, expand=1)

    # Configure columns
    productTable.heading('id', text='Shoe ID')
    productTable.heading('name', text='Shoe Name')
    productTable.heading('price', text='Price')
    productTable.heading('brand', text='Brand')
    productTable.heading('section', text='Section')

    # Column widths
    for col in ('id','name','price','brand','section'):
        productTable.column(col, width=200, anchor=CENTER)

    def slide_text(label, text):
        label.config(text=text)
    
    def refresh_table():
        for item in productTable.get_children():
            productTable.delete(item)
        for shoe in shoes:
            productTable.insert('', 'end', values=(
                shoe.get('id', ''),
                shoe.get('name', ''),
                shoe.get('price', ''),
                shoe.get('brand', ''),
                shoe.get('section', '')
            ))

    # Button Frame
    buttonFrame = Frame(root, bg='whitesmoke')
    buttonFrame.place(x=50, y=650, width=1300, height=80)

    # Buttons
    Button(buttonFrame, text='Add', command=lambda: add_data(), 
           bg='#4CAF50', fg='white', width=10).pack(side=LEFT, padx=10)
    Button(buttonFrame, text='Update', command=lambda: update_data(),
           bg='#2196F3', fg='white', width=10).pack(side=LEFT, padx=10)
    Button(buttonFrame, text='Delete', command=lambda: delete(),
           bg='#f44336', fg='white', width=10).pack(side=LEFT, padx=10)
    Button(buttonFrame, text='Search', command=lambda: search_data(),
           bg='#FF9800', fg='white', width=10).pack(side=LEFT, padx=10)
    Button(buttonFrame, text='View All', command=lambda: view(),
           bg='#607D8B', fg='white', width=10).pack(side=LEFT, padx=10)

    refresh_table()
    root.grab_set()
    return root