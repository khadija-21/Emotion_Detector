from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import numpy
import os
from subprocess import run
import time
import cv2
import tkinter as tk
from PIL import Image, ImageTk 
import keyboard
class Utilisateur:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Utilisateurs")
       

        root.geometry('{}x{}'.format(1300, 700))

        IMAGE_PATH = 'C:/Users/asus/Desktop/Nouveau/Emotion_Detector/angryimg.png'
            
       
        canvas = tk.Canvas(self.root, width=1700, height=700)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((1700, 700), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)


        title = Label( text="Gestion des Utilisateurs",width=30,bg="white",font=("times new roman", 30, "bold"))
        canvas.create_window(320, 10, anchor=tk.NW, window=title)

        def retour():
            root.destroy()
            run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/admin.py")
  
        but = Button(padx=5,pady=5,width=10,bg='white',fg='black',text="Retour",command=retour,font=('Helvetica'),border=0)
        but.place(x=15, y=15)

        #require data variables
        self.num_var = StringVar()
        self.nom_var = StringVar()
        self.prenom_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.age_var = StringVar()
    

        self.search_by = StringVar()
        self.search_txt = StringVar()


        #manage frame left side
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Manage_Frame.place(x=20, y=100, width=450, height=560)

        m_title = Label(Manage_Frame, text="",  bg="white", fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)
       
      
        lbl_num = Label(Manage_Frame, text="Numéro :",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_num.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        txt_num = Entry(Manage_Frame, textvariable=self.num_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_num.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_nom = Label(Manage_Frame, text="Nom :",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_nom.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        txt_nom = Entry(Manage_Frame, textvariable=self.nom_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_nom.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lbl_prenom = Label(Manage_Frame, text="Prénom :",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_prenom.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        txt_prenom= Entry(Manage_Frame, textvariable=self.prenom_var,  font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_prenom.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Genre :",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state="readonly" )
        combo_gender['values'] = ("Homme", "Femme", "autre")
        combo_gender.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        
        lbl_email = Label(Manage_Frame, text="Email :",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_email.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lbl_age = Label(Manage_Frame, text="Age :",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_age.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        txt_age = Entry(Manage_Frame, textvariable=self.age_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_age.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        capturebtn = Button(Manage_Frame, text="Ajouter images", width=30, command=self.capture).grid(row=7, column=1, padx=20, pady=10)
        
        #button frame
        Button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="white")
        Button_Frame.place(x=20, y=450, width=380)


        addbtn = Button(Button_Frame, text="Ajouter", fg="white", bg="blue",width=8, command=self.add_utilisateur).grid(row=0, column=0, padx=5, pady=5)
        updatebtn = Button(Button_Frame, text="Modifier", fg="white", bg="orange",width=8, command=self.update_data).grid(row=0, column=1, padx=5, pady=5)
        deletebtn = Button(Button_Frame, text="Supprimer", fg="white", bg="red",width=8, command=self.delete_data).grid(row=0, column=2, padx=5, pady=5)
        clearbtn = Button(Button_Frame, text="Vider", fg="white", bg="green",width=8, command=self.clear).grid(row=0, column=3, padx=5, pady=5)
        

        #==============Detail Frame========================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=100, width=750, height=580)

        lbl_search = Label(Detail_Frame, width=8, text="Search By",  bg="white", fg="black", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("times new roman", 13), state="readonly" )
        combo_search['values'] = ("num")
        combo_search.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_search.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=8, command=self.search_data).grid(row=1, column=3, padx=5, pady=5)
        showallbtn = Button(Detail_Frame, text="Show All", width=8,  command=self.fetch_data).grid(row=1, column=4, padx=5, pady=5)
        
        #Table Frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=20, y=60, width=700, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame, columns=("num", "nom","prenom","gender", "age", "email"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("num", text="num")
        self.Student_table.heading("nom", text="nom")
        self.Student_table.heading("prenom", text="prenom")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("age", text="age")
        self.Student_table.heading("email", text="email")
        self.Student_table['show']='headings' # removing extra index col at begining

        #setting up widths of cols
        self.Student_table.column("num", width=100)
        self.Student_table.column("nom", width=100)
        self.Student_table.column("prenom", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("age", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.pack(fill=BOTH, expand=1) #fill both is used to fill cols around the frame
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)# this is an event to select row 
        
        self.fetch_data() #to display data in grid

    def add_utilisateur(self):

        if self.nom_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="reconnaissance")
            cur = con.cursor()
            
            cur.execute("insert into utilisateur(num,nom,prenom,age,genre,email) values(%s,%s, %s, %s, %s, %s)",
                 (self.num_var.get(), self.nom_var.get(), self.prenom_var.get(),self.age_var.get(), self.gender_var.get(), 
                 self.email_var.get()  ))


            con.commit()
            self.fetch_data() # this is for if we add any new student then it will call and update the pool
            self.clear()
            con.close()
            messagebox.showinfo("Successfull", "Record has been inserted.")

    def fetch_data(self):
            
        con = mysql.connector.connect(host="localhost", user="root", password="", database="reconnaissance")
        cur = con.cursor()

        cur.execute("select num,nom,prenom,genre,age,email from utilisateur")
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

            con.commit()
        con.close()

    def clear(self):
        self.num_var.set("")
        self.nom_var.set("")
        self.prenom_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.age_var.set("")

    def get_cursor(self, evnt):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']
        self.num_var.set(row[0])
        self.nom_var.set(row[1])
        self.prenom_var.set(row[2])
        self.gender_var.set(row[3])
        self.age_var.set(row[4])
        self.email_var.set(row[5])
        
    def update_data(self):
        if self.nom_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="reconnaissance")
            cur = con.cursor()
            
            cur.execute("UPDATE utilisateur SET nom=%s, prenom=%s, age=%s,genre=%s,  email=%s where num=%s",
                 (self.nom_var.get(), self.prenom_var.get(), self.age_var.get(), self.gender_var.get(), self.email_var.get(), self.num_var.get()  ))


            con.commit()
            self.fetch_data() # this is for if we add any new student then it will call and update the pool
            self.clear()
            con.close()
            messagebox.showinfo("successfull", "Record has been updated.")

    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="reconnaissance")
        cur = con.cursor()
        cur.execute("DELETE FROM utilisateur WHERE num="+self.num_var.get()+" ")
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("successfull", "Record has been deleted.")

    
    def search_data(self):

        con = mysql.connector.connect(host="localhost", user="root", password="", database="reconnaissance")
        cur = con.cursor()

        cur.execute("SELECT * FROM utilisateur WHERE num ="+self.search_txt.get()+" ")
        
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

            con.commit()
        con.close()
    def capture(self):
            cap=cv2.VideoCapture(0)
            count = 0
            repertoire = "C:/Users/asus/Desktop/Nouveau/Emotion_Detector/images/"+self.prenom_var.get()
            if not os.path.exists(repertoire):
                os.makedirs(repertoire)
            
            while True:
                ret,test_img=cap.read()
                if not ret :
                    continue
                
                cv2.imwrite("C:/Users/asus/Desktop/Nouveau/Emotion_Detector/images/"+self.prenom_var.get()+"/"+self.prenom_var.get()+"%d.jpg" % count, test_img)     # save frame as JPG file
                count += 1
                resized_img = cv2.resize(test_img, (900, 600))
                cv2.imshow('face detection  ',resized_img)
                
                #wait until 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    #cap.release()
                    cv2.destroyAllWindows
                    repertoire ="C:/Users/asus/Desktop/Nouveau/Emotion_Detector/trainner.yml"
                    if  os.path.exists(repertoire):
                        os.remove(repertoire)
                    messagebox.showwarning("Warning", "wait to refresh")
                    run("python C:/Users/asus/Desktop/Nouveau/Emotion_Detector/face.py")
                    messagebox.showinfo("Title", "refresh done")
                    break



root = Tk()
obj = Utilisateur(root)
root.mainloop()



