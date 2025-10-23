# ...existing code...
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import os

# In-memory data (import or share with other modules as needed)
shoes = []
sales = []


def open_retrieve_window():
    win = Toplevel()
    win.title('View / Search Data')
    win.geometry('1000x650')
    win.configure(bg='#f5f7fa')
    win.grab_set()
    win.resizable(False, False)

    # Keep references to images to avoid garbage collection
    win._images = {}

    # Top banner
    banner = Frame(win, bg='#2b2f77', height=80)
    banner.pack(fill=X, side=TOP)
    Label(banner, text='Soul Kicks — View & Search', bg='#2b2f77', fg='white',
          font=('Segoe UI', 18, 'bold')).pack(padx=20, pady=18, anchor=W)

    body = Frame(win, bg='#f5f7fa')
    body.pack(fill=BOTH, expand=True, padx=16, pady=12)

    # Left panel: controls and lists
    left = Frame(body, bg='#f5f7fa', width=560)
    left.pack(side=LEFT, fill=Y, padx=(0, 12), pady=4)

    # Search area
    search_frame = LabelFrame(left, text='Search Shoes', bg='#f5f7fa', font=('Segoe UI', 10, 'bold'))
    search_frame.pack(fill=X, padx=6, pady=(6, 12))

    Label(search_frame, text='Name / Brand:', bg='#f5f7fa').grid(row=0, column=0, padx=8, pady=8, sticky=W)
    search_var = StringVar()
    search_entry = Entry(search_frame, textvariable=search_var, width=28, font=('Segoe UI', 10))
    search_entry.grid(row=0, column=1, padx=6, pady=8, sticky=W)

    Button(search_frame, text='Search', bg='#1f8feb', fg='white', activebackground='#1677c6',
           command=lambda: populate_shoes_tree(filter_text=search_var.get())).grid(row=0, column=2, padx=6)
    Button(search_frame, text='Clear', command=lambda: (search_var.set(''), populate_shoes_tree()),
           bg='#a0a6b8', fg='white').grid(row=0, column=3, padx=6)

    # Shoes Treeview
    shoes_frame = LabelFrame(left, text='Shoes', bg='#f5f7fa', font=('Segoe UI', 10, 'bold'))
    shoes_frame.pack(fill=BOTH, expand=True, padx=6, pady=(0, 12))

    columns = ('Name', 'Size', 'Price', 'Stock', 'Brand')
    shoes_tree = ttk.Treeview(shoes_frame, columns=columns, show='headings', height=8)
    for col in columns:
        shoes_tree.heading(col, text=col)
        shoes_tree.column(col, anchor=CENTER, width=90)
    shoes_tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(6, 0), pady=6)

    shoes_scroll = ttk.Scrollbar(shoes_frame, orient=VERTICAL, command=shoes_tree.yview)
    shoes_tree.configure(yscroll=shoes_scroll.set)
    shoes_scroll.pack(side=RIGHT, fill=Y, padx=(0,6), pady=6)

    # Shoes actions
    action_frame = Frame(left, bg='#f5f7fa')
    action_frame.pack(fill=X, padx=6, pady=(0, 12))

    def on_shoe_select(event=None):
        sel = shoes_tree.selection()
        if not sel:
            return
        item = shoes_tree.item(sel[0])['values']
        detail = f"Name: {item[0]}\nSize: {item[1]}\nPrice: {item[2]}\nStock: {item[3]}\nBrand: {item[4]}"
        messagebox.showinfo('Shoe Details', detail)

    Button(action_frame, text='View Selected', bg='#27ae60', fg='white', command=on_shoe_select).pack(side=LEFT, padx=6)
    Button(action_frame, text='Show Stock Summary', bg='#34495e', fg='white',
           command=lambda: messagebox.showinfo('Stock Summary', '\n'.join([f"{s['name']}: {s['stock']} pairs" for s in shoes]) or 'No stock data.')).pack(side=LEFT, padx=6)
    Button(action_frame, text='Refresh', bg='#f39c12', fg='white', command=lambda: populate_all()).pack(side=RIGHT, padx=6)

    # Right panel: image + sales
    right = Frame(body, bg='#f5f7fa', width=420)
    right.pack(side=RIGHT, fill=BOTH)

    # Image area
    img_frame = Frame(right, bg='#ffffff', relief=RIDGE, bd=1)
    img_frame.pack(fill=X, padx=6, pady=(6, 10))

    img_path = os.path.join('.', 'Images', 'main.jpeg')
    if os.path.exists(img_path):
        try:
            pil = Image.open(img_path).resize((380, 220), Image.LANCZOS)
            photo = ImageTk.PhotoImage(pil)
            win._images['main'] = photo
            Label(img_frame, image=photo, bg='white').pack(padx=6, pady=6)
        except Exception:
            Label(img_frame, text='Image failed to load', bg='white').pack(padx=6, pady=40)
    else:
        Label(img_frame, text='No Image Found', bg='white').pack(padx=6, pady=40)

    # Sales Treeview
    sales_frame = LabelFrame(right, text='Sales Reports', bg='#f5f7fa', font=('Segoe UI', 10, 'bold'))
    sales_frame.pack(fill=BOTH, expand=True, padx=6, pady=(0, 6))

    s_cols = ('Shoe', 'Customer', 'Quantity', 'Amount', 'Date')
    sales_tree = ttk.Treeview(sales_frame, columns=s_cols, show='headings', height=8)
    for col in s_cols:
        sales_tree.heading(col, text=col)
        sales_tree.column(col, anchor=CENTER, width=80)
    sales_tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(6, 0), pady=6)

    sales_scroll = ttk.Scrollbar(sales_frame, orient=VERTICAL, command=sales_tree.yview)
    sales_tree.configure(yscroll=sales_scroll.set)
    sales_scroll.pack(side=RIGHT, fill=Y, padx=(0,6), pady=6)

    def on_sale_select(event=None):
        sel = sales_tree.selection()
        if not sel:
            return
        item = sales_tree.item(sel[0])['values']
        detail = f"Shoe: {item[0]}\nCustomer: {item[1]}\nQuantity: {item[2]}\nAmount: {item[3]}\nDate: {item[4]}"
        messagebox.showinfo('Sale Details', detail)

    sales_tree.bind('<Double-1>', on_sale_select)

    # Styling Treeviews (basic)
    style = ttk.Style(win)
    style.theme_use('default')
    style.configure('Treeview', rowheight=22, font=('Segoe UI', 9))
    style.configure('Treeview.Heading', font=('Segoe UI', 10, 'bold'))

    # Populate functions
    def populate_shoes_tree(filter_text: str = ''):
        shoes_tree.delete(*shoes_tree.get_children())
        filtered = []
        if filter_text:
            ft = filter_text.strip().lower()
            filtered = [s for s in shoes if ft in s.get('name', '').lower() or ft in s.get('brand', '').lower()]
        else:
            filtered = shoes[:]

        if not filtered:
            shoes_tree.insert('', END, values=('No shoes found', '', '', '', ''))
            return

        for s in filtered:
            shoes_tree.insert('', END, values=(s.get('name', ''), s.get('size', ''), s.get('price', ''), s.get('stock', ''), s.get('brand', '')))

    def populate_sales_tree():
        sales_tree.delete(*sales_tree.get_children())
        if not sales:
            sales_tree.insert('', END, values=('No sales found', '', '', '', ''))
            return
        for sale in sales:
            sales_tree.insert('', END, values=(sale.get('shoe', ''), sale.get('customer', ''), sale.get('quantity', ''), sale.get('amount', ''), sale.get('date', '')))

    def populate_all():
        populate_shoes_tree(filter_text=search_var.get())
        populate_sales_tree()

    # initial population
    populate_all()

    # helpful hint
    hint = Label(win, text='Tip: Double-click a sale to view details. Select a shoe and click "View Selected".', bg='#f5f7fa', fg='#555', font=('Segoe UI', 9))
    hint.pack(side=BOTTOM, fill=X, pady=(0, 8))

# To use: call open_retrieve_window() from your menu
