from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
from functools import reduce
import pymysql as sql
 

win=Tk()
win.config(bg="#FFFFFF")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='rail_way')
    cur=conn.cursor()
    return conn,cur

def payment():
    Fname=ent1.get()
    Lname=ent2.get()
    country=ent3.get()
    subject=ent4.get()
    

    cmd=f"insert into feedback values('{Fname}','{Lname}','{country}','{subject}')"
    conn,cur=db_connect()
    cur.execute(cmd)
    conn.commit()
    print(cmd)
    win.destroy()
    os.system("python payment.py")




def fun():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    d=ent4.get()
    if a=="" or b=="" or c==" " or d==" ":
        messagebox.showerror("empty","Please fill the Details")
    messagebox.showinfo("Success","Thank you for feedback")
    win.pack_propagate()
    


lab=Label(win,text="",width=17,height=9,fg="#FFFEFE", font=("bold",50),bg="#000961")
lab.place(x=600,y=0)

lab=Label(win,text="Send Feedback",width=15,fg="#FFFEFE", font=("bold",30),bg="#000961")
lab.place(x=750,y=30)


lab=Label(win,text="First Name:",width=9,fg="#FFFEFE",font=("bold",20) ,bg="#000961")
lab.place(x=650,y=100)
ent1=Entry(win,width=35,font=("bold",21),fg="#000000")
ent1.place(x=650,y=150)


lab=Label(win,text="Last Name:",width=9,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=650,y=200)
ent2=Entry(win,width=35,font=("bold",21),fg="#000000")
ent2.place(x=650,y=250)


lab=Label(win,text="Country:",width=6,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=650,y=300)
ent3=Entry(win,width=35,font=("bold",21),fg="#000000")
ent3.place(x=650,y=350)


lab=Label(win,text="Subject:",width=6,fg="#FFFEFE",font=("bold",20),bg="#000961")
lab.place(x=650,y=400)
ent4=Entry(win,width=14,font=("corbel light",58),fg="black")
ent4.place(x=650,y=450)


btn=Button(win,text="Submit",width=35,height=1,fg="black",font=("bold",20),bg="#62DE3C",command=payment)
btn.place(x=650,y=600)

lab=Label(win,text="",width=50,height=4,fg="#FFFEFE", font=("bold",50),bg="black")
lab.place(x=0,y=730)

lab=Label(win,text="Contact Us",width=9,fg="#FFFFFF", font=("bold",30),bg="#000000")
lab.place(x=180,y=750)
lab=Label(win,text="Useful Links",width=10,fg="#FFFFFF", font=("bold",30),bg="#000000")
lab.place(x=780,y=750)
lab=Label(win,text="Payment Options",width=13,fg="#FFFFFF", font=("bold",30),bg="#000000")
lab.place(x=1280,y=750)

lab=Label(win,text="Email:Railwayenquiries19gmail.com",width=28,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=820)
lab=Label(win,text="Phone: +91 697584955",width=19,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=850)
lab=Label(win,text="Address: Mhaveer nagar vistar yojna 1-H-7 first floor\n mai vist buldding",width=42,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=880)
lab=Label(win,text="beside of shiv jyoti in front of dot code edification",width=39,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=180,y=935)


lab=Label(win,text="About Us",width=7,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=820)
lab=Label(win,text="Privacy Policy",width=11,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=855)
lab=Label(win,text="Terms of Service",width=13,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=890)
lab=Label(win,text="FAQs",width=4,fg="#FFFFFF", font=("bold",15),bg="#000000")
lab.place(x=780,y=925)

'''
file=PhotoImage(file="img23.png")
lab=Label(win,image=file)
lab.place(x=1350,y=820)

file1=PhotoImage(file="img24.png")
lab1=Label(win,image=file1)
lab1.place(x=1280,y=820)

file2=PhotoImage(file="imf4.png")
lab2=Label(win,image=file2)
lab2.place(x=1420,y=820)

file3=PhotoImage(file="img25.png")
lab3=Label(win,image=file3)
lab3.place(x=1490,y=820)
'''
win.mainloop()