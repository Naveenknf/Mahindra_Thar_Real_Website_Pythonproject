from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

knf = customtkinter.CTk()
knf.title('MAHENDRA THAR CAR_COLLECTIONS')
knf.wm_state("zoomed")
knf.iconbitmap('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')


my_frame = customtkinter.CTkScrollableFrame(knf,
                                            orientation="vertical",
                                            width=1330,
                                            height=670,
                                            fg_color="black",
                                            scrollbar_fg_color="#202020",
                                            scrollbar_button_hover_color="blue",
                                            corner_radius=20,
                                            )
my_frame.grid(row=1, column=0)

l=Label(my_frame,text='Mahendra car Collections',font=('Calibri',25),bg='black',fg='red')
#x axis,y axis place
l.place(x=500,y=30)

l=Label(my_frame,text='Sports Utility Vehicle',font=('Elephant',18),bg='black',fg='green')
#x axis,y axis place
l.place(x=20,y=100)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection1.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=0,column=0,padx=10, pady=150)

l=Label(my_frame,text='Scarpio-N',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=80,y=330)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection2.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=0,column=1,padx=20, pady=30)

l=Label(my_frame,text='XUV700',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=460,y=330)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection3.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=0,column=2,padx=20, pady=30)

l=Label(my_frame,text='Thar',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=800,y=330)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection4.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=0,column=3,padx=20, pady=30)

l=Label(my_frame,text='XUV300',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1150,y=330)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection5.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=1,column=0,padx=0, pady=30)

l=Label(my_frame,text='Bolero Neo',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=80,y=700)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection6.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=1,column=1,padx=0, pady=0)

l=Label(my_frame,text='Bolero',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=700)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection7.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=1,column=2,padx=0, pady=0)

l=Label(my_frame,text='Scorpio Classic',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=750,y=700)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection8.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=1,column=3,padx=0, pady=0)

l=Label(my_frame,text='KUV100 NXT',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1120,y=700)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection10.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=2,column=0,padx=20, pady=80)

l=Label(my_frame,text='XUV400',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=80,y=990)

l=Label(my_frame,text='Pik-Ups',font=('Elephant',18),bg='black',fg='green')
#x axis,y axis place
l.place(x=20,y=1050)


imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection11.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=3,column=0,padx=20, pady=30)

l=Label(my_frame,text='Maxx Pik-Up City',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=1290)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection12.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=3,column=1,padx=20, pady=30)

l=Label(my_frame,text='Maxx Pik-Up HD',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=400,y=1290)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection13.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=3,column=2,padx=20, pady=30)

l=Label(my_frame,text='Bolero Pik-Up',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=770,y=1290)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection14.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=3,column=3,padx=20, pady=40)

l=Label(my_frame,text='Bolero Comper',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1130,y=1290)

l=Label(my_frame,text='Small Commercial',font=('Elephant',20),bg='black',fg='green')
#x axis,y axis place
l.place(x=20,y=1370)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection15.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=4,column=0,padx=20, pady=40)

l=Label(my_frame,text='Alfa DX',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=120,y=1620)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection16.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=4,column=1,padx=20, pady=100)

l=Label(my_frame,text='Alfa DX CNG',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=1620)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection17.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=4,column=2,padx=20, pady=40)

l=Label(my_frame,text='Alfa Plus',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=800,y=1620)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection18.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=4,column=3,padx=20, pady=50)

l=Label(my_frame,text='Alfa Plus CNG',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1130,y=1620)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection19.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=5,column=0,padx=20, pady=40)

l=Label(my_frame,text='Jeeto Strong',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=50,y=1940)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection20.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=5,column=1,padx=20, pady=40)

l=Label(my_frame,text='Super Maxi Truck',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=420,y=1940)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection21.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=5,column=2,padx=20, pady=40)

l=Label(my_frame,text='Super Mini Truck',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=750,y=1940)

l=Label(my_frame,text='Electric',font=('Elephant',20),bg='black',fg='green')
#x axis,y axis place
l.place(x=20,y=2030)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection22.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=6,column=0,padx=20, pady=100)

l=Label(my_frame,text='Zor Grand',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=100,y=2270)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection23.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=6,column=1,padx=20, pady=40)

l=Label(my_frame,text='Treo Auto',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=2270)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection24.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=6,column=2,padx=20, pady=40)


l=Label(my_frame,text='Treo Zor',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=800,y=2270)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection25.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=6,column=3,padx=20, pady=40)

l=Label(my_frame,text='Treo Yaari',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1150,y=2270)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection26.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=7,column=0,padx=20, pady=40)

l=Label(my_frame,text='e-Alfa Super',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=100,y=2600)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection27.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=7,column=1,padx=20, pady=40)

l=Label(my_frame,text='e-Alfa Cargo',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=2600)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection28.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=7,column=2,padx=20, pady=40)

l=Label(my_frame,text='E-Verito',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=810,y=2600)

l=Label(my_frame,text='Trucks',font=('Elephant',20),bg='black',fg='green')
#x axis,y axis place
l.place(x=20,y=2660)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection29.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=8,column=0,padx=20, pady=100)

l=Label(my_frame,text='Blazo Haulage',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=80,y=2910)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection30.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=8,column=1,padx=20, pady=40)

l=Label(my_frame,text='Blazo Tipper',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=450,y=2910)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection31.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=8,column=2,padx=20, pady=40)

l=Label(my_frame,text='Blazo Tractor Trailer',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=750,y=2910)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection32.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=8,column=3,padx=20, pady=40)

l=Label(my_frame,text='Furio',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=1150,y=2910)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection33.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=9,column=0,padx=20, pady=40)

l=Label(my_frame,text='jayo',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=120,y=3210)

l=Label(my_frame,text='Buses',font=('Elephant',20),bg='black',fg='green')
#x axis,y axis place
l.place(x=20,y=3270)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection34.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=10,column=0,padx=20, pady=40)

l=Label(my_frame,text='Cruzio',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=120,y=3500)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\car_collection35.jpg'
img = Image.open(imgpath)
img = img.resize((300, 180))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.grid(row=10,column=1,padx=20, pady=40)

l=Label(my_frame,text='Cruzio Grando',font=('Elephant',15),bg='black',fg='white')
#x axis,y axis place
l.place(x=420,y=3500)

def star1():
    knf.destroy()
    import buy
b1 = Button(my_frame, text='After', font=('Elephant', 12),command=star1, fg='White', bg='black', )
b1.place(x=1200, y=3450)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\mahendralogo.jpg'
img = Image.open(imgpath)
img = img.resize((120, 80))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=30, y=10)

imgpath = 'C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\3barcode.png'
img = Image.open(imgpath)
img = img.resize((100, 80))
tk_img = ImageTk.PhotoImage(img)
img_label = Label(my_frame, image=tk_img, bg='black')
img_label.image = tk_img
img_label.place(x=1200, y=20)


knf.mainloop()
