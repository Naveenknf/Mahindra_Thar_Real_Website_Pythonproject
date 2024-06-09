from tkinter import *
from PIL import Image,ImageTk
#to create a frame/window
knf=Tk()
#window maximize
knf.wm_state('zoomed')

#to set frame title
knf.title('MAHENDRA THAR BUY')
knf.config(bg='black')

iconimg=Image.open('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')
tkicon=ImageTk.PhotoImage(iconimg)
knf.iconphoto(False,tkicon)

l=Label(knf,text='Buy Your Choose',font=('Calibri',25),bg='black',fg='white')
#x axis,y axis place
l.place(x=0,y=0)

l=Label(knf,text='SCORPIO-N',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=30,y=50)

l=Label(knf,text='price $ 1360199*',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=100,y=275)

def star1():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star1, fg='White', bg='black')
b9.place(x=30, y=305)

def star2():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star2, fg='White', bg='black')
b9.place(x=150, y=305)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy1.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=10, y=80)

l=Label(knf,text='XUV 700',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=400,y=50)

l=Label(knf,text='prize $ 1399000*',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=480,y=275)

def star3():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star3, fg='White', bg='black')
b9.place(x=400, y=305)

def star4():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star4, fg='White', bg='black')
b9.place(x=520, y=305)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy2.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=350, y=80)

l=Label(knf,text='THAR',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=730,y=50)

l=Label(knf,text='prize $ 1125000*',font=('calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=850,y=275)

def star5():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star5, fg='White', bg='black')
b9.place(x=750, y=305)

def star6():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star6, fg='White', bg='black')
b9.place(x=880, y=305)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy3.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=700, y=80)

l=Label(knf,text='XUV 300',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1100,y=50)

l=Label(knf,text='prize $ 799000*',font=('calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1200,y=275)

def star7():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star7, fg='White', bg='black')
b9.place(x=1100, y=305)

def star8():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star8, fg='White', bg='black')
b9.place(x=1220, y=305)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy4.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1050, y=80)


l=Label(knf,text='BOLERO',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=390)

l=Label(knf,text='prize $ 989599*',font=('calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=130,y=630)

def star9():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star9, fg='White', bg='black')
b9.place(x=50, y=660)

def star10():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star10, fg='White', bg='black')
b9.place(x=160, y=660)


l=Label(knf,text='SCORPIO CLASSIC',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=380,y=390)

l=Label(knf,text='prize $ 1358600.*',font=('calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=480,y=630)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy5.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=10, y=430)

def star11():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star9, fg='White', bg='black')
b9.place(x=390, y=660)

def star12():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star10, fg='White', bg='black')
b9.place(x=510, y=660)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy6.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=350, y=430)

l=Label(knf,text='BOLERO NEO',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=750,y=390)

l=Label(knf,text='prize $ 989600*',font=('calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=850,y=630)

def star13():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star13, fg='White', bg='black')
b9.place(x=750, y=660)

def star14():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star14, fg='White', bg='black')
b9.place(x=880, y=660)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy9.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=700, y=430)


l=Label(knf,text='XUV400',font=('jumble',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1100,y=390)

l=Label(knf,text='prize $ 1549000*',font=('calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1200,y=630)

def star15():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Explore', font=('Elephant', 15),command=star15, fg='White', bg='black')
b9.place(x=1100, y=660)

def star16():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Book Now', font=('Elephant', 15),command=star16, fg='White', bg='black')
b9.place(x=1220, y=660)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\buy8.jpg'
img = Image.open(imgpath)
img = img.resize((300, 200))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1050, y=430)

def star17():
    knf.destroy()
    import service
b1 = Button(knf, text='After', font=('Elephant', 12),command=star17, fg='White', bg='black', )
b1.place(x=1270, y=20)



knf.mainloop()


