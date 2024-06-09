
import tkinter as tk
from tkvideo import tkvideo
import pygame
from tkinter import *
from PIL import Image,ImageTk


def play_video():
    player.play()

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\168.wav")  # Path to your audio file
    pygame.mixer.music.play()

# Create the Tkinter window
root = tk.Tk()
root.title("MAHENDRA THAR EARTH EDIT OWN")
root.wm_state('zoomed')
root.config(background='black')


# Create a label to display the video
video_label = tk.Label(root)
video_label.place(x=0,y=0)
#video_label.pack()

# Load the video
player = tkvideo("C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\123.mp4", video_label, loop=1, size=(1360, 700))  # Path to your video file

# Play video and audio automatically
play_video()
play_audio()


iconimg=Image.open('C:\\Users\\91995\\PycharmProjects\\pythonProject\\mahendrathar\\iconimage1.jpg')
tkicon=ImageTk.PhotoImage(iconimg)
root.iconphoto(False,tkicon)


root.mainloop()












