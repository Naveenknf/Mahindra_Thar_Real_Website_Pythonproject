from tkinter import *
from PIL import Image,ImageTk
import tkinter

knf=Tk()
knf.wm_state('zoomed')
knf.title('MAHINDRA THAR VARIANTS')

knf.config(bg="black")

iconimg=Image.open('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')
tkicon=ImageTk.PhotoImage(iconimg)
knf.iconphoto(False,tkicon)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendralogo.jpg'
img = Image.open(imgpath)
img = img.resize((120, 80))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=30, y=10)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\3barcode.png'
img = Image.open(imgpath)
img = img.resize((100, 80))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1250, y=10)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\explore1.jpg'
img = Image.open(imgpath)
img = img.resize((800, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=560, y=60)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\variants1.jpg'
img = Image.open(imgpath)
img = img.resize((800, 400))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=680, y=200)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\explore3.jpg'
img = Image.open(imgpath)
img = img.resize((600, 400))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=2, y=400)

l=Label(knf,text='VARIANTS & PRICING*',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=110)

l=Label(knf,text='Xplore All Variants ',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=150)

l=Label(knf,text='LXDAT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=190)

l=Label(knf,text='4WDHT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=220)

l=Label(knf,text='EARTH ED ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=250)

l=Label(knf,text='$ 1760 001.00',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=280)

l=Label(knf,text='Transmission',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=330)

l=Label(knf,text='Automatic',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=350)

l=Label(knf,text='Max.Power',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=400)

l=Label(knf,text='97kW',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=420)

l=Label(knf,text='Seeating Capacity',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=470)

l=Label(knf,text='4 Seater',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=490)

l=Label(knf,text="Key Features",font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=550)

l=Label(knf,text="HVAC,Touchscreen",font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=570)


l=Label(knf,text='LXDAT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=190)

l=Label(knf,text='4WDHT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=220)

l=Label(knf,text='EARTH ED ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=250)

l=Label(knf,text='$ 1760 001.00',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=280)

l=Label(knf,text='Transmission',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=330)

l=Label(knf,text='Automatic',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=350)

l=Label(knf,text='Max.Power',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=400)

l=Label(knf,text='97kW',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=420)

l=Label(knf,text='Seeating Capacity',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=470)

l=Label(knf,text='4 Seater',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=490)

l=Label(knf,text="Key Features",font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=550)

l=Label(knf,text="DRL,Alloys,BLD",font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=250,y=570)


l=Label(knf,text='LXPMT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=190)

l=Label(knf,text='4WDHT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=220)

l=Label(knf,text='EARTH ED ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=250)

l=Label(knf,text='$ 1540 000.00',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=280)

l=Label(knf,text='Transmission',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=330)

l=Label(knf,text='Manual',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=350)

l=Label(knf,text='Max.Power',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=400)

l=Label(knf,text='112kW',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=420)

l=Label(knf,text='Seeating Capacity',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=470)

l=Label(knf,text='4 Seater',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=490)

l=Label(knf,text="Key Features",font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=550)

l=Label(knf,text="R18A/T Tyres",font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=430,y=570)



l=Label(knf,text='LXPAT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=190)

l=Label(knf,text='4WDHT ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=220)

l=Label(knf,text='EARTH ED ',font=('Calibri',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=250)

l=Label(knf,text='$ 1699 800.00',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=280)

l=Label(knf,text='Transmission',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=330)

l=Label(knf,text='Automatic',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=350)

l=Label(knf,text='Max.Power',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=400)

l=Label(knf,text='112kW',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=420)

l=Label(knf,text='Seeating Capacity',font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=470)

l=Label(knf,text='4 Seater',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=490)

l=Label(knf,text="Key Features",font=('Calibri',13),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=550)

l=Label(knf,text="Driver Information",font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=640,y=570)

def star1():
    knf.destroy()
    import Gallery
b1 = Button(knf, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1200, y=35)

knf.mainloop()

