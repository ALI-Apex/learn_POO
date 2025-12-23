class Personne:
    """Constructeur"""

    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    """ Les methodes """

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age}ans et j'habite à {self.ville}")

    def avoir_anniverssaire(self):
        try:
            # verifier si l'age est bien un nombre et l'incrementer de 1
            self.age = int(self.age) + 1
            # formatage de texte
            print(f"Joyeux anniverssaire {self.nom}, tu as maintenant {self.age}ans")
        except ValueError:
            print("Erreur: La variable age doit etre un chiffre")


class CompteBancaire:
    """constructeur"""

    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0

    def deposer(self, montant):
        try:
            self.solde += int(montant)
            print(
                f"Vous avez deposer {montant}$ sur votre compte, votre nouveau solde est {self.solde}$"
            )
        except ValueError:
            print("Erreur: Veuillez entrer un montant valide")

    def retirer(self, montant):
        if self.solde > 0:
            try:
                self.solde -= int(montant)
                print(f"Vous avez retiré {montant}$")
            except ValueError:
                print("Erreur: Veuillez entrer un montant valide")
        elif self.solde < 0:
            print("Votre solde est insuffisant")

    def afficher_solde(self):
        print(f"Votre solde est de {self.solde}$")


""" Instanciation """
personne1 = Personne("ALI", 23, "Lomé")
compte1 = CompteBancaire("ALI")

""" appelle des methodes sur l'objet """
# class personne
personne1.se_presenter()
print(personne1.avoir_anniverssaire())

# classcompteBancaire
compte1.afficher_solde()
compte1.deposer(1000)
compte1.retirer(500)
compte1.afficher_solde()
