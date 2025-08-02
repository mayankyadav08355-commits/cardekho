from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import pymysql as sql
 
win=Tk()
win.config(bg="#73FBFD")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def db_connect():
    conn= sql.connect(host='localhost',user='root',password='',port=3306,database='rail_way')
    cur=conn.cursor()
    return conn,cur

def payment():
    full_name=ent1.get()
    email=ent2.get()
    phone=ent3.get()
    Aadhar=ent4.get()
    clas=var.get()
    fro=ent5.get()
    to=ent6.get()
    d=date.get()
    
def payment():
    full_name = ent1.get()
    email = ent2.get()
    phone = ent3.get()
    Aadhar = ent4.get()
    clas = com.get()  # Get selected class from combobox
    fro = ent5.get()
    to = ent6.get()
    d = date.get()

    # Set payment based on class selected
    if clas == 'Sleeper':
        payment_amount = 1500
    elif clas == 'Economic':
        payment_amount = 1000
    elif clas == 'General':
        payment_amount =500 
    else:
        messagebox.showerror("Error", "Invalid class selected!")
        return

    # Print the payment amount (you can use it for further processing)
    print(f"Payment Amount for {clas} class: {payment_amount}")

    


    cmd=f"insert into pbookings values('{full_name}','{email}','{phone}','{Aadhar}','{clas}','{fro}','{to}','{d}')"
    conn,cur=db_connect()
    cur.execute(cmd)
    conn.commit()
    print(cmd)
    win.destroy()
    os.system(f"python payment.py {payment_amount}")
    #os.system("python payment.py")

    #cmd=f"insert into pbooking values('{full_name}','{email}','{phone}','{Aadhar}','{clas}','{fro}','{to}','{d}')"

 

def Home():
    win.destroy()
    os.system("python Home.py")



image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\head-train-hauled-diesel-electric-locomotive-isolated-white-background-copy-space-202966014.webp")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

    
    


lab=Label(win,text="",width=20,height=13,fg="#000000", font=("bold",50),bg="#FFFFFF")
lab.place(x=1000,y=10)

lab=Label(win,text="Train Ticket booking",width=20,fg="#000000", font=("bold",30),bg="#FFFFFF")
lab.place(x=1180,y=30)

lab=Label(win,text=" Booking for: {{train_name}}",width=25,fg="#000000", font=("bold",20),bg="#FFFFFF")
lab.place(x=1060,y=130)

lab=Label(win,text="Full Name",width=8,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=210)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent1.place(x=1300,y=210)

lab=Label(win,text="Email",width=4,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=280)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent2.place(x=1300,y=280)


lab=Label(win,text="Phone N0.",width=8,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=350)
ent3=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent3.place(x=1300,y=350)


lab=Label(win,text="Aadhar card no.",width=12,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=420)
ent4=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent4.place(x=1300,y=420)

lab=Label(win,text="class",width=4,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=490)
var=StringVar()
com=ttk.Combobox(win,width=38,background="#F0F0F0")
com['state']='readonly'
com['values']=('General','Economic','Sleeper')
com.place(x=1300,y=490)


lab=Label(win,text="from",width=4,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=560)
ent5=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent5.place(x=1300,y=560)

lab=Label(win,text="To",width=3,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=630)
ent6=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent6.place(x=1300,y=630)

lab=Label(win,text="Date",width=5,fg="#000000",font=("bold",20) ,bg="#FFFFFF")
lab.place(x=1100,y=690)
date=DateEntry(win, date_pattern="yyyy-mm-dd",width=38)
date.place(x=1300,y=690)


btn=Button(win,text="Book Ticket",width=45,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=payment)
btn.place(x=1025,y=790)

btn=Button(win,text="Back Home",width=45,height=1,fg="#000000",font=("bold",20),bg="#A1FB8E",command=Home  )
btn.place(x=1025,y=890)



win.mainloop()