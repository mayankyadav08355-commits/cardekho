from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image,ImageTk
 
win=Tk()
win.config(bg="#73FBFD")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def back():
    win.destroy()
    os.system("python Home.py")

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img0.png")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.pack()

lab=Label(win,text="Who We Are",width=10,height=0,fg="#000000",font=("bold",30))
lab.place(x=30,y=10)
lab=Label(win,text="Welcome to our Railway Project! We are  dedicated to providing a seamless, efficient, and  eco-friendly transportation\n solution for all our passengers Our project leverages cutting-edge  technology to ensure safety, speed, and comfort.",width=100,height=0,fg="#000000",font=("bold",15))
lab.place(x=0,y=60)
lab=Label(win,text="Our Mission",width=9,height=0,fg="#000000",font=("bold",30))
lab.place(x=30,y=140)
lab=Label(win,text="Our mission is to revolutionize rail travel by integrating modern technology with sustainable practices. We aim to connect\n cities and communities, fostering economic growth and reducing the environmental impact of transportation",width=100,height=0,fg="#000000",font=("bold",15))
lab.place(x=10,y=190)

lab=Label(win,text="What We Offer",width=12,height=0,fg="#000000",font=("bold",30))
lab.place(x=30,y=270)
lab=Label(win,text="Our railway services include high-speed travel, punctual schedules, and state-of-the-art facilities. Whether you're\n commuting to work or traveling across the country, we ensure a reliable and enjoyable journey",width=94,height=0,fg="#000000",font=("bold",15))
lab.place(x=10,y=320)

btn=Button(win,text="Go Back",width=15,height=1,fg="#FFFEFE",font=("bold",20),command=back,bg="#09082E")
btn.place(x=50,y=450)
win.mainloop()