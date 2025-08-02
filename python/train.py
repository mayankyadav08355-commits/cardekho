from tkinter import *
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

'''def search_trains():
    source = source_entry.get().strip().capitalize()
    destination = destination_entry.get().strip().capitalize()

    if not source or not destination:
        messagebox.showerror("error","please enter both source and destination stations.")
        return
    
    conn, cursor = db_connect()
    if not conn:
        return
    
    try:
        cursor.execute("SELECT Tname, departuretime, Arrival, duration, status, source, destination FROM t  WHERE source  = %s AND destination = %s,(source,destination)") 
        results = cursor.fetchall()

    except sql.Error as e:
        messagebox.showerror("database error",f"error querying the database:\n{e}")
        results = [] 
    finally:
        conn.close()

    for item in train_table.get_children(): 
        train_table.delete(item)   

    if results:
        for train in results:
            train_table.insert("","end", values=train)
    else:
        messagebox.showinfo("no train found", f"no train found from {source} to {destination}.")

def show_selected_train():
    selected_item = train_table.selection()
    if not selected_item:
        messagebox.showerror("error","please select a train from the list.")
        return

    train = train_table.item(selected_item[0],"values")
    details =(
            f"Tname:{train[0]}\n"
            f"departuretime:{train[1]}\n"
            f"Arrival:{train[2]}\n"
            f"duration:{train[3]}\n"
            f"status:{train[4]}\n"
            f"source:{train[5]}\n"
            f"destination:{train[6]}"
        )  
    messagebox.showinfo("selected train",details)
def book_selected_train():
    selected_item = train_table.selection()
    if not selected_item:
        messagebox.showerror("error","please select a train to book.")
        return
         
    train=train_table.item(selected_item[0],"values")
    confirmation = messagebox.askyesno(
            "confirm booking",
            f"do you want to book the following train?\n\n"
            f"Tname:{train[0]}\n"
            f"departuretime:{train[1]}\n"
            f"Arrival:{train[2]}\n"
            f"duration:{train[3]}\n"
            f"status:{train[4]}\n"
            f"source:{train[5]}\n"
            f"destination:{train[6]}"
        )
    if confirmation:
        messagebox.showinfo("booking confirmed",f"you have succesfully booked the train:\n\n{train[0]}({train[1]})")

root = tk.Tk()
root.title("train search")
root.geometry("900x600")

style=ttk.Style()
style.theme_use("default")
style.configure(
    "treeview",
    fieldbackground="lightblue",
    foreground="black",
    rowheight=50
    )
style.configure(  
    "Treeview.heading",
    background="darkblue",
    forground="white",
    font=("Arial",12,"bold")
)
    

search_frame = tk.Frame(win)
search_frame.pack(pady=10)

tk.Label(search_frame,text="source:").grid(row=0,column=0,padx=5)
source_entry=tk.Entry(search_frame)
source_entry.grid(row=0,column=1,padx=5)

tk.Label(search_frame,text="destination:").grid(row=0,column=2, padx=5)
destination_entry = tk.Entry(search_frame)
destination_entry.grid(row=0, column=4,padx=5)
     
search_button = tk.Button(search_frame,text="search train", command=search_trains)
search_button.grid(row=0,column=4, padx=10)
    
columns=("tname"," departuretime", "Arrival", "duration", "status", "source", "destination")
train_table= ttk.Treeview(root, columns=columns, show="headings", height=10)
train_table.pack(padx=20, pady=10,fill="both",expand=True)


for col in columns:
    train_table.heading(col,text=col)
    train_table.column(col,anchor="center",width=200)

detail_button=tk.Button(root,text="show selected train details",command=show_selected_train)
detail_button.pack(pady=10)


book_button =tk.Button(root, text="book train", command=book_selected_train)
book_button.pack(pady=10)

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img21.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

tk.Label(search_frame,text="source:").grid(row=0,column=0,padx=5)
source_entry=tk.Entry(search_frame)
source_entry.grid(row=0,column=1,padx=5)


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
source_entry=Entry(win,width=25,font=("bold",21),fg="#000000",bg="white")
source_entry=tk.Entry(search_frame)
source_entry.place(x=900,y=840)

lab=Label(win,text="Destination station",width=14,fg="#FFFEFE", font=("bold",30),bg="#3282F6")
lab.place(x=1440,y=780)
destination_entry=Entry(win,width=25,font=("bold",21),fg="#000000",bg="white")
destination_entry_entry=tk.Entry(search_frame)
destination_entry.place(x=1440,y=840)

btn=Button(win,text="Search Train",width=35,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=search_trains)
btn.place(x=1155,y=900)

columns=("tname"," departuretime", "Arrival", "duration", "status", "source", "destination")
train_table= ttk.Treeview(root, columns=columns, show="headings", height=10)
train_table.pack(padx=20, pady=10,fill="both",expand=True)


for col in columns:
    train_table.heading(col,text=col)
    train_table.column(col,anchor="center",width=200)

detail_button=tk.Button(root,text="show selected train details",command=show_selected_train)
detail_button.pack(pady=10)


book_button =tk.Button(root, text="book train", command=book_selected_train)
book_button.pack(pady=10)


trv=ttk.Treeview(win,columns=(1,2,3,4,5,6,7,8),height=2,show="headings")
trv.column(1,anchor=CENTER,stretch=NO,width=240)  
trv.column(2,anchor=CENTER,stretch=NO,width=240)
trv.column(3,anchor=CENTER,stretch=NO,width=240)  
trv.column(4,anchor=CENTER,stretch=NO,width=240)
trv.column(5,anchor=CENTER,stretch=NO,width=240)  
trv.column(6,anchor=CENTER,stretch=NO,width=240)
trv.column(7,anchor=CENTER,stretch=NO,width=240)  
trv.column(8,anchor=CENTER,stretch=NO,width=240)

trv.heading(1,text="Train Name")
trv.heading(2,text="Departure Time")
trv.heading(3,text="Arrival Time")
trv.heading(4,text="Duration")
trv.heading(5,text="Status")
trv.heading(6,text="Source")
trv.heading(7,text="Destination")
trv.heading(8,text="Book ticket")

trv.place(x=0,y=80)


win.mainloop()

    


if a=="":
    messagebox.showerror("empty","Please fill the Train details")
    messagebox.showinfo("Success","Search Successfully")
    win.pack_propagate()'''
   

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

btn=Button(win,text="Search Train",width=35,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E")
btn.place(x=1155,y=900)


trv=ttk.Treeview(win,columns=(1,2,3,4,5,6,7,8),height=2,show="headings")
trv.column(1,anchor=CENTER,stretch=NO,width=240)  
trv.column(2,anchor=CENTER,stretch=NO,width=240)
trv.column(3,anchor=CENTER,stretch=NO,width=240)  
trv.column(4,anchor=CENTER,stretch=NO,width=240)
trv.column(5,anchor=CENTER,stretch=NO,width=240)  
trv.column(6,anchor=CENTER,stretch=NO,width=240)
trv.column(7,anchor=CENTER,stretch=NO,width=240)  
trv.column(8,anchor=CENTER,stretch=NO,width=240)

trv.heading(1,text="Train Name")
trv.heading(2,text="Departure Time")
trv.heading(3,text="Arrival Time")
trv.heading(4,text="Duration")
trv.heading(5,text="Status")
trv.heading(6,text="Source")
trv.heading(7,text="Destination")
trv.heading(8,text="Book ticket")

trv.place(x=0,y=80)


win.mainloop()