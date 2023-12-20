import customtkinter
from tkinter import *
from PIL import Image


app=customtkinter.Ctk()
app.geometry("300x500")
app.title("BMI CALCULATOR")
app.config(bg="#020414")

image_icon=PhotoImaege(file="")
app.iconphoto(False,image_icon)

top=Label(app,text="BMI CALCULATOR",font=('Arial',18,'bold'),fg="#FFFFFF",












app.mainloop()