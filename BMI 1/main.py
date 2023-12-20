from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")


#icon
image_icon=PhotoImage(file="BMI 1/images/icon.png")
root.iconphoto(False,image_icon)


#top
top=PhotoImage(file="BMI 1/images/top.png")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10,y=-10)


#bottom
Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)

#two boxes
box=PhotoImage(file="BMI 1/images/box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

#scale
scale=PhotoImage(file="BMI 1/images/scale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=310)


#######################################Slider1#####################
current_value=tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())


#command to change background color of scale slider
style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(root,from_=0,to=220,orient='horizontal',style="TScale",command=slider_changed, variable=current_value)
slider.place(x=80,y=250)



################################################################################




##############################Slider2################################################





################################################################


#Entry Box
Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER) #to align text center.
height.place(x=35,y=160)
#Height.set()

weight = Entry(root, textvariable=Weight, width=5, font='arial 50',bg="#fff", fg="#000", bd=0, justify=CENTER)  # to align text center.
weight.place(x=225, y=160)
#Weight.set()


#man image
secondimage=Label(root,bg="lightblue")
secondimage.place(x=70,y=530)

root.mainloop()