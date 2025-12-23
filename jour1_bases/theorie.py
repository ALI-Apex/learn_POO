class Voiture:

    def __init__(self, marque, modele, annee):
        """constructeur : s'exécute à la creation d'un objet"""

        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0

    def rouler(self, km):
        self.kilometrage += km
        print(f"La {self.marque} a roulé {km}km")

    def afficher_info(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.kilometrage}km "


""" Création des instnces de l class voiture """

voiture1 = Voiture("Toyota", "Corrolla", 2020)
voiture2 = Voiture("Honda", "Civic", 2021)

""" Utiliser les methodes """
voiture1.rouler(1000)
print(voiture1.afficher_info())

print("======== Deuxieme voiture ========= ")

voiture2.rouler(2000)
print(voiture2.afficher_info())
