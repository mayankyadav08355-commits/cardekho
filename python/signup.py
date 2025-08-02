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

def sign_up():
    username=ent1.get()
    password=ent2.get()
    if (username=="") or (password==""):
        messagebox.showwarning("Warning","Please provide a valid input!!!")
    else:
        cmd=f"select username from signup"
        conn,cur=db_connect()
        cur.execute(cmd)
        data=cur.fetchall()
        #Username_set=list(reduce(lambda x,y:x+y,data))
    
        if username in data:
            messagebox.showwarning("Warning","Username is already exists !!! try differnt username")
        else:
            cmd=f"insert into signup values('{username}','{password}')"
            cur.execute(cmd)
            conn.commit()
            messagebox.showinfo("Sign Up","Account is successfully Created")
            os.system("python Home.py")


def sign():
    win.destroy()
    os.system("python login.py")
'''
def fun():
    a=ent1.get()
    if a=="":
        messagebox.showerror("empty","Please fill the username")
    messagebox.showinfo("Success","signup Successfully")
    win.destroy()
    os.system("python home.py")
'''
def back():
    win.destroy()
    os.system("python first..py")

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img2.png")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=17,height=7,fg="#FFFEFE", font=("bold",50),bg="#09082E")
lab.place(x=1100,y=150)




lab=Label(win,text="Sign UP",width=10,fg="#FFFEFE", font=("bold",50),bg="#09082E")
lab.place(x=1250,y=200)


lab=Label(win,text="Username",width=8,fg="#FFFEFE",font=("bold",20) ,bg="#09082E")
lab.place(x=1164,y=300)
ent1=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#09082E")
ent1.place(x=1300,y=300)


lab=Label(win,text="Password",width=8,fg="#FFFEFE",font=("bold",20),bg="#09082E")
lab.place(x=1164,y=400)
ent2=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#09082E")
ent2.place(x=1300,y=400)

lab=Label(win,text="You have an account aalready ",width=25,fg="#FFFEFE",font=("bold",15),bg="#09082E")
lab.place(x=1164,y=460)

btn=Button(win,text="login",width=5,fg="#73FBFD",font=("bold",15),bg="#09082E",command=sign,relief=FLAT)
btn.place(x=1435,y=455)

btn=Button(win,text="Sign up",width=15,height=1,fg="#FFFEFE",font=("bold",20),bg="#09082E",command=sign_up)
btn.place(x=1150,y=550)

btn=Button(win,text="back",width=15,height=1,fg="#FFFEFE",font=("bold",20),command=back,bg="#09082E")
btn.place(x=1450,y=550)

win.mainloop()