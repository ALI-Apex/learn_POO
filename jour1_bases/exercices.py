class Personne:
    """Constructeur"""

    def __init__(self, nom, age, ville):
        self.nom = nom
        self.ville = ville

        try:
            self.age = int(age)
            if self.age < 0:
                raise ValueError("Erreur: L'age ne doit pas etre negatif")
        except ValueError:
            raise ValueError("Erreur: L'age doit etre un nombre entier")

    """ Les methodes """

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age}ans et j'habite à {self.ville}")

    def avoir_anniverssaire(self):
        self.age += 1
        print(f"Joyeux anniverssaire {self.nom}, tu as maintenant {self.age}ans")


class CompteBancaire:
    """constructeur"""

    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0

    def deposer(self, montant):
        try:
            # convertir le montant
            montant = float(montant)

            # verifier si le montant est positif
            if montant <= 0:
                print("Erreur: le montant doit etre positif")
                return

            self.solde += montant
            print(
                f"Vous avez deposer {montant}$ sur votre compte, votre nouveau solde est {self.solde}$"
            )
        except ValueError:
            print("Erreur: Veuillez entrer un montant valide")

    def retirer(self, montant):
        try:
            montant = float(montant)

            # verifier si le montant est positif
            if montant <= 0:
                print("Erreur: le montant doit etre positif")
                return

            # verifier si le solde est suffisant
            if montant > self.solde:
                print("Votre solde est insuffisant")
                return

            self.solde -= montant
            print(f"Vous avez retiré {montant}$")
        except ValueError:
            print("Erreur: Veuillez entrer un montant valide")

    def afficher_solde(self):
        print(f"Titulaire : {self.titulaire}")
        print(f"Solde : {self.solde}$")


class Rectangle:
    """Constructeur"""

    def __init__(self, largeur, hauteur):
        """Validation des attributs"""
        try:
            self.largeur = float(largeur)
            self.hauteur = float(hauteur)

            if self.hauteur < 0 or self.largeur < 0:
                raise ValueError("Les dimensions doivent etre positives")
        except ValueError:
            raise ValueError(
                "Erreur: les dimenssions doivent etre des nombres positives"
            )

    """ Methodes """

    def calculer_air(self):
        aire = self.largeur * self.hauteur
        print(f"L'aire de votre rectangle est {aire}cm2")
        return aire

    def calculer_perimetre(self):
        perimetre = 2 * (self.largeur + self.hauteur)
        print(f"Le perimetre de votre rectangle est {perimetre}cm")
        return perimetre

    def est_carre(self):
        if self.largeur == self.hauteur:
            print(f"Oui, c'est un carré de cotés {self.largeur}")
            return True
        else:
            print("Non, ce n'est pas un carré")
            return False


""" Instanciation """
personne1 = Personne("ALI", 23, "Lomé")
compte1 = CompteBancaire("ALI")
rectangle1 = Rectangle(100, 50)

""" appelle des methodes sur l'objet """
# class personne
personne1.se_presenter()
print(personne1.avoir_anniverssaire())

# classcompteBancaire
compte1.afficher_solde()
compte1.deposer(1000)
compte1.retirer(500)
compte1.afficher_solde()

# class rectangle
rectangle1.calculer_air()
rectangle1.calculer_perimetre()
rectangle1.est_carre()
