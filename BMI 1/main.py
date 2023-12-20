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

root.mainloop()