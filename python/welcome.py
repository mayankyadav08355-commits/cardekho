from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os
from tkinter import ttk

def update_progress(value):
    canvas.delete("progress")
    canvas.create_rectangle(0,0,value *1, bar_height, fill="green", tags="progress")
    lbl.config(text=f'loading....{value//10}')
    if value <1000:
        win.after(4,update_progress,value+1)
    else :
        win.destroy()
        os.system("python first..py") 
win=Tk()


#image=("about as.jpg")
win.state('zoomed') #output hmesha full screen me open hoga
files1=Image.open("C:\\Users\\Mayank\\Desktop\\railway ticket system\\img.png")  # used for open image
files2=files1.resize((1300,700)) #for assign size
 
tk_image=ImageTk.PhotoImage(files2) #tk_imagee is a var name and ImageTk.PhotoImage is predefined
 
new_Label=tk.Label(win,image=tk_image) # here is image= is predefined
new_Label.pack()    #fix image in full screen


bar_width=1000
bar_height=40
#win.wm_attributes('-transparent color',"#ab23ff")
win.geometry("1000x500")
lbl=Label(win)
lbl.place(x=150,y=470)
canvas=tk.Canvas(win,width=bar_width, height=bar_height,bg="white")
canvas.place(x=150,y=500)
update_progress(0)


 





#lbl1=Label(win,text="WELCOME \n TO EVENT MANAFMENT PROGECT",fg="black",font=("Rockwell Extra Bold",22,"bold"))
#lbl1.place(x=350,y=380)


win.mainloop()