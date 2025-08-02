from tkinter import *
from tkinter import ttk, messagebox
import pymysql as sql
from PIL import Image, ImageTk


# ---------- DATABASE CONNECTION FUNCTION ----------

def db_connect():
    conn = sql.connect(host='localhost', user='root', password='', port=3306, database='rail_way')
    cur = conn.cursor()
    return conn, cur


# ---------- SEARCH FUNCTION ----------
def search_booking():
    aadhar = ent1.get().strip()
    email = ent2.get().strip()

    if not aadhar or not email:
        messagebox.showerror("Input Error", "Please fill both Aadhar card no. and Email")
        return

    conn = None  # Make sure it's defined for finally block
    try:
        conn, cur = db_connect()

        query = """
            SELECT pt.train_name, 
                pb.Fname, pt.source, pt.destination,
                pb.aadharno, pb.Email,  pb.Date
            FROM   pbookings pb
            JOIN   pptrain pt
                ON pt.source = pb.`from` AND pt.destination = pb.`to`
            WHERE  pb.aadharno = %s AND pb.Email = %s
        """

        
        cur.execute(query, (aadhar, email))
        rows = cur.fetchall()

    except sql.Error as e:
        messagebox.showerror("Database Error", str(e))
        return
    finally:
        if conn:
            conn.close()

    # Clear Treeview and insert new results
    tree.delete(*tree.get_children())
    if rows:
        for row in rows:
            tree.insert("", "end", values=row)
            break
    else:
        messagebox.showinfo("Not Found", "No matching records found.")

# ---------- GUI SETUP ----------
win = Tk()
win.title("Train Booking Search")
win.config(bg="skyblue")
win.minsize(width=1920, height=1080)
win.maxsize(width=1920, height=1080)

# ---------- BACKGROUND IMAGE ----------
bg_image_path = "C:\\Users\\Mayank\\Desktop\\railway ticket system\\img12.jpg"
image = Image.open(bg_image_path).resize((1920, 1080))
tk_image = ImageTk.PhotoImage(image)
image_label = Label(win, image=tk_image)
image_label.place(x=0, y=0)


lab=Label(win,text="",width=17,height=7,fg="#FFFEFE", font=("bold",50),bg="#EFEFEF")
lab.place(x=600,y=0)
# ---------- TITLE ----------
Label(win, text="Your Booking", fg="#000000", font=("bold", 30), bg="#EFEFEF").place(x=800, y=30)

# ---------- AADHAR INPUT ----------
Label(win, text="Aadhar card no.:", fg="#000000", font=("bold", 20), bg="#EFEFEF").place(x=650, y=100)
ent1 = Entry(win, width=35, font=("bold", 21))
ent1.place(x=650, y=150)

# ---------- EMAIL INPUT ----------
Label(win, text="Email:", fg="#000000", font=("bold", 20), bg="#EFEFEF").place(x=650, y=250)
ent2 = Entry(win, width=35, font=("bold", 21))
ent2.place(x=650, y=300)

# ---------- SEARCH BUTTON ----------
btn = Button(win, text="Search", width=35, height=1, fg="white", font=("bold", 20), bg="#0023F5", command=search_booking)
btn.place(x=650, y=400)

# ---------- TREEVIEW STYLE ----------
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", fieldbackground="#FFFFFF", foreground="black", rowheight=50)
style.configure("Treeview.Heading", background="#FFFFFF", foreground="black", font=("Arial", 13, "bold"), padding=(3, 7))

# ---------- TREEVIEW WIDGET ----------
columns = ("1", "2", "3", "4", "5", "6", "7")
headings = [
    ("1", "Train Name"),
    ("2", "Passenger Name"),
    ("3", "Source"),
    ("4", "Destination"),
    ("5", "Aadhar Card No."),
    ("6", "Email"),
    ("7", "date"),
    
]


tree = ttk.Treeview(win, columns=columns, show="headings", height=8)
tree.place(x=0, y=580)

for col, text in headings:
    tree.heading(col, text=text)
    tree.column(col, width=280, anchor="center")

win.mainloop()
