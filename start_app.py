
import numpy
from tkinter import *
import os
from subprocess import run
import time
import cv2
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk 
from tkinter import messagebox

IMAGE_PATH = 'C:/Users/asus/Desktop/Nouveau/Emotion_Detector/1.jpg'

root = tk.Tk()
root.geometry('{}x{}'.format(1300, 700))

canvas = tk.Canvas(root, width=1300, height=700)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1300, 700), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

def Admin():
    root.destroy()
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/authentification.py")

def utilisateur():
    messagebox.showwarning("Warning", "wait to refresh")
    run("python python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/emotions.py --mode display")


imgfile = 'C:/Users/asus/Desktop/Nouveau/Emotion_Detector/logo.png' ## chemin d'accès à l'image  
monimage = Image.open(imgfile)
filename = ImageTk.PhotoImage(monimage) 
background_label = Label(image=filename)
canvas.create_window(20, 20, anchor=tk.NW, window=background_label)

but1 = Button(padx=5,pady=5,width=20,height=2,bg='white',fg='#212121',relief=GROOVE,command=Admin,text='Administrateur',font=('Helvetica'),border=5)
canvas.create_window(300, 270, anchor=tk.NW, window=but1)


but3 = Button(padx=5,pady=5,width=20,height=2,bg='black',fg='white',relief=GROOVE,command=utilisateur,text='utilisateur',font=('Helvetica '),border=5)
canvas.create_window(750, 270, anchor=tk.NW, window=but3)

root.mainloop()