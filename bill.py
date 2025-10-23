from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox


def connect_to_bill():
    # functions part
    def slide_text(label, text):
        label.config(text="")
        # Add one character at a time with a delay
        for char in text:
            label.config(text=label.cget("text") + char)
            label.update()
            time.sleep(0.1)
    
    def operations(title,text,command):
        global bidEntry,cidEntry,pidEntry,qtyEntry,amtEntry,purchaseEntry,window
        window = Toplevel()
        window.geometry("450x450+550+150")
        window.title(title)
        window.config(bg="pink") 
        window.resizable(0,0)
        window.grab_set()

        bidLabel = Label(window,text = 'Bill ID',font=('arial',16,'bold'),compound=LEFT,bg="pink")
        bidLabel.place(x=20, y=30)
        bidEntry = Entry(window,font=('times new roman',13,'bold'),fg="black",bd=3)
        bidEntry.place(x=220, y=32)

        cidLabel = Label(window,text = 'Customer ID',font=('arial',16,'bold'),compound=LEFT,bg="pink")
        cidLabel.place(x=20, y=90)
        cidEntry = Entry(window,font=('times new roman',13,'bold'),fg="black",bd=3)
        cidEntry.place(x=220, y=92)

        pidLabel = Label(window,text = 'Product ID',font=('arial',16,'bold'),compound=LEFT,bg="pink")
        pidLabel.place(x=20, y=150)
        pidEntry = Entry(window,font=('times new roman',13,'bold'),fg="black",bd=3)
        pidEntry.place(x=220, y=152)

        qtyLabel = Label(window,text = 'Quantity',font=('arial',16,'bold'),compound=LEFT,bg="pink")
        qtyLabel.place(x=20, y=210)
        qtyEntry = Entry(window,font=('times new roman',13,'bold'),fg="black",bd=3)
        qtyEntry.place(x=220, y=212)

        amtLabel = Label(window,text = 'Amount',font=('arial',16,'bold'),compound=LEFT,bg="pink")
        amtLabel.place(x=20, y=270)
        amtEntry = Entry(window,font=('times new roman',13,'bold'),fg="black",bd=3)
        amtEntry.place(x=220, y=272)

        purchaseLabel = Label(window,text = 'Purchase Date',font=('arial',16,'bold'),compound=LEFT,bg="pink")
        purchaseLabel.place(x=20, y=330)
        purchaseEntry = Entry(window,font=('times new roman',13,'bold'),fg="black",bd=3)
        purchaseEntry.place(x=220, y=332)

        searchButton = Button(window,command=command,text=text,width=15,font=('times new roman',14,'bold'),bg = "#3EB489",cursor="hand2")
        searchButton.place(x = 140, y = 390)

        if title == 'Update Operation':
            indexing = BillTable.focus()
            content = BillTable.item(indexing)
            bidEntry.insert(content['values'][0])
            cidEntry.insert(0,content['values'][1])
            pidEntry.insert(0,content['values'][2])
            qtyEntry.insert(1,content['values'][3])
            amtEntry.insert(2,content['values'][4])
            purchaseEntry.insert(3,content['values'][5])

    def update_data():
        indexing = BillTable.focus()
        content = BillTable.item(indexing)
        bill_id = content['values'][0]
        for bill in bills:
            if bill['bid'] == bill_id:
                bill['cid'] = cidEntry.get()
                bill['pid'] = pidEntry.get()
                bill['qty'] = qtyEntry.get()
                bill['amt'] = amtEntry.get()
                bill['purchase'] = purchaseEntry.get()
                break
        messagebox.showinfo('Success',f'Bill Id {bill_id} is modified Successfully',parent=window)
        window.destroy()
        view()

    def delete():
        def delete_data():
            indexing = BillTable.focus()
            content = BillTable.item(indexing)
            content_id = content['values'][0]
            global bills
            bills = [bill for bill in bills if bill['bid'] != content_id]
            messagebox.showinfo('Deleted',f'{content_id} Bill ID row is Deleted Successfully',parent=window)
            window.destroy()
            view()

        window = Toplevel()
        window.geometry("450x200+540+280")
        window.title("Delete Operation")
        window.config(bg="pink") 
        window.resizable(0,0)
        window.grab_set()

        display = Label(window,text='Did you select the row of bill table ?\n  If not, Please select the row of table',font=('arial',15,'bold'),bg='pink')
        display.place(x=20, y=30)

        yesButton = Button(window,command=delete_data,text='YES',font=('arial',12,'bold'),width=6,bg='yellow',cursor="hand2")
        yesButton.place(x=190,y=100)

    def search_data():
        BillTable.delete(*BillTable.get_children())
        for bill in bills:
            if (bidEntry.get() and bill['bid'] == bidEntry.get()) or \
               (cidEntry.get() and bill['cid'] == cidEntry.get()) or \
               (pidEntry.get() and bill['pid'] == pidEntry.get()) or \
               (qtyEntry.get() and bill['qty'] == qtyEntry.get()) or \
               (amtEntry.get() and bill['amt'] == amtEntry.get()) or \
               (purchaseEntry.get() and bill['purchase'] == purchaseEntry.get()):
                BillTable.insert('',END,values=(bill['bid'], bill['cid'], bill['pid'], bill['qty'], bill['amt'], bill['purchase']))
        window.destroy()

    def view():
        BillTable.delete(*BillTable.get_children())
        for bill in bills:
            BillTable.insert('',END,values=(bill['bid'], bill['cid'], bill['pid'], bill['qty'], bill['amt'], bill['purchase']))

    def add_data():
        if cidEntry.get()=='' or qtyEntry.get()=='' or purchaseEntry.get()=='' or amtEntry.get()=='' or bidEntry.get()=='' or pidEntry.get()=='':
            messagebox.showerror('Error',"All Fields are required",parent=window)
        else:
            for bill in bills:
                if bill['bid'] == bidEntry.get():
                    messagebox.showerror('Error','Bill ID cannot be repeated',parent=window)
                    return
            bills.append({
                'bid': bidEntry.get(),
                'cid': cidEntry.get(),
                'pid': pidEntry.get(),
                'qty': qtyEntry.get(),
                'amt': amtEntry.get(),
                'purchase': purchaseEntry.get()
            })
            result = messagebox.showinfo('Confirm','Data added successfully',parent=window)
            if result:
                bidEntry.delete(0,END)
                cidEntry.delete(0,END)
                pidEntry.delete(0,END)
                qtyEntry.delete(0,END)
                amtEntry.delete(0,END)
                purchaseEntry.delete(0,END)
            window.destroy()
            view()

    # In-memory bill data
    global bills
    if 'bills' not in globals():
        bills = []

    # GUI part
    root = Toplevel()
    style = ttk.Style(root)
    style.theme_use("default")
    root.geometry("1400x750+65+15")
    root.title("Bill Table")
    root.config(bg='whitesmoke')
    root.resizable(0,0)

    heading_label = Label(root,font=("Arial", 30,"bold"), pady=15,bg="whitesmoke")
    heading_label.pack()

    middleFrame = Frame(root, bg = "white",highlightbackground='black',highlightthickness=1)
    middleFrame.place(x = 50,y = 100, width = 1300, height = 520)

    BillTable = ttk.Treeview(middleFrame,columns=('bill_id','cid','pid','qty','amt','purchase_date'))
    BillTable.pack(fill=BOTH,expand=1)

    BillTable.heading('bill_id',text = 'Bill ID')
    BillTable.column('bill_id',anchor=CENTER)
    BillTable.heading('cid',text = 'Customer ID')
    BillTable.column('cid',anchor=CENTER)
    BillTable.heading('pid',text = 'Product ID')
    BillTable.column('pid',anchor=CENTER)
    BillTable.heading('qty',text = 'Quantity')
    BillTable.column('qty',anchor=CENTER)
    BillTable.heading('amt',text = 'Amount')
    BillTable.column('amt',anchor=CENTER)
    BillTable.heading('purchase_date',text = 'Purchase Date')
    BillTable.column('purchase_date',anchor=CENTER)

    BillTable.config(show='headings')
    view()
    addButton = Button(root,command=lambda: operations('Add Operation','ADD DATA',add_data),text='Insert',width=10,font=('times new roman',16,"bold"),bg='#00FF00',cursor="hand2")
    addButton.place(x=150,y=650)

    searchButton = Button(root,command=lambda: operations('Serach Operation','SEARCH DATA',search_data),text='Search',width=10,font=('times new roman',16,"bold"),bg='#DA70D6',cursor="hand2")
    searchButton.place(x=400,y=650)

    viewButton = Button(root,command=view,text='View Data',width=10,font=('times new roman',16,"bold"),bg='yellow',cursor="hand2")
    viewButton.place(x=650,y=650)

    deleteButton = Button(root,command=delete,text='Delete',width=10,font=('times new roman',16,"bold"),bg='red',cursor="hand2")
    deleteButton.place(x=900,y=650)

    updateButton = Button(root,command=lambda: operations('Update Operation','UPDATE DATA',update_data),text='Update',width=10,font=('times new roman',16,"bold"),bg='#A020F0',cursor="hand2")
    updateButton.place(x=1150,y=650)

    style = ttk.Style()
    style.configure('Treeview',rowheight=25,font=('arial',12,'normal'))
    style.configure("Treeview.Heading",font=('times new roman',16,"bold"),background='#FD7F20',padding=(30,10))
    
    slide_text(heading_label,'Bill Table')
    root.mainloop()