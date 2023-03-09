import os
import platform
import sys
os.system('cls')
class Animal:
    nom = ""
    espece = ""
    age = 0
    
    def __init__( self,nom, espece, age):
        self.nom = nom
        self.espece = espece
        self.age = age

    def faire_du_bruit(self,nom):
        print(nom+ " miolle ")

    def manger(self,nom):
        print("mon " + nom +" mange du poisson ")

    def dormir(self,nom):
        print("mon chat " +nom + " dort sur mon lit ")

    def se_presente(self):
       print(f"mon {self.espece} s'appelle {self.nom} et il a {self.age} ans")



animal1 = Animal("Félix", "Chat", 3)
animal2 = Animal("Rex", "Chien", 2)
animal3 = Animal("Bugs", "lapin", 1)
animal4 = Animal("Donald", "Canard", 4)
animal5 = Animal("Dumbo", "Éléphant", 10)


animal1.faire_du_bruit(animal1.nom)
animal2.manger(animal2.nom)
animal3.dormir(animal3.nom)
animal4.se_presente()
animal5.faire_du_bruit(animal5.nom)