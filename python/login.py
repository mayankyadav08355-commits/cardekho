from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
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
    username=ent1.get()
    password=ent2.get()
    cmd=f"select * from signup where username='{username}'"
    conn,cur=db_connect()
    data=cur.execute(cmd)
    if data:
        cmd=f"select * from signup where username='{username}' and  password='{password}'"
        data = cur.execute(cmd)
        if data:
             messagebox.showinfo("","loginsuccessful")
             return afterlog()
        else:
            messagebox.showwarning("","incorect password")
    else:
        messagebox.showwarning("","not registerd account")



def afterlog():
    username=ent1.get()
    password=ent2.get()
    if username=="" or password=="":
        messagebox.showwarning("","please fill all field ")
    else:
        win.destroy()
        os.system("python Home.py")   




def back():
    win.destroy()
    os.system("python signup.py")

def Home():
    win.destroy()
    os.system("python Home.py")


def sign():
    win.destroy()
    os.system("python signup.py")

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img2.png")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="",width=17,height=7,fg="#FFFEFE", font=("bold",50),bg="#09082E")
lab.place(x=1100,y=150)




lab=Label(win,text="LOG IN",width=10,fg="#FFFEFE", font=("bold",50),bg="#09082E")
lab.place(x=1250,y=200)


lab=Label(win,text="Username",width=8,fg="#FFFEFE",font=("bold",20) ,bg="#09082E")
lab.place(x=1164,y=300)
ent1=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#09082E")
ent1.place(x=1300,y=300)


lab=Label(win,text="Password",width=8,fg="#FFFEFE",font=("bold",20),bg="#09082E")
lab.place(x=1164,y=400)
ent2=Entry(win,width=25,font=("bold",21),fg="#FFFEFE",bg="#09082E")
ent2.place(x=1300,y=400)



btn=Button(win,text="Log in",width=15,height=1,fg="#FFFEFE",font=("bold",20),bg="#09082E",command=reference)
btn.place(x=1150,y=550)

btn=Button(win,text="back",width=15,height=1,fg="#FFFEFE",font=("bold",20),command=back,bg="#09082E")
btn.place(x=1450,y=550)

win.mainloop()