class Personne:
    def __init__(self, nom, prenom, age, adresse,fonction):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.focntion=fonction

    def fatiguer(self):
        print("Je suis tres fatiguée.")

    def Aplat(self):
        print("Je suis Aplat ")

    def se_presente(self):
        print(f"Bonjour, je m'appelle {self.nom} {self.prenom} et j'ai {self.age} ans. J'habite à {self.adresse}.")


# Création d'une instance de la classe Personne
ma_personne = Personne("Dupont", "Jean", 30, "12 rue des Lilas, 75001 Paris")

# Appel de la méthode se_presente pour afficher les informations de la personne
ma_personne.se_presente()
