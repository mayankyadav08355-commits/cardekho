from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
import sys
import pymysql as sql
 
 
win=Tk()
win.config(bg="#48B5FF")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")



def fun():
    a=ent1.get()
    a=ent2.get()
    a=ent3.get()
    if a=="":
        messagebox.showerror("empty","Please fill the Details")
    else:    
        messagebox.showinfo("Success","payment Successfully")
        win.destroy()
if len(sys.argv) > 1:
    payment_amount = sys.argv[1]  # This is the amount passed from booking.py
else:
    payment_amount = "N/A"  # Default value if no argument is passed
    

def Previous():
    win.destroy()
    os.system("python Home.py") 

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img5.jpg")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()


lab=Label(win,text="",width=20,height=10,font=("bold",50),bg="#B5FCF6")
lab.place(x=50,y=130)

file1=PhotoImage(file="imf3.png")
lab1=Label(win,image=file1)
lab1.place(x=130,y=220)
'''
file=PhotoImage(file="img6.png")
lab=Label(win,image=file)
lab.place(x=540,y=220)
'''


lab=Label(win,text="Payment Details",width=20,fg="#000000", font=("bold",30),bg="#B5FCF6")
lab.place(x=200,y=150)


lab=Label(win,text="Card Number:",width=10,fg="#000000",font=("bold",20) ,bg="#B5FCF6")
lab.place(x=130,y=410)
ent1=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent1.place(x=340,y=410)


lab=Label(win,text="payment:"+ payment_amount,width=18,fg="#000000", font=("bold",20),bg="#B5FCF6")
lab.place(x=130,y=480)


lab=Label(win,text="Expiry Date:",width=9,fg="#000000",font=("bold",20) ,bg="#B5FCF6")
lab.place(x=130,y=550)
ent2=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent2.place(x=340,y=550)


lab=Label(win,text="CVV:",width=4,fg="#000000",font=("bold",20) ,bg="#B5FCF6")
lab.place(x=130,y=620)
ent3=Entry(win,width=25,font=("bold",21),fg="#000000",bg="#F0F0F0")
ent3.place(x=340,y=620)

btn=Button(win,text="Previous",width=10,fg="#000000",font=("bold",20),bg="#A1FB8E",command=Previous)
btn.place(x=130,y=750)

btn=Button(win,text="Submit",width=10,fg="#000000",font=("bold",20),bg="#A1FB8E",command=fun)
btn.place(x=570,y=750)


win.mainloop()