from tkinter import *
from PIL import Image,ImageTk
knf1=Tk()
knf1.wm_state('zoomed')

knf1.title('MAHINDRA THAR VEHICLES')


knf1.config(bg='black')
iconimg=Image.open('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')
tkicon=ImageTk.PhotoImage(iconimg)
knf1.iconphoto(False,tkicon)

imgpath='C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\vehicles_images1.jpg'
img=Image.open(imgpath)
img=img.resize((1362,592))
bgimg=ImageTk.PhotoImage(img)
bglabel=Label(knf1,i=bgimg)
bglabel.place(x=1,y=60)

def star1():
    knf1.destroy()
    import car_collection
b1 = Button(knf1, text='Our SUVs', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=650, y=660)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendralogo.jpg'
img = Image.open(imgpath)
img = img.resize((100, 50))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf1, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=80, y=0)

l=Label(knf1,text='Vehicles',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=280,y=15)

l=Label(knf1,text='Buy',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=380,y=15)

l=Label(knf1,text='Service',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=15)


l=Label(knf1,text='Experience',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=545,y=15)

l=Label(knf1,text='Global Markets',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=675,y=15)

l=Label(knf1,text='Test Drive',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=950,y=15)

l=Label(knf1,text='Locate Us',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1070,y=15)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\searchimage1.jpg'
img = Image.open(imgpath)
img = img.resize((30, 30))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf1, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1200, y=15)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\loginimage1.jpg'
img = Image.open(imgpath)
img = img.resize((30, 30))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf1, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1280, y=15)



knf1.mainloop()
