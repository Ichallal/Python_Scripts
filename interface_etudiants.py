import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ajout d'étudiant")
        self.liste_etudiants = []
        self.create_widgets()

    def create_widgets(self):
        # Création des étiquettes et champs de saisie
        label_nom = tk.Label(self, text="Nom de l'étudiant : ")
        label_nom.grid(row=0, column=0)
        self.champ_nom = tk.Entry(self)
        self.champ_nom.grid(row=0, column=1)

        label_prenom = tk.Label(self, text="Prénom de l'étudiant : ")
        label_prenom.grid(row=1, column=0)
        self.champ_prenom = tk.Entry(self)
        self.champ_prenom.grid(row=1, column=1)

        label_age = tk.Label(self, text="Âge de l'étudiant : ")
        label_age.grid(row=2, column=0)
        self.champ_age = tk.Entry(self)
        self.champ_age.grid(row=2, column=1)

        # Création du bouton d'ajout et du bouton d'affichage
        bouton_ajouter = tk.Button(self, text="Ajouter", command=self.ajouter_etudiant)
        bouton_ajouter.grid(row=3, column=0)

        bouton_afficher = tk.Button(self, text="Afficher tous les étudiants", command=self.afficher_etudiants)
        bouton_afficher.grid(row=3, column=1)

    def ajouter_etudiant(self):
        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        age = self.champ_age.get()
        etudiant = Student(nom, prenom, age)
        self.liste_etudiants.append(etudiant)
        messagebox.showinfo("Succès", "L'étudiant {} a été ajouté avec succès.".format(etudiant.nom))

    def afficher_etudiants(self):
        if not self.liste_etudiants:
            messagebox.showwarning("Avertissement", "Aucun étudiant n'a été ajouté.")
        else:
            message = "Liste des étudiants : \n"
            for etudiant in self.liste_etudiants:
               message += "nom: {} {}\n".format(etudiant.nom, etudiant.prenom)
               message += "Age: {} ans\n".format(etudiant.age)
            messagebox.showinfo("Liste des étudiants", message)

if __name__ == "__main__":
    app = App()
    app.mainloop()