import os
import platform
os.system('cls')

class MaClasse:
    a = 0
    b = 0
    student_name = ""
    boolean = True

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somme(self):
        return self.a + self.b

    def moins(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def puissance(self):
        return self.a ** self.b

def utilier(obj):
    La_somme = obj.somme()
    Le_moins = obj.moins()
    La_multiplication = obj.multiplication()
    La_division = obj.division()
    La_puissance = obj.puissance()
    print("Résultat de la somme:", La_somme)
    print("Résultat de la soustraction:", Le_moins)
    print("Résultat de la multiplication:", La_multiplication)

obj = MaClasse(1, 5)
utilier(obj)