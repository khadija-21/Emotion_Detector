from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import *
import mysql.connector
from PIL import Image, ImageTk 
import time
import os
from subprocess import run
class Personne:
  
  def __init__(self, num,nom, prenom, age ,genre,pwd,email):
    self.nom = nom
    self.prenom = prenom
    self.date_naissance = date_naissance

class Utilisateur(Personne):
  
  def __init__(self, num,nom, prenom, age ,genre,pwd,email):
        Personne.__init__(self,num,nom, prenom, age ,genre,pwd,email)

class Admin(Personne):
  
  def __init__(self,num,nom, prenom, age ,genre,pwd,email):
        self.isAdmin= "admin"
        Personne.__init__(self,num,nom, prenom, age ,genre,pwd,email) 
           

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="reconnaissance")
mycur = db.cursor()

def logg_destroy():
    logg.destroy()
    root2.destroy()
def fail_destroy():
    fail.destroy()

def logged():
    root.destroy()
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/admin.py")


def failed():
    global fail
    fail = Toplevel(root)
    fail.title("Invalid")
    fail.geometry("400x150")

    Label(fail, text="Email ou mot de passe sont incorrectes", fg="red", font=('Times 15 bold')).place(x=10,y=50)
    Button(fail, text="Ok", width=9, height=1, command=fail_destroy).place(x=10,y=100)


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from utilisateur where email = %s and pwd = %s and isAdmin='admin'"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def retour():
    root.destroy()
    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/start_app.py")


def main_screen():
    global root

    IMAGE_PATH = 'C:/Users/asus/Desktop/Nouveau/Emotion_Detector/b.png'
    
    root = tk.Tk()
    root.geometry('{}x{}'.format(1300, 700))

    canvas = tk.Canvas(root, width=1300, height=700)
    canvas.pack()

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1300, 700), Image.ANTIALIAS))
    canvas.background = img  
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

    global username_varify
    global password_varify
    label1 = Label(text="Se connecter", font="Helvetica 25", bg="white", fg="black")
    canvas.create_window(550, 150, anchor=tk.NW, window=label1)
    username_varify = StringVar()
    password_varify = StringVar()


    label2 = Label(text="Email :", bg="white",font="20")
    canvas.create_window(490, 250, anchor=tk.NW, window=label2)
    entry1 = Entry(textvariable=username_varify,bd=1, bg="#F7F7F7",relief=GROOVE)
    canvas.create_window(590, 250, anchor=tk.NW, window=entry1)

    label3 = Label(text="Password :", bg="white",font="20")
    canvas.create_window(490, 330, anchor=tk.NW, window=label3)
    entry2 = Entry(textvariable=password_varify, show="*",bd=1, bg="#F7F7F7",relief=GROOVE)
    canvas.create_window(590, 330, anchor=tk.NW, window=entry2)


    but = Button(padx=5,pady=5,width=10,bg='white',fg='black',text="Retour",command=retour,font=('Helvetica'),border=0)
    canvas.create_window(10, 10, anchor=tk.NW, window=but)

    but = Button(padx=5,pady=5,width=20,bg='#1E1E1E',fg='white',text="Connexion",command=login_varify,font=('Helvetica'),border=0)
    canvas.create_window(550, 400, anchor=tk.NW, window=but)

main_screen()
root.mainloop()