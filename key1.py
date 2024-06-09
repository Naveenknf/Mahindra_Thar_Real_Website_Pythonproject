from tkinter import *
import customtkinter
from PIL import Image, ImageTk

# Set appearance mode and color theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Create the Tkinter window
knf = customtkinter.CTk()
knf.title('MAHENDRA THAR KEY HIGHTLIGHT')
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

# List of image paths for the first set of images
image_files1 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\key1.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\key2.jpg",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\key3.jpg"
]

# List of image paths for the second set of images
image_files2 = [
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\venv\\b4.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\venv\\b5.png",
    "C:\\Users\\91995\\PycharmProjects\\pythonProject\\venv\\b6.png"
]

# Function to resize image
def resize_image(img_path, width, height):
    img = Image.open(img_path)
    img_resized = img.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(img_resized)

# Function to create labels and display images for a given frame and list of image paths
def display_images(frame, image_files):
    image_labels = []
    for image_file in image_files:
        image = resize_image(image_file, 650, 300)
        image_label = Label(frame, image=image)
        image_label.image = image
        image_labels.append(image_label)
    return image_labels

# Create labels to display images in the first frame
image_labels1 = display_images(my_frame1, image_files1)

# Create labels to display images in the second frame
image_labels2 = display_images(my_frame1, image_files1)

# Function to update image position for the first frame
def update_image_position1(index=0):
    # Hide previous image
    if index > 0:
        image_labels1[index - 1].grid_remove()
    else:
        image_labels1[-1].grid_remove()

    # Show current image
    image_labels1[index].grid(row=index, column=1, padx=0, pady=20)

    # Schedule the next image change after 1000 milliseconds (1 second)
    knf.after(1000, update_image_position1, (index + 1) % len(image_labels1))

# Function to update image position for the second frame
def update_image_position2(index=0):
    # Hide previous image
    if index > 0:
        image_labels2[index - 1].grid_remove()
    else:
        image_labels2[-1].grid_remove()

    # Show current image
    image_labels2[index].grid(row=1, column=2, padx=0, pady=20)

    # Schedule the next image change after 1000 milliseconds (1 second)
    knf.after(1000, update_image_position2, (index + 1) % len(image_labels2))

# Start updating the image position for the first frame
update_image_position1()

# Start updating the image position for the second frame
update_image_position2()

def star1():
    knf.destroy()
    import variants
b1 = Button(knf, text='Key Highlight', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=25, y=5)

# Run the Tkinter event loop
knf.mainloop()
