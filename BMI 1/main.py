from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


root = Tk()
root.title("BMI Calculator")
root.geometry("600x600+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")


def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    # convert height to meter
    m = h/100
    bmi = round(float(w/m**2))
    label1.config(text=bmi)

    if (bmi <= 18.5):
        label2.config(text="underweight!")
        label3.config(text="It indicates ,\n You have lower weight.")

    elif (bmi >= 18.5 and bmi <= 25):
        label2.config(text="Normal!")
        label3.config(text="It indicates,\n you have healthy body!")

    elif (bmi > 25 and bmi <= 30):
        label2.config(text="Overweight!")
        label3.config(
            text="It indicates,\n you ar slightly overweight!\n")

    else:
        label2.config(text="Obese!")
        label3.config(
            text="Health may be at risk, \n if you do not lose weight")


# icon
image_icon = PhotoImage(file="BMI 1/images/icon.png")
root.iconphoto(False, image_icon)


# top
top = PhotoImage(file="BMI 1/images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=50, y=10)


# bottom
Label(root, width=73, height=15, bg="lightblue").pack(side=BOTTOM)


# two boxes
box = PhotoImage(file="BMI 1/images/box.png")
Label(root, image=box).place(x=50, y=100)
Label(root, image=box).place(x=330, y=100)


# scale
scale = PhotoImage(file="BMI 1/images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=330)


####################################### Slider1#####################
current_value1 = tk.DoubleVar()


def get_current_value1():
    return '{: .2f}'.format(current_value1.get())


def slider_changed1(event):
    Height.set(get_current_value1())

    size = int(float(get_current_value1()))
    img = (Image.open("BMI 1/images/man.png"))
    resized_image = img.resize((50, 10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image = photo2


# command to change background color of scale slider
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=200, orient='horizontal',
                   style="TScale", command=slider_changed1, variable=current_value1)
slider.place(x=80, y=250)


################################################################################


############################## Slider2################################################
current_value2 = tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())


# command to change background color of scale slider
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal',
                    style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=370, y=250)


################################################################


# Entry Box
Height = StringVar()
Weight = StringVar()

height = Entry(root,  textvariable=Height, width=6, font='arial 30',
               bg="#fff", fg="#000", bd=0, justify=CENTER)  # to align text center.
height.place(x=70, y=160)
Height.set(get_current_value1())

weight = Entry(root, textvariable=Weight, width=6, font='arial 30',
               bg="#fff", fg="#000", bd=0, justify=CENTER)  # to align text center.
weight.place(x=350, y=160)
Weight.set(get_current_value2())


# man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)


Button(root, text="View Report", width=15, height=2, font="arial 10 bold",
       bg="#1f6e68", fg="white", command=BMI).place(x=430, y=530)

label1 = Label(root, font="arial 55 bold",
               bg="lightblue", fg="#000000")
label1.place(x=420, y=375)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=200, y=450)

label3 = Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=185, y=500)


root.mainloop()
