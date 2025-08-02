from tkinter import *
from tkinter import ttk
import tkinter
 
win=Tk()
win.config(bg="skyblue")
win.minsize(width="1700",height="1000")
win.maxsize(width="500",height="500")

def add():
    n1=ent1.get()
    n2=ent2.get()
    num3=int(n1)+int(n2)
    lab=Label(win,text=num3,width=10,bg="black",fg="pink")
    lab.place(x=0,y=300)

def sub():
    n1=ent1.get()
    n2=ent2.get()
    num4=int(n1)-int(n2)
    lab=Label(win,text=num4,width=10,bg="black",fg="pink")
    lab.place(x=0,y=300)

def multi():
     n1=ent1.get()
     n2=ent2.get()
     num4=int(n1)*int(n2)
     lab=Label(win,text=num4,width=10,bg="black",fg="pink")
     lab.place(x=0,y=300)

def divi():
     n1=ent1.get()
     n2=ent2.get()
     num4=int(n1)/int(n2)
     lab=Label(win,text=num4,width=10,bg="black",fg="pink")
     lab.place(x=0,y=300)     


lab=Label(win,text="enterNo.1",width=10,bg="black",fg="pink")
lab.place(x=0,y=0)

ent1=Entry(win,width=30,font=("bold",18),fg="blue")
ent1.place(x=100,y=0)


lab=Label(win,text="enterNo.2",width=10,bg="black",fg="pink")
lab.place(x=0,y=50)


ent2=Entry(win,width=30,font=("bold",18),fg="blue")
ent2.place(x=100,y=50)

btn=Button(win,text="add",width=15,height=1,bg="blue",fg="black",command=add)
btn.place(x=80,y=100)



btn=Button(win,text="subtraction",width=15,height=1,bg="blue",fg="black",command=sub)
btn.place(x=80,y=140)


btn=Button(win,text="multiplication",width=15,height=1,bg="blue",fg="black",command=multi)
btn.place(x=80,y=180)




btn=Button(win,text="divide",width=15,height=1,bg="blue",fg="black",command=divi)
btn.place(x=80,y=220)

'''file=PhotoImage(file="main1.png")

lbl=Label(win,image=file,width=728,height=445)
lbl.place(x=0,y=0)'''


win.mainloop()