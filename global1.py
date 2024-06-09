#global market code

from tkinter import *
from PIL import Image,ImageTk
knf1=Tk()
knf1.wm_state('zoomed')

knf1.title('MAHINDRA THAR GLOBAL ')

knf1.config(bg='black')
iconimg=Image.open('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')
tkicon=ImageTk.PhotoImage(iconimg)
knf1.iconphoto(False,tkicon)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendrariselogo.jpg'
img = Image.open(imgpath)
img = img.resize((150, 50))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf1, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=20, y=10)

l=Label(knf1,text='Vehicles',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=280,y=30)

l=Label(knf1,text='Buy',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=380,y=30)

l=Label(knf1,text='Service',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=30)

l=Label(knf1,text='Experience',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=545,y=30)

l=Label(knf1,text='Global Markets',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=675,y=30)

l=Label(knf1,text='Test Drive',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=950,y=30)

l=Label(knf1,text='Locate Us',font=('Calibri',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1070,y=30)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\searchimage1.jpg'
img = Image.open(imgpath)
img = img.resize((30, 30))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf1, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1200, y=30)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\loginimage1.jpg'
img = Image.open(imgpath)
img = img.resize((30, 30))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf1, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1280, y=30)

# image Frame 2
frame2 = Frame(knf1, bg="black")
frame2.place(x=0, y=80, width=1370, height=620)
image_files = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\global1.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\global2.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\global3.jpg"]

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
        image = resize_image(image_files[image_index], 1370, 620)
        image_label.configure(image=image)
        image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected.
        image_index += 1
        knf1.after(2000, update_image)  # Change image every 3 seconds (3000 milliseconds).
    else:
        image_index = 0
        update_image()

update_image()

def star1():
    knf1.destroy()
    import explore
b1 = Button(knf1, text='>', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1330, y=30)

knf1.mainloop()