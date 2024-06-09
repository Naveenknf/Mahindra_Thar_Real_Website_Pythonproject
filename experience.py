from tkinter import *
from PIL import Image,ImageTk
import tkinter

knf=Tk()
knf.wm_state('zoomed')

knf.title('MAHINDRA THAR EXPERIENCE')

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


imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\experience1.jpg'
img = Image.open(imgpath)
img = img.resize((260, 520))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=30, y=110)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\experience2.jpg'
img = Image.open(imgpath)
img = img.resize((260, 520))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=295, y=150)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\experience3.jpg'
img = Image.open(imgpath)
img = img.resize((260, 520))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=560, y=110)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\experience4.jpg'
img = Image.open(imgpath)
img = img.resize((260, 520))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=825, y=150)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\experience5.jpg'
img = Image.open(imgpath)
img = img.resize((260, 520))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1090, y=110)

def star1():
    knf.destroy()
    import global1
b1 = Button(knf, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1260, y=40)

knf.mainloop()
