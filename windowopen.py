from tkinter import *
from PIL import Image,ImageTk
import tkinter

knf=Tk()
knf.wm_state('zoomed')

knf.title('MAHINDRA THAR')

knf.config(bg="black")

iconimg=Image.open('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')
tkicon=ImageTk.PhotoImage(iconimg)
knf.iconphoto(False,tkicon)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendralogo.jpg'
img = Image.open(imgpath)
img = img.resize((150, 110))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=0, y=10)

def star1():
    knf.destroy()
    import vehicles
b1 = Button(knf, text='Vehicles', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=150, y=30)
def star2():
    knf.destroy()
    import buy
b2 = Button(knf, text='buy', font=('Elephant', 12),command=star2, fg='White', bg='black')
b2.place(x=240, y=30)
def star3():
    knf.destroy()
    import service
b3 = Button(knf, text='Service', font=('Elephant', 12),command=star3, fg='White', bg='black')
b3.place(x=300, y=30)
def star4():
    knf.destroy()
    import experience
b4= Button(knf, text='Experience', font=('Elephant', 12),command=star4, fg='White', bg='black')
b4.place(x=390, y=30)
def star5():
    knf.destroy()
    import global1
b5 = Button(knf, text='Global Markets', font=('Elephant', 12),command=star5, fg='White', bg='black')
b5.place(x=510, y=30)
def star6():
    knf.destroy()
    #import vehicles
b6 = Button(knf, text='Test Drive', font=('Elephant', 12),command=star6, fg='White', bg='black')
b6.place(x=670, y=30)
def star7():
    knf.destroy()
    #import vehicles
b7 = Button(knf, text='Locate Us', font=('Elephant', 12),command=star7, fg='White', bg='black')
b7.place(x=790, y=30)
def star8():
    knf.destroy()
    #import vehicles
b8 = Button(knf, text='Search', font=('Elephant', 12),command=star8, fg='White', bg='black')
b8.place(x=930, y=30)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\searchimage1.jpg'
img = Image.open(imgpath)
img = img.resize((40,40))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=890, y=25)

def star9():
    knf.destroy()
    #import vehicles
b9 = Button(knf, text='Login', font=('Elephant', 12),command=star9, fg='White', bg='black')
b9.place(x=1040, y=30)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\loginimage1.jpg'
img = Image.open(imgpath)
img = img.resize((30,30))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1010, y=25)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendrarise2.jpg'
img = Image.open(imgpath)
img = img.resize((230,100))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1130, y=0)

'''l=Label(knf,text='OWN THAR',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=150,y=100)'''
def star15():
    knf.destroy()
    import own
b10 = Button(knf, text='OWN THAR', font=('Elephant', 12),command=star15, fg='White', bg='black')
b10.place(x=150, y=100)

def star10():
    knf.destroy()
    import explore
b10 = Button(knf, text='Explore Thar', font=('Elephant', 12),command=star10, fg='White', bg='black')
b10.place(x=450, y=100)
def star11():
    knf.destroy()
    import key1
b11 = Button(knf, text='Key Highights', font=('Elephant', 12),command=star11, fg='White', bg='black')
b11.place(x=650, y=100)
def star12():
    knf.destroy()
    import variants
b12 = Button(knf, text='Variants and Pricing', font=('Elephant', 12),command=star12, fg='White', bg='black')
b12.place(x=840, y=100)
def star13():
    knf.destroy()
    import feature
b13 = Button(knf, text='Features', font=('Elephant', 12),command=star13, fg='White', bg='black')
b13.place(x=1100, y=100)
def star14():
    knf.destroy()
    import Gallery
b14 = Button(knf, text='Gallery', font=('Elephant', 12),command=star14, fg='White', bg='black')
b14.place(x=1250, y=100)

# image Frame 2
frame2 = Frame(knf, bg="black")
frame2.place(x=0, y=150, width=1370, height=592)
image_files = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\scollimage1.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\scrollimage2.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\scrollimage3.jpg"]

image_index = 0
image_label = Label(frame2)
image_label.pack(fill="both", expand=False)

def resize_image(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

def update_image():
    global image_index
    if image_index < len(image_files):
        image = resize_image(image_files[image_index], 1370, 592)
        image_label.configure(image=image)
        image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected.
        image_index += 1
        knf.after(1000, update_image)  # Change image every 3 seconds (3000 milliseconds).
    else:
        image_index = 0
        update_image()

update_image()

knf.mainloop()


