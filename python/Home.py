from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import pymysql as sql
from tkcalendar import DateEntry
 
win=Tk()
win.config(bg="#73FBFD")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def booking():
    win.destroy()
    os.system("python booking.py")

def contact():
    win.destroy()
    os.system("python contact.py") 

def service():
    win.destroy()
    os.system("python service.py")       


def Home():
    win.destroy()
    os.system("python Home.py")

def About():
    win.destroy()
    os.system("python About.py") 

def cancel():
    win.destroy()
    os.system("python cancelticket.py")

def mybook():
    win.destroy()
    os.system("python MyBooking.py")    

def show():
    a=ent1.get()
    if a=="":
        messagebox.showerror("empty","Please fill the train details ")
    messagebox.showinfo("Success","Search Train")
    
    win.destroy()
    os.system("python pp.py")

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img9.webp")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()


frame=Frame(win,bg="#F0B87B",width=1920,height=100)
frame.place(x=0,y=1)

lab=Label(frame,text="Welcome To Indian Railway",width=25,height=0,fg="#000000",font=("bold",30),bg="#F0B87B")
lab.place(x=0,y=25)


btn=Button(frame,text="Home",width=9,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=Home)
btn.place(x=900,y=20)

btn=Button(frame,text="About",width=9,fg="#000000",font=("bold",20),bg="#F0B87B",command=About,relief="flat")
btn.place(x=1050,y=20)
btn=Button(frame,text="My Booking",width=9,fg="#000000",font=("bold",20),bg="#F0B87B",command=mybook,relief="flat")
btn.place(x=1240,y=20)
btn=Button(frame,text="Contact US",width=9,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=contact)
btn.place(x=1440,y=20)
btn=Button(frame,text="Service",width=9,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=service)
btn.place(x=1600,y=20)
btn=Button(frame,text="Cancel",width=9,fg="#000000",font=("bold",20),bg="#F0B87B",relief="flat",command=cancel)
btn.place(x=1750,y=20)

lab=Label(win,text="",width=15,height=8,fg="#000000", font=("bold",50),bg="#F0B87B")
lab.place(x=1050,y=200)


lab=Label(win,text="Search Your Journey",width=20,height=0,fg="#000000",font=("bold",30),bg="#F0B87B")
lab.place(x=1120,y=240)

lab=Label(win,text="from:",width=4,fg="#000000",font=("bold",20) ,bg="#F0B87B")
lab.place(x=1140,y=350)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent1.place(x=1140,y=390)

lab=Label(win,text="To:",width=3,fg="#000000",font=("bold",20) ,bg="#F0B87B")
lab.place(x=1140,y=450)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent2.place(x=1140,y=490)

lab=Label(win,text="Date:",width=5,fg="#000000",font=("bold",20) ,bg="#F0B87B")
lab.place(x=1130,y=550)
date=DateEntry(win, date_pattern="yyyy-mm-dd",width=38)
date.place(x=1140,y=590)

btn=Button(win,text="Search",width=35,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=show)
btn.place(x=1060,y=700)

win.mainloop()