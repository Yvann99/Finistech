import pandas as pd
from models import Agriculteur

def charger_exploitations(chemin_fichier):
    # Lecture de l'onglet spécifique
    df = pd.read_excel(chemin_fichier, sheet_name='Exploitations agricoles')
    
    liste_objets_agri = []
    
    for _, row in df.iterrows():
        # On crée l'objet en utilisant les noms de colonnes de ton image
        agri = Agriculteur(
            nom=row['Nom_Exploitation'],
            id_agri=row['ID_Agri'],
            cp=row['Code_Postal'],
            produit=row['Type_Produit'],
            capacite=row['Capacite_Annuelle'],
            cout=row['Cout_Production'],
            score=row['Score_Credit'],
            stockage=row['Stockage_Max']
        )
        liste_objets_agri.append(agri)
        
    return liste_objets_agri

# --- TEST ---
if __name__ == "__main__":
    mes_agris = charger_exploitations('Liste clients.xlsx')
    for a in mes_agris:
        print(f"Chargé : {a.nom} (ID: {a.id}) - Produit: {a.produit}")