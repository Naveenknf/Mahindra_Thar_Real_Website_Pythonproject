from tkinter import *
import customtkinter
from PIL import Image, ImageTk

# Create the Tkinter window
knf = customtkinter.CTk()
knf.title('MAHENDRA THAR GALLERY')
knf.wm_state("zoomed")
knf.iconbitmap('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')

my_frame = customtkinter.CTkScrollableFrame(knf,
                                            orientation="vertical",
                                            width=1330,
                                            height=670,
                                            fg_color="#202020",
                                            scrollbar_fg_color="#202020",
                                            scrollbar_button_hover_color="blue",
                                            corner_radius=20,
                                            )
my_frame.grid(row=1, column=0)


# Define paths to your images
image_paths = [
    'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery1.png',
    'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery2.png',
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery3.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery4.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery5.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery6.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery7.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery8.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery10.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery11.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery12.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery13.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery14.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery15.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery16.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery17.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\gallery19.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\galllery20.png"
    # Add more image paths as needed
]

# Load and display each image
for i, img_path in enumerate(image_paths):
    img = Image.open(img_path)
    img = img.resize((1320, 550))  # Adjust the size as needed
    tk_img = ImageTk.PhotoImage(img)
    img_label = Label(my_frame, image=tk_img, bg='black')
    img_label.image = tk_img
    img_label.grid(row=i, column=0,padx=0, pady=30)

l=Label(my_frame,text='Mahendra Thar Gallery',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=0,y=0)

def star1():
    knf.destroy()
    import windowopen
b1 = Button(my_frame, text='Back', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1230, y=11020)

knf.mainloop()