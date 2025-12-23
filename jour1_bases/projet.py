class Livre:
    """constructeur"""

    def __init__(self, titre, auteur, pages, lu=False):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self.lu = lu

    """ Methodes """

    def marquer_comme_lu(self):
        self.lu = True
        print(f"'{self.titre}' a été marqué comme lu")

    def marquer_comme_non_lu(self):
        self.lu = False
        print(f"'{self.titre}' a été marqué comme non lu")

    def afficher_info(self):
        """Affiche les informations du livre"""
        statut = "Lu" if self.lu else "Non lu"
        print(f"📚 {self.titre}")
        print(f"   Auteur: {self.auteur}")
        print(f"   Pages: {self.pages}")
        print(f"   Statut: {statut}")
        print()

    def __str__(self):
        """Représentation en chaîne de caractères"""
        statut = "✓" if self.lu else "✗"
        return f"{statut} {self.titre} - {self.auteur} ({self.pages} pages)"


""" instanciation """
livres = []

livre1 = Livre("Père riche, père pauvre", "Robert Kyosaki", 200, True)
livre2 = Livre("L'art de la guerre", "Sun Tzu ", 100, False)
livre3 = Livre("Du reve à la réalité", "John Maxwell ", 150, True)
livre4 = Livre("Devenez un grand leader", "Steven Sample", 300, True)
livre5 = Livre("La chevre de ma mère", "Ricardo Kaniama", 100, True)

livres.append(livre1)
livres.append(livre2)
livres.append(livre3)
livres.append(livre4)
livres.append(livre5)

# Afficher tous les livres
print("=== TOUS LES LIVRES ===")
for livre in livres:
    print(livre)

print("\n=== LIVRES LUS ===")
for livre in livres:
    if livre.lu:
        print(f"- {livre.titre} par {livre.auteur}")

print("\n=== LIVRES NON LUS ===")
for livre in livres:
    if not livre.lu:
        print(f"- {livre.titre} par {livre.auteur}")

# Exemple d'utilisation des méthodes
print("\n=== TEST DES MÉTHODES ===")
livre2.marquer_comme_lu()
livre2.afficher_info()

# Statistiques
total_pages = sum(livre.pages for livre in livres)
livres_lus = sum(1 for livre in livres if livre.lu)
print(f"\n📊 Statistiques:")
print(f"Total de livres: {len(livres)}")
print(f"Livres lus: {livres_lus}/{len(livres)}")
print(f"Total de pages: {total_pages}")
