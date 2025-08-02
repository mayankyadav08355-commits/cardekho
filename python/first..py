from tkinter import *
from tkinter import ttk,Frame,Button
import tkinter as tk
import os 
from PIL import Image,ImageTk

def update_progress(value):
    canvas.delete("progress")
    canvas.create_rectangle(0,0,value *1, bar_height, fill="pink", tags="progress")
    lbl.config(text=f'loading....{value//10}')
    if value <1000:
        win.after(4,update_progress,value+1)
    else :
        win.destroy()
        os.system("python signup.py") 
win=Tk()

win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")

def book():
    win.destroy()
    os.system("python signup.py")
image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img3.png")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()





lab=Label(win,text="Welcome to Railway Ticket Reservation",width=35,fg="#133294", font=("bold",50),bg="#FFAFFB")
lab.place(x=250,y=100)



lab=Label(win,text="Book your train ticket with ease and convenience",width=40,fg="#133294", font=("bold",25),bg="#FFAFFB")
lab.place(x=550,y=200)


bar_width=1300
bar_height=50

lbl=Label(win)
lbl.place(x=350,y=760)
canvas=tk.Canvas(win,width=bar_width, height=bar_height,bg="white")
canvas.place(x=350,y=800)
update_progress(0)

win.mainloop()