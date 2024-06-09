
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

# Set appearance mode and color theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Create the Tkinter window
knf = customtkinter.CTk()
knf.title('MAHENDRA THAR FEATURE')
knf.wm_state("zoomed")
knf.iconbitmap('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')

# Create the first scrollable frame
my_frame1 = customtkinter.CTkScrollableFrame(knf,
                                            orientation="vertical",
                                            width=1330,
                                            height=670,
                                            fg_color="black",
                                            scrollbar_fg_color="#202020",
                                            scrollbar_button_hover_color="blue",
                                            corner_radius=20,
                                            )
my_frame1.grid(row=1, column=0)

l=Label(my_frame1,text='FEATURES & SPECIFICATIONS',font=('Elephant',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=0)

l=Label(my_frame1,text='Design',font=('Elephant',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=50)

# List of image paths for the first set of images
image_files1 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature1.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature2.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature3.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature4.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature5.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature6.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature7.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature8.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature9.jpg"
]

# Function to resize image
def resize_image1(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

# Function to create labels and display images for a given frame and list of image paths
def display_images1(frame, image_files):
    image_labels = []
    for image_file in image_files:
        image = resize_image1(image_file, 1300, 600)
        image_label = Label(frame, image=image)
        image_label.image = image
        image_labels.append(image_label)
    return image_labels

# Create labels to display images in the first frame
image_labels1 = display_images1(my_frame1, image_files1)


# Function to update image position for the first frame
def update_image_position1(index=0):
    # Hide previous image
    if index > 0:
        image_labels1[index - 1].grid_remove()
    else:
        image_labels1[-1].grid_remove()

    # Show current image
    image_labels1[index].grid(row=0, column=1, padx=10, pady=100)

    # Schedule the next image change after 1000 milliseconds (1 second)
    knf.after(2000, update_image_position1, (index + 1) % len(image_labels1))

# Start updating the image position for the first frame
update_image_position1()


#position 2

l=Label(my_frame1,text='Performance and Capability',font=('Elephant',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=780)

# image Frame 2
frame2 = Frame(my_frame1, bg="black")
frame2.grid(row=1, column=1, padx=10, pady=20)  # Adjust the padding here
image_files2 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature10.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature11.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature12.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature14.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature15.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature16.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature17.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature18.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature19.jpg"
]

image_index2 = 0
image_label2 = Label(frame2)
image_label2.pack(fill="both", expand=False)

def resize_image2(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

def update_image2():
    global image_index2
    if image_index2 < len(image_files2):
        image = resize_image2(image_files2[image_index2], 1300, 600)
        image_label2.configure(image=image)
        image_label2.image = image
        image_index2 += 1
        knf.after(2000, update_image2)
    else:
        image_index2 = 0
        update_image2()

update_image2()



#position 3

l=Label(my_frame1,text='Comfort & Convenience',font=('Elephant',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=1500)

# image Frame 3

frame3 = Frame(my_frame1, bg="black")
frame3.grid(row=2, column=1, padx=10, pady=100)
image_files3 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature20.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature21.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature22.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature23.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature24.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature25.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature27.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature28.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature29.jpg"
]

image_index3 = 0
image_label3 = Label(frame3)
image_label3.pack(fill="both", expand=False)

def resize_image3(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

def update_image3():
    global image_index3
    if image_index3 < len(image_files3):
        image = resize_image3(image_files3[image_index3], 1300, 600)
        image_label3.configure(image=image)
        image_label3.image = image
        image_index3 += 1
        knf.after(2000, update_image3)
    else:
        image_index3 = 0
        update_image3()

update_image3()


#position 4

l=Label(my_frame1,text='Technology',font=('Elephant',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=2230)

# image Frame 4
frame4 = Frame(my_frame1, bg="black")
frame4.grid(row=3, column=1, padx=10, pady=20)
image_files4 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature30.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature31.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature32.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature41.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature33.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature40.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature34.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature35.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature36.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature37.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature38.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature39.jpg"
]

image_index4 = 0
image_label4 = Label(frame4)
image_label4.pack(fill="both", expand=False)

def resize_image4(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

def update_image4():
    global image_index4
    if image_index4 < len(image_files4):
        image = resize_image4(image_files4[image_index4], 1300, 600)
        image_label4.configure(image=image)
        image_label4.image = image
        image_index4 += 1
        knf.after(2000, update_image4)
    else:
        image_index4 = 0
        update_image4()

update_image4()


#position 5

l=Label(my_frame1,text='Safety',font=('Elephant',18),bg='black',fg='white')
#x axis,y axis place
l.place(x=10,y=2950)


# image Frame 5
frame5 = Frame(my_frame1, bg="black")
frame5.grid(row=4, column=1, padx=10, pady=100)
image_files5 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature42.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature43.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature44.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature45.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature46.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature47.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\feature48.jpg"
]

image_index5 = 0
image_label5 = Label(frame5)
image_label5.pack(fill="both", expand=False)

def resize_image5(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

def update_image5():
    global image_index5
    if image_index5 < len(image_files5):
        image = resize_image5(image_files5[image_index5], 1300, 600)
        image_label5.configure(image=image)
        image_label5.image = image
        image_index5 += 1
        knf.after(2000, update_image5)
    else:
        image_index5 = 0
        update_image5()

update_image5()


def star1():
    my_frame1.destroy()
    #import
b1 = Button(my_frame1, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1250, y=3650)

# Run the Tkinter event loop
knf.mainloop()
