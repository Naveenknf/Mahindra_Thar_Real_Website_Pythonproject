from tkinter import *
from PIL import Image,ImageTk
import tkinter

knf=Tk()
knf.wm_state('zoomed')

knf.title('MAHINDRA THAR EXPLORE')

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


imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\explore1.jpg'
img = Image.open(imgpath)
img = img.resize((800, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=560, y=60)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\explore2.jpg'
img = Image.open(imgpath)
img = img.resize((600, 400))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=700, y=250)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\explore3.jpg'
img = Image.open(imgpath)
img = img.resize((600, 400))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=2, y=400)

l=Label(knf,text='EXPLORE THAR',font=('Calibri',25),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=150)

l=Label(knf,text='Here is where the ',font=('Elephant',30),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=240)

l=Label(knf,text='Himpossible begins ',font=('Elephant',30),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=310)

l=Label(knf,text='An enduring con that just keeps on giving,The All-New Thar comes',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=400)

l=Label(knf,text='equipped with the iconic design and all new interiors to help you',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=430)

l=Label(knf,text='Explore The Impossible',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=470)

def star1():
    knf.destroy()
    #import vehicles
b1 = Button(knf, text='ENQUIRE NOW', font=('Elephant', 18),command=star1, fg='White', bg='black', )
b1.place(x=150, y=550)
def star2():
    knf.destroy()
   # import pls2
b2 = Button(knf, text='TEST DRIVE', font=('Elephant', 18),command=star2, fg='White', bg='black')
b2.place(x=410, y=550)

def star1():
    knf.destroy()
    import key1
b1 = Button(knf, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1250, y=30)

'''def star1():
    knf.destroy()
    #import 
b1 = Button(knf, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1250, y=30)'''

knf.mainloop()
