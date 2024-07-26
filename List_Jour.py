from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as mb
import sqlite3

class List_Jour:
    def __init__(self,mast):
        self.master = mast
        self.master.title("Liste jour et rendez-vous")
        ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        self.master.configure(background="#BCD2EE")
        
        self.Nom = ctk.CTkLabel(self.master,text='Les jours',text_color="white", font=('Helvetica',50,'bold'))
        self.Nom.place(x=160,y=20 )

        self.rechercher_entry = ctk.CTkEntry(self.master,  font=('Helvetica',18,'bold'), width=200, height=30)
        self.rechercher_entry.place(x=75,y=140 )
        self.rechercher_button = ctk.CTkButton(self.master, text='Rechercher', command=self.rechercher_ligne_par_valeur,  font=('Helvetica',15,'bold'), height=30, width=100)
        self.rechercher_button.place(x=280,y=140 )
        self.voir_button = ctk.CTkButton(self.master, text='Voir', command=self.voir,  font=('Helvetica',15,'bold'), height=30, width=100)
        self.voir_button.place(x=390,y=140 )
        

        self.scrollbar = Scrollbar(self.master, orient = VERTICAL)

        style1 = ttk.Style()
        style1.layout('my.treeview.layout',
                    [('Header', {'sticky':'nswe'})] +
                    [('Separator', {'sticky':'ew'})] +
                    [('Item..focus', {'sticky':'nswe'})] +
                    [('Item', {'sticky':'nswe'})]
                    )
        style1.configure("Treeview",  background="#00C957")
        style1.configure("Treeview.Item", font=("Helvetica", 12))
        style1.configure("Treeview.Heading",  font=("tahoma", 10))

        

        self.table = ttk.Treeview(self.master, style='Treeview.Heading', column= ("ID","Nom","Prenom","Age","Motif de consultation","Jour","Rendez-vous","Montant total","Versement","Reste","Num de tel"), show='headings', height=17 , yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=475,y=180, height=388)
        self.scrollbar.config(command=self.table.yview())       
        self.table.place(x=75,y=180, width=400)
         

        self.table.heading("ID",text="ID")
        self.table.heading("Nom",text="Nom")
        self.table.heading("Prenom",text="Prenom")
        self.table.heading("Age",text="Age")
        self.table.heading("Motif de consultation",text="Motif de consultation")
        self.table.heading("Jour",text="Jour")
        self.table.heading("Rendez-vous",text="Rendez-vous")
        self.table.heading("Montant total",text="Montant total")
        self.table.heading("Versement",text="Versement")
        self.table.heading("Reste",text="Reste")
        self.table.heading("Num de tel",text="Num de tel")
       
        self.table.column("ID", anchor=W, width=5)
        self.table.column("Nom", anchor=W, width=5)
        self.table.column("Prenom", anchor=W, width=6)
        self.table.column("Age", anchor=W, width=6)
        self.table.column("Motif de consultation", anchor=W, width=6)
        self.table.column("Jour", anchor=W, width=6)
        self.table.column("Rendez-vous", anchor=W, width=6)
        self.table.column("Montant total", anchor=W, width=6)
        self.table.column("Versement", anchor=W, width=6)
        self.table.column("Reste", anchor=W, width=6)
        self.table.column("Num de tel", anchor=W, width=6)


        self.Nom2 = ctk.CTkLabel(self.master,text='Les rendez-vous',text_color="white", font=('Helvetica',50,'bold'))
        self.Nom2.place(x=530,y=20 )

        self.rechercher2_entry = ctk.CTkEntry(self.master,  font=('Helvetica',18,'bold'), width=200, height=30)
        self.rechercher2_entry.place(x=525,y=140 )
        self.rechercher2_button = ctk.CTkButton(self.master, text='Rechercher', command=self.rechercher_ligne_par_valeur2,  font=('Helvetica',15,'bold'), height=30, width=100)
        self.rechercher2_button.place(x=730,y=140 )
        self.voir2_button = ctk.CTkButton(self.master, text='Voir', command=self.voir2,  font=('Helvetica',15,'bold'), height=30, width=100)
        self.voir2_button.place(x=840,y=140 )

        self.scrollbar2 = Scrollbar(self.master, orient = VERTICAL)


    
        self.table2 = ttk.Treeview(self.master, style='Treeview.Heading', column= ("ID","Nom","Prenom","Age","Motif de consultation","Jour","Rendez-vous","Montant total","Versement","Reste","Num de tel"), show='headings', height=17 , yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.place(x=925,y=180, height=388)
        self.scrollbar2.config(command=self.table2.yview())       
        self.table2.place(x=525,y=180, width=400)
         

        self.table2.heading("ID",text="ID")
        self.table2.heading("Nom",text="Nom")
        self.table2.heading("Prenom",text="Prenom")
        self.table2.heading("Age",text="Age")
        self.table2.heading("Motif de consultation",text="Motif de consultation")
        self.table2.heading("Jour",text="Jour")
        self.table2.heading("Rendez-vous",text="Rendez-vous")
        self.table2.heading("Montant total",text="Montant total")
        self.table2.heading("Versement",text="Versement")
        self.table2.heading("Reste",text="Reste")
        self.table2.heading("Num de tel",text="Num de tel")
       
        self.table2.column("ID", anchor=W, width=5)
        self.table2.column("Nom", anchor=W, width=5)
        self.table2.column("Prenom", anchor=W, width=6)
        self.table2.column("Age", anchor=W, width=6)
        self.table2.column("Motif de consultation", anchor=W, width=6)
        self.table2.column("Jour", anchor=W, width=6)
        self.table2.column("Rendez-vous", anchor=W, width=6)
        self.table2.column("Montant total", anchor=W, width=6)
        self.table2.column("Versement", anchor=W, width=6)
        self.table2.column("Reste", anchor=W, width=6)
        self.table2.column("Num de tel", anchor=W, width=6)

        self.lire_table()
        self.lire_table2()




    def lire_table(self):
          
          # Connect to SQLite database
          conn = sqlite3.connect("data_base.db")
          cursor = conn.cursor()

          # Fetch data from SQLite
          #req = "SELECT Nom, Prenom, Age, Motif, Jour, Rendez_vous, Montant_total, Versement, Reste, Num_de_tel FROM Patient" 
          cursor.execute("SELECT * FROM Patient")
          data = cursor.fetchall()

  
          self.table.delete(*self.table.get_children())

          counter = 1  # Start from 1 or another appropriate value
          for i in data:
            self.table.insert('', 'end', iid=str(counter), values=i)
            counter += 1
 
          conn.close()  


    def lire_table2(self):
          
          # Connect to SQLite database
          conn = sqlite3.connect("data_base.db")
          cursor = conn.cursor()

          # Fetch data from SQLite
          #req = "SELECT Nom, Prenom, Age, Motif, Jour, Rendez_vous, Montant_total, Versement, Reste, Num_de_tel FROM Patient" 
          cursor.execute("SELECT * FROM Patient")
          data = cursor.fetchall()

  
          self.table2.delete(*self.table2.get_children())

          counter = 1  # Start from 1 or another appropriate value
          for i in data:
            self.table2.insert('', 'end', iid=str(counter), values=i)
            counter += 1
 
          conn.close()  



    def rechercher_ligne_par_valeur(self):

        rechercher_entry = self.rechercher_entry.get()
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()

    # Remplacez 'nom_de_la_table' par le nom réel de votre table et 'nom_colonne' par le nom de la colonne dans laquelle vous voulez rechercher.
        req = (f"SELECT * FROM Patient WHERE Jour LIKE ?")
        cursor.execute(req, ('%' + rechercher_entry + '%',))

    # Utilisation du caractère joker '%' pour rechercher partiellement la valeur
        resultats = cursor.fetchall()
        print(resultats)
        if  not resultats: 
    
            mb.showerror("Erreur","Il n'existe aucun patient ", parent=self.master) 
            print(resultats)  
        
        else :

            # Effacer les anciennes entrées dans le tableau
            for row in self.table.get_children():
                self.table.delete(row)

            # Afficher les résultats dans le tableau
            for resultat in resultats:
                self.table.insert("", "end", values=resultat)

        conn.commit()
        conn.close() 

    

    def rechercher_ligne_par_valeur2(self):

        rechercher_entry2 = self.rechercher2_entry.get()
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()

    # Remplacez 'nom_de_la_table' par le nom réel de votre table et 'nom_colonne' par le nom de la colonne dans laquelle vous voulez rechercher.
        req = (f"SELECT * FROM Patient WHERE Rendez_vous LIKE ?")
        cursor.execute(req, ('%' + rechercher_entry2 + '%',))

    # Utilisation du caractère joker '%' pour rechercher partiellement la valeur
        resultats = cursor.fetchall()
        print(resultats)
        if  not resultats: 
    
            mb.showerror("Erreur","Il n'existe aucun patient ", parent=self.master) 
            print(resultats)  
        
        else :

            # Effacer les anciennes entrées dans le tableau
            for row in self.table2.get_children():
                self.table2.delete(row)

            # Afficher les résultats dans le tableau
            for resultat in resultats:
                self.table2.insert("", "end", values=resultat)

        conn.commit()
        conn.close() 




    def voir(self):
        # Call your read function to refresh the table with all data
        self.lire_table()

        # Optionally, you can clear the search entry if you have one
        self.rechercher_entry.delete(0, 'end')

    def voir2(self):
        # Call your read function to refresh the table with all data
        self.lire_table2()

        # Optionally, you can clear the search entry if you have one
        self.rechercher2_entry.delete(0, 'end')
    






if (__name__ == '__main__'):
    window = ctk.CTk()
    window.iconbitmap('images\\download.ico')
    std = List_Jour(window)
    mainloop()        