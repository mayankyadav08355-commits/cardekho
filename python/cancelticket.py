from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
from functools import reduce
import pymysql as sql

win=Tk()
win.config(bg="skyblue")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")


def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='rail_way')
    cur=conn.cursor()
    return conn,cur



def reference():
    aadharno=ent1.get()
    Fname=ent2.get()
    cmd=f"delete from pbookings where aadharno='{aadharno}' and FName='{Fname}'"
    conn,cur=db_connect()
    data=cur.execute(cmd)
    conn.commit()
    if aadharno=="":
        messagebox.showwarning("","enter details")
    elif data:
        messagebox.showinfo("","data successfully deleted")
    else:
        messagebox.showwarning("","not registerd account")

def afterlog():
    aadharno=ent1.get()
    Fname=ent2.get()
    if aadharno=="" or Fname=="":
        messagebox.showwarning("","please fill all field ")
    else:
        win.destroy()
        os.system("python Home.py") 


image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img2.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=17,height=7,fg="#FFFEFE", font=("bold",50),bg="#000961")
lab.place(x=600,y=0)

lab=Label(win,text="Cancel Train Ticket",width=15,fg="#FFFEFE", font=("bold",30),bg="#000961")
lab.place(x=750,y=30)


lab=Label(win,text="Aadhar card no.:",width=13,fg="#FFFEFE",font=("bold",20) ,bg="#000961")
lab.place(x=650,y=100)
ent1=Entry(win,width=35,font=("bold",21),fg="#000000")
ent1.place(x=650,y=150)


lab=Label(win,text="Passenger Name:",width=13,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=650,y=250)
ent2=Entry(win,width=35,font=("bold",21),fg="#000000")
ent2.place(x=650,y=300)


btn=Button(win,text="Cancel Ticket",width=35,height=1,fg="black",font=("bold",20),bg="#62DE3C" , command=reference)
btn.place(x=650,y=400)


win.mainloop()