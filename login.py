from tkinter import *
import time
from tkinter import messagebox
from Create import open_create_window
from Retrieve import open_retrieve_window
from Update import open_update_window
from Delete import open_delete_window

# Store users in memory for this session
users = {
    'admin': {'password': 'admin123', 'type': 'Admin'},
    'user': {'password': 'user123', 'type': 'Regular'}
}

def on_enter(event): 
    connect_button.config(bg="orange")
def on_leave(event): 
    connect_button.config(bg="#90EE90")

def clock():
    date = time.strftime('%d/%m/%Y') 
    currentTime = time.strftime('%H:%M:%S')
    dateTimeLabel.config(text = f'Date:{date}\nTime:{currentTime}')
    dateTimeLabel.after(1000,clock)

def slide_text():
    # Animate the heading label text using after()
    def animate(x=0):
        heading_label.place(x=x, y=300)
        next_x = x + 2
        if next_x > window.winfo_width():
            next_x = -heading_label.winfo_width()
        window.after(10, lambda: animate(next_x))
    animate()

# Registration window

def open_registration():
    def register():
        username = reg_usernameEntry.get()
        password = reg_passwordEntry.get()
        user_type = user_type_var.get()
        if username == '' or password == '':
            messagebox.showerror('Error','Fields cannot be empty',parent=regWindow)
        elif username in users:
            messagebox.showerror('Error','Username already exists',parent=regWindow)
        else:
            users[username] = {'password': password, 'type': user_type}
            messagebox.showinfo('Success',f'Registration successful as {user_type}',parent=regWindow)
            regWindow.destroy()

    regWindow = Toplevel()
    regWindow.geometry("400x250+600+350")
    regWindow.title("Register")
    regWindow.resizable(0,0)
    regWindow.configure(bg="lightblue")
    regWindow.grab_set()

    Label(regWindow, text='Username:', font=('Arial', 12), bg='lightblue').place(x=50, y=40)
    reg_usernameEntry = Entry(regWindow, font=('Arial', 12), bd=2)
    reg_usernameEntry.place(x=150, y=40)

    Label(regWindow, text='Password:', font=('Arial', 12), bg='lightblue').place(x=50, y=80)
    reg_passwordEntry = Entry(regWindow, font=('Arial', 12), bd=2, show='*')
    reg_passwordEntry.place(x=150, y=80)

    Label(regWindow, text='User Type:', font=('Arial', 12), bg='lightblue').place(x=50, y=120)
    user_type_var = StringVar(value='Regular')
    Radiobutton(regWindow, text='Admin', variable=user_type_var, value='Admin', bg='lightblue').place(x=150, y=120)
    Radiobutton(regWindow, text='Regular', variable=user_type_var, value='Regular', bg='lightblue').place(x=220, y=120)

    Button(regWindow, text='Register', command=register, font=('Arial', 12, 'bold'), bg='cornflowerblue', fg='white').place(x=150, y=170)

    regWindow.mainloop()

# Login window

def show_menu(user_type):
    menuWindow = Toplevel()
    menuWindow.geometry("500x400+600+300")
    menuWindow.title("Main Menu")
    menuWindow.resizable(0,0)
    menuWindow.configure(bg="#f1c727")
    menuWindow.grab_set()

    Label(menuWindow, text=f"Welcome, {user_type} User!", font=("Arial", 18, "bold"), bg="#f1c727").pack(pady=20)
    Label(menuWindow, text="Select an action:", font=("Arial", 14), bg="#f1c727").pack(pady=10)

    if user_type == 'Admin':
        Button(menuWindow, text="Create (Add New Data)", font=("Arial", 12), width=25, bg="#00FF00", command=open_create_window).pack(pady=5)
        Button(menuWindow, text="Retrieve (View/Search Data)", font=("Arial", 12), width=25, bg="#DA70D6", command=open_retrieve_window).pack(pady=5)
        Button(menuWindow, text="Update (Change Existing Data)", font=("Arial", 12), width=25, bg="#A020F0", command=open_update_window).pack(pady=5)
        Button(menuWindow, text="Delete (Remove Data)", font=("Arial", 12), width=25, bg="red", command=open_delete_window).pack(pady=5)
    else:
        Button(menuWindow, text="Create (Add New Data)", font=("Arial", 12), width=25, bg="#00FF00", command=open_create_window).pack(pady=5)
        Button(menuWindow, text="Retrieve (View/Search Data)", font=("Arial", 12), width=25, bg="#DA70D6", command=open_retrieve_window).pack(pady=5)
    # You can connect these buttons to your actual functions/modules as needed

def connect_to_database():
    def login():
        username = usernameEntry.get()
        password = passwordEntry.get()
        if username == '' or password == '' or hostnameEntry.get() == '':
            messagebox.showerror('Error','Fields cannot be empty',parent=loginWindow)
        elif username not in users or users[username]['password'] != password:
            messagebox.showerror('Error','Invalid credentials',parent=loginWindow)
        else:
            user_type = users[username]['type']
            if user_type == 'Admin':
                messagebox.showinfo('Success','Welcome Admin! You have higher access.',parent=loginWindow)
            else:
                messagebox.showinfo('Success','Welcome Regular User! Limited access.',parent=loginWindow)
            loginWindow.destroy()
            show_menu(user_type)

    loginWindow = Toplevel()
    loginWindow.geometry("500x320+520+300")
    loginWindow.title("Login Credentials")
    loginWindow.resizable(0,0)
    loginWindow.configure(bg="pink")
    loginWindow.grab_set()
    
    hostnameImage = PhotoImage(file='./Images/hostname.png')
    hostnameLabel = Label(loginWindow,image=hostnameImage,text = 'Host Name',font=('arial',16,'bold'),compound=LEFT,bg="pink")
    hostnameLabel.place(x=70, y=50)
    hostnameEntry = Entry(loginWindow,font=('times new roman',13,'bold'),fg="royalblue",bd=3)
    hostnameEntry.place(x=240, y=57)

    usernameImage = PhotoImage(file='./Images/username.png')
    usernameLabel = Label(loginWindow,image=usernameImage,text='User Name',font=('arial',16,'bold'),compound=LEFT,bg="pink")
    usernameLabel.place(x=70, y=95)
    usernameEntry = Entry(loginWindow,font=('times new roman',13,'bold'),fg="royalblue",bd=3)
    usernameEntry.place(x=240, y=102)

    passwordImage = PhotoImage(file='./Images/password.png')
    passwordLabel = Label(loginWindow,image=passwordImage,text='Password',font=('arial',16,'bold'),compound=LEFT,bg="pink")
    passwordLabel.place(x=70, y=145)
    passwordEntry = Entry(loginWindow,font=('times new roman',13,'bold'),fg="royalblue",bd=3, show='*')
    passwordEntry.place(x=240, y=152)

    loginButton = Button(loginWindow,command=login,text="Login",font=("Arial", 12, "bold"),width=10,bg = "cornflowerblue",
                        fg="white",activebackground="cornflowerblue",cursor="hand2")
    loginButton.place(x=190,y=200)

    registerButton = Button(loginWindow,command=open_registration,text="Register",font=("Arial", 12, "bold"),width=10,bg = "#90EE90",
                        fg="black",activebackground="#90EE90",cursor="hand2")
    registerButton.place(x=300,y=200)

    loginWindow.mainloop()

#GUI part

window = Tk()
window.title("Database Connection")
window.geometry("1520x780+2+2")
window.grab_set()

# Create a Canvas widget
canvas = Canvas(window, width=1530, height=790)

# Load the background image
background_image = PhotoImage(file="./Images/db.png")

# Create a background image on the canvas
canvas.create_image(0, 0, anchor=NW, image=background_image)
canvas.place(x=-10,y=-10)
canvas.pack()

dateTimeLabel = Label(window,font = ('timew new roman',18,'bold'),bg="#0f133f",fg="white")
dateTimeLabel.place(x=35,y=35)
clock()

# Create a label for the heading
heading_label = Label(window, text="Welcome to GoShoe Management System", 
                      font=("Arial", 24, "bold"),bg="#132049",fg="white")
heading_label.place(x=450,y=330)

# Create a button to connect to the database
connect_button = Button(window, text="Connect To Database", 
                        command=connect_to_database,
                        width=18,
                        height=1,
                        font=("Arial", 18, "bold"),
                        bg = "#90EE90",
                        cursor="hand2"
                        )   
connect_button.place(x=360,y=400)

connect_button.bind("<Enter>", on_enter)
connect_button.bind("<Leave>", on_leave)

slide_text()


window.mainloop()


