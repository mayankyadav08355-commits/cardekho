'''from tkinter import *
from tkinter import ttk,messagebox,Frame,Button
import tkinter as tk
import os
from PIL import Image,ImageTk
from functools import reduce
import pymysql as sql

win=Tk()


win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='railway')
    cur=conn.cursor()
    return conn,cur

def search_train():
    source = ent1.get()
    destination = ent2.get()
    
    if not source or not destination:
        messagebox.showerror("Input Error", "Please enter both source and destination stations.")
        return
    #print(f"Query: SELECT * FROM trains WHERE source = '{source}' AND destination = '{destination}'")
    # Connect to the database and execute a query to find trains
    conn, cur = db_connect()
    query = f"SELECT * FROM t WHERE source = 'kota' AND destination = 'jaipur'"
    cur.execute(query)
    results = cur.fetchall()
    
    # Clear previous treeview entries
    for row in trv.get_children():
        trv.delete(row)

    if not results:
        messagebox.showinfo("No Results", "No trains found for the given source and destination.")
    else:
        # Add the train details to the Treeview
        for row in results:
            trv.insert("", "end", values=row)
    
    # Close the database connection
    conn.close()

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img21.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=50,height=1,fg="#FFFEFE", font=("bold",50),bg="#3282F6")
lab.place(x=0,y=0)

lab=Label(win,text="Train Details",width=40,fg="#FFFEFE", font=("bold",30),bg="#3282F6")
lab.place(x=510,y=10)

lab=Label(win,text="",width=25,height=4,fg="#FFFEFE", font=("bold",50),bg="#3282F6")
lab.place(x=930,y=700)

lab=Label(win,text="Search Train",width=10,fg="#FFFEFE", font=("bold",30),bg="#3282F6")
lab.place(x=1300,y=720)

lab=Label(win,text="Source Station",width=11,fg="#FFFEFE", font=("bold",30),bg="#3282F6")
lab.place(x=990,y=780)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="white")
ent1.place(x=990,y=840)

lab=Label(win,text="Destination station",width=14,fg="#FFFEFE", font=("bold",30),bg="#3282F6")
lab.place(x=1440,y=780)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="white")
ent2.place(x=1440,y=840)

btn=Button(win,text="Search Train",width=35,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=search_train)
btn.place(x=1155,y=900)


trv=ttk.Treeview(win,columns=(1,2,3,4,5,6,7),height=2,show="headings")
trv.column(1,anchor=CENTER,stretch=NO,width=240)  
trv.column(2,anchor=CENTER,stretch=NO,width=240)
trv.column(3,anchor=CENTER,stretch=NO,width=240)  
trv.column(4,anchor=CENTER,stretch=NO,width=240)
trv.column(5,anchor=CENTER,stretch=NO,width=240)  
trv.column(6,anchor=CENTER,stretch=NO,width=240)
trv.column(7,anchor=CENTER,stretch=NO,width=240)  


trv.heading(1,text="Train Name")
trv.heading(2,text="Departure Time")
trv.heading(3,text="Arrival Time")
trv.heading(4,text="Duration")
trv.heading(5,text="Status")
trv.heading(6,text="Source")
trv.heading(7,text="Destination")


trv.place(x=0,y=80)


win.mainloop()'''

from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import pymysql as sql
import os

win = Tk()

win.minsize(width="1920", height="1080")
win.maxsize(width="1920", height="1080")

def db_connect():
    conn = sql.connect(host='localhost', user='root', password='', port=3306, database='rail_way')
    cur = conn.cursor()
    return conn, cur

def search_train():
    source = ent1.get()
    destination = ent2.get()

    if not source or not destination:
        messagebox.showerror("Input Error", "Please enter both source and destination stations.")
        return

    try:
        conn, cur = db_connect()
        query = "SELECT * FROM tdetail WHERE source = %s AND destination = %s"
        cur.execute(query, (source, destination))
        results = cur.fetchall()

        for row in trv.get_children():
            trv.delete(row)

        if not results:
            messagebox.showinfo("No Results", "No trains found for the given source and destination.")
        else:
            for row in results:
                trv.insert("", "end", values=row)

        conn.close()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def book_ticket():
    selected_item = trv.focus()
    if not selected_item:
        messagebox.showerror("Selection Error", "Please select a train first.")
        return

    train_details = trv.item(selected_item)['values']
    train_name = train_details[0]
    source = train_details[5]
    destination = train_details[6]

    # Inserting the booking information into the database
    try:
        conn, cur = db_connect()
        query = "INSERT INTO pptrain (train_name, source, destination) VALUES (%s, %s, %s)"
        cur.execute(query, (train_name, source, destination))
        conn.commit()
        messagebox.showinfo("Booking Successful", f"Train '{train_name}' from {source} to {destination} has been booked successfully.")
        conn.close()
        os.system("python  booking.py") 

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while booking the train: {e}")

# Interface setup
image = Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img21.jpg")
image = image.resize((1920, 1080))
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win, image=tk_image)
image_label.pack()

lab = Label(win, text="", width=50, height=1, fg="#FFFEFE", font=("bold", 50), bg="#3282F6")
lab.place(x=0, y=0)

lab = Label(win, text="Train Details", width=40, fg="#FFFEFE", font=("bold", 30), bg="#3282F6")
lab.place(x=510, y=10)

lab = Label(win, text="", width=25, height=4, fg="#FFFEFE", font=("bold", 50), bg="#3282F6")
lab.place(x=930, y=700)

lab = Label(win, text="Search Train", width=10, fg="#FFFEFE", font=("bold", 30), bg="#3282F6")
lab.place(x=1300, y=720)

lab = Label(win, text="Source Station", width=11, fg="#FFFEFE", font=("bold", 30), bg="#3282F6")
lab.place(x=990, y=780)

ent1 = Entry(win, width=25, font=("bold", 21), fg="#000000", bg="white")
ent1.place(x=990, y=840)

lab = Label(win, text="Destination station", width=14, fg="#FFFEFE", font=("bold", 30), bg="#3282F6")
lab.place(x=1440, y=780)

ent2 = Entry(win, width=25, font=("bold", 21), fg="#000000", bg="white")
ent2.place(x=1440, y=840)

btn_search = Button(win, text="Search Train", width=25, height=1, fg="#000000", font=("bold", 20), bg="#A1FB8E", command=search_train)
btn_search.place(x=990, y=900)

btn_book = Button(win, text="Book Train", width=25, height=1, fg="#000000", font=("bold", 20), bg="#A1FB8E", command=book_ticket)
btn_book.place(x=1440, y=900)

# Treeview setup
trv = ttk.Treeview(win, columns=(1, 2, 3, 4, 5, 6, 7), height=10, show="headings")
trv.column(1, anchor=CENTER, stretch=NO, width=273)
trv.column(2, anchor=CENTER, stretch=NO, width=273)
trv.column(3, anchor=CENTER, stretch=NO, width=273)
trv.column(4, anchor=CENTER, stretch=NO, width=273)
trv.column(5, anchor=CENTER, stretch=NO, width=273)
trv.column(6, anchor=CENTER, stretch=NO, width=273)
trv.column(7, anchor=CENTER, stretch=NO, width=273)

trv.heading(1, text="Train Name")
trv.heading(2, text="Departure Time")
trv.heading(3, text="Arrival Time")
trv.heading(4, text="Duration")
trv.heading(5, text="Status")
trv.heading(6, text="Source")
trv.heading(7, text="Destination")

trv.place(x=0, y=80)

win.mainloop()
