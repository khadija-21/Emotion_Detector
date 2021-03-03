

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

IMAGE_PATH = 'C:/Users/asus/Desktop/Nouveau/Emotion_Detector/login1.png'
    
root = tk.Tk()
root.geometry('{}x{}'.format(1300, 700))

canvas = tk.Canvas(root, width=1300, height=700)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1300, 700), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

def emotion():
    messagebox.showwarning("Warning", "wait to refresh")
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/emotions.py --mode display")
def capture():
    root.destroy()
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/capture.py")
def face():
    repertoire ="C:/Users/asus/Desktop/Nouveau/Emotion_Detector/trainner.yml"
    if  os.path.exists(repertoire):
        os.remove(repertoire)
    messagebox.showwarning("Warning", "wait to refresh")
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/face.py")
    messagebox.showinfo("Title", "refresh done")
def gestion():
    root.destroy()
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/gestion.py")

def retour():
    root.destroy()
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/authentification.py")
def face():
    repertoire ="C:/Users/asus/Desktop/Nouveau/Emotion_Detector/trainner.yml"
    if  os.path.exists(repertoire):
        os.remove(repertoire)
    messagebox.showwarning("Warning", "wait to refresh")
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/face.py")
    messagebox.showinfo("Title", "refresh done")

imgfile = 'C:/Users/asus/Desktop/Nouveau/Emotion_Detector/logo.png' ## chemin d'accès à l'image  
monimage = Image.open(imgfile)
filename = ImageTk.PhotoImage(monimage) 
background_label = Label(image=filename)
canvas.create_window(500, 50, anchor=tk.NW, window=background_label)

but = Button(padx=5,pady=5,width=10,bg='white',fg='black',text="log out",command=retour,font=('Helvetica'),border=0)
canvas.create_window(10, 10, anchor=tk.NW, window=but)

label = Label(text="Bienvenue Dans l'espace ",font=('Times 35 bold'),bg='white')
label2 = Label(text="Administrateur",font=('Times 35 bold'),bg='white')
canvas.create_window(400, 150, anchor=tk.NW, window=label)
canvas.create_window(490, 230, anchor=tk.NW, window=label2)


but2 = Button(padx=5,pady=5,width=30,height=2,bg='orange',fg='white',text="Detection d'émotion",command=emotion,font=('Helvetica'),border=0)
canvas.create_window(360, 350, anchor=tk.NW, window=but2)

but3 = Button(padx=5,pady=5,width=30,height=2,bg='blue',fg='white',text="Refresh",command=face,font=('Helvetica'),border=0)
canvas.create_window(500, 450, anchor=tk.NW, window=but3)

but4 = Button(padx=5,pady=5,width=30,height=2,bg='#024604',fg='white',text="Gestion des Utilisateurs",command=gestion,font=('Helvetica'),border=0)
canvas.create_window(650, 550, anchor=tk.NW, window=but4)


root.mainloop()