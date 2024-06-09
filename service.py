from tkinter import *
from PIL import Image, ImageTk

# Function to change the image forward
def next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(images)
    show_image(img_label)  # Pass img_label to show_image()

# Function to change the image backward
def prev_image():
    global current_image_index
    current_image_index = (current_image_index - 1) % len(images)
    show_image(img_label)  # Pass img_label to show_image()

# Function to display the current image
def show_image(label):  # Accept img_label as an argument
    img = Image.open(images[current_image_index])
    img = img.resize((1200, 500), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)
    label.config(image=tk_img)
    label.image = tk_img

# List of image paths
images = ['C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service1.png',
          'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service2.png',
          'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service3.png',
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service4.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service5.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service6.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service7.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service8.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service9.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service10.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service11.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service12.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service13.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service14.png",
          "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\service15.png"
          ]

# Initialize current image index
current_image_index = 0

# Create the Tkinter window
knf = Tk()  # Use Tk() from tkinter
knf.title('MAHENDRA THAR SERVICE')
knf.wm_state("zoomed")
knf.config(bg="black")

knf.iconbitmap('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendralogo.jpg'
img = Image.open(imgpath)
img = img.resize((150, 110))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=0, y=10)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\3barcode.png'
img = Image.open(imgpath)
img = img.resize((100, 80))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(knf, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1250, y=20)

# Create label to display image
img_label = Label(knf)
#img_label.pack()
img_label.place(x=90,y=150)

# Load initial image
show_image(img_label)  # Pass img_label to show_image()

# Create button to change image forward
next_button = Button(knf, text=">", command=next_image)
next_button.place(x=1320, y=350)

# Create button to change image backward
prev_button = Button(knf, text="<", command=prev_image,)
prev_button.place(x=30, y=350)


l=Label(knf,text='New Mahendra Thar',font=('Calibri',25),bg='black',fg='white')
#x axis,y axis place
l.place(x=200,y=40)

l=Label(knf,text='Service & Fecilities',font=('Calibri',20),bg='black',fg='white')
#x axis,y axis place
l.place(x=200,y=90)


def star1():
    knf.destroy()
    import experience
b1 = Button(knf, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1290, y=45)


# Run the Tkinter event loop
knf.mainloop()
