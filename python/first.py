'''from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
from PIL import Image,ImageTk
 
win=Tk()
win.config(bg="skyblue")
win.minsize(width="1920",height="1080")
win.maxsize(width="1920",height="1080")'''

'''image= Image.open("photo.png")
image = image.resize((200,150))

tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(win,image=tk_image)
image_label.place(x=650,y=220)'''

'''file=PhotoImage(file="imf2.png")
lab1=Label(win,image=file)
lab1.pack()

mayank= Image.open("img4.png")
mayank = mayank.resize((200,150))

tk_image = ImageTk.PhotoImage(mayank)
may = tk.Label(win,image=tk_image)
may.place(x=1400,y=100)
def fun():
    messagebox.showwarning("warnig","empty")'''

'''lab=Label(win,text="name",width=30,height=5,bg="black",fg="pink")
lab.place(x=0,y=0)

ent=Entry(win,width=30,font=("bold",30),fg="blue")
ent.place(x=10,y=20)

btn=Button(win,text="okk",width=15,height=5,bg="blue",fg="black")
btn.place(x=30,y=50)

var=StringVar()
com=ttk.Combobox(win,width=30)
com['state']='readonly'
com['values']=('jan','feb','march')
com.place(x=0,y=100)

checkbtn1=IntVar()
checkbtn2=IntVar()

but=Checkbutton(win,text="python",variable=checkbtn1)
but.pack()

var=IntVar()
radio=Radiobutton(win,text="male",value=0,variable=var)
radio.pack()
radio=Radiobutton(win,text="female",value=1,variable=var)
radio.pack()


bt=Button(win,text="print",command=fun)
bt.place(x=0,y=2)

lab=Label(win,text="enterNo.1",width=10)
lab.place(x=0,y=0)

ent=Entry(win,width=30,font=("bold",15),fg="blue")
ent.place(x=100,y=0)


lab=Label(win,text="enterNo.2",width=10,bg="black",fg="pink")
lab.place(x=0,y=50)



checkbtn1=IntVar()


but=Checkbutton(win,text="fill the form",variable=checkbtn1,font=("bold",20))
but.place(x=1000,y=450)

var=IntVar()
lab=Label(win,text="Gender",width=10,fg="black",font=("bold",25) )
lab.place(x=1000,y=550)
radio=Radiobutton(win,text="male",value=0,variable=var,font=("bold",20))
radio.place(x=1250,y=550)
radio=Radiobutton(win,text="female",value=1,variable=var,font=("bold",20))
radio.place(x=1370,y=550)

image= Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img2.png")
image = image.resize((1920,1080))

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(win,image=tk_image)
image_label.pack()'''

'''bt=Button(win,text="print",command=fun)
bt.place(x=0,y=2)

ent=Entry(win,width=30,font=("bold",15),fg="blue")
ent.pack(pady=20)'''

'''trv=ttk.Treeview(win,columns=(1,2),height=15,show="headings")
  
trv.column(1,anchor=CENTER,stretch=NO,width=100)  
trv.column(2,anchor=CENTER,stretch=NO,width=100)
    
trv.heading(1,text="gcuwefh")
trv.heading(2,text="gcuwefh")
trv.place(x=100,y=10)'''

from tkinter import *
import tkinter as tk
win=Tk()
win.geometry("500x500")
win.config(bg="skyblue")
lab=Label(win,text="LOG IN",width=10,fg="black", bg="white")
lab.place(x=150,y=50)
lab=Label(win,text="Username",width=8,fg="black",bg="white")
lab.place(x=100,y=100)
ent1=Entry(win,width=20,fg="black",bg="white")
ent1.place(x=200,y=100)
lab=Label(win,text="Password",width=8,fg="black",bg="white")
lab.place(x=100,y=150)
ent2=Entry(win,width=20,fg="black",bg="white")
ent2.place(x=200,y=150)
var=IntVar()
radio=Radiobutton(win,text="male",value=0,variable=var)
radio.place(x=100,y=200)
radio=Radiobutton(win,text="female",value=1,variable=var)
radio.place(x=300,y=200)
btn=Button(win,text="Log in",width=10,height=1,fg="black",bg="white")
btn.place(x=100,y=250)
btn=Button(win,text="back",width=10,height=1,fg="black",bg="white")
btn.place(x=250,y=250)
win.mainloop()





