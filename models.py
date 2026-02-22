class Agriculteur:
    def __init__(self, nom, id_agri, cp, produit, capacite, cout, score, stockage):
        self.nom = nom
        self.id = id_agri
        self.code_postal = cp
        self.produit = produit
        self.capacite = capacite
        self.cout_production = cout
        self.score_credit = score
        self.stockage_max = stockage
def __repr__(self):
        return f"Agriculteur({self.nom}, {self.produit})"