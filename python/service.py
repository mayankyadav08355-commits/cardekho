from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
import os
from PIL import Image,ImageTk
 

win=Tk()
win.config(bg="skyblue")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def Home():
    win.destroy()
    os.system("python Home.py")


image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img27.png")
image = image.resize((1920,900))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.place(x=0,y=110)


lab=Label(win,text="",width=100,height=2,fg="#FFFEFE", font=("bold",35),bg="red")
lab.place(x=0,y=0)


lab=Label(win,text="Here are Some Facilities Available on Indian\n Railways Trains and at Railway Stations",width=40,height=2,fg="#000000", font=("bold",25),bg="red")
lab.place(x=10,y=10)

btn=Button(win,text="back Home",width=15,height=1,fg="#FFFFFF",font=("bold",20),command=Home,bg="#0023F5")
btn.place(x=1550,y=30)

win.mainloop()