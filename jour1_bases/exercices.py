class Personne:
    """ Constructeur  """
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
        
    
    
""" Instanciation """ 
personne1 = Personne("ALI", 23, "Lomé")

""" appelle des methodes sur l'objet """
personne1.se_presenter()
print(personne1.avoir_anniverssaire())