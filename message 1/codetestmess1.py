import math
import os

# ouvrir un fichier
with open('message1.txt', 'r', encoding="utf-8") as file:
    message = file.read()

print(f"Message chiffré: {message}\n")

def trouver_nb_lignes(message, num_col):
    """Trouve le nombre de lignes sachant le nombre de colonnes"""
    nb_cases = len(message)
    num_ligne = math.ceil(nb_cases / num_col)
    return num_ligne

def dechiffrer_message(message, num_col):
    """Déchiffre et retourne le message"""
    num_ligne = trouver_nb_lignes(message, num_col)
    
    tableau = []
    for i in range(len(message)):
        tableau.append(message[i])
    
    message_dechiffre = ""
    for col in range(num_col):
        for ligne in range(num_ligne):
            index = ligne * num_col + col
            if index < len(tableau):
                message_dechiffre += tableau[index]
    
    return message_dechiffre

def verifier_sens(message):
    """Vérifie si le message a du sens (contient des mots français courants)"""
    # Liste de mots français très courants
    mots_courants = ['le', 'la', 'les', 'de', 'un', 'une', 'et', 'est', 'dans', 
                     'pour', 'que', 'qui', 'avec', 'par', 'sur', 'ce', 'il',
                     'vous', 'nous', 'je', 'tu', 'se', 'son', 'sa', 'ses',
                     'avoir', 'être', 'faire', 'dire', 'aller', 'voir', 'pouvoir']
    
    message_lower = message.lower()
    mots_trouves = sum(1 for mot in mots_courants if mot in message_lower)
    
    # Score basé sur le pourcentage de mots courants trouvés
    score = (mots_trouves / len(mots_courants)) * 100
    return score, mots_trouves

# Tester toutes les colonnes et noter les meilleures
print("=== ANALYSE AUTOMATIQUE ===\n")
resultats = []

for num_col in range(2, len(message) + 1):
    message_dechiffre = dechiffrer_message(message, num_col)
    score, nb_mots = verifier_sens(message_dechiffre)
    
    resultats.append({
        'colonnes': num_col,
        'score': score,
        'nb_mots': nb_mots,
        'message': message_dechiffre
    })

# Trier par score décroissant
resultats.sort(key=lambda x: x['score'], reverse=True)

# Afficher les 5 meilleurs résultats
print("TOP 5 DES RÉSULTATS LES PLUS PROBABLES:\n")
for i, res in enumerate(resultats[:5], 1):
    print(f"#{i} - {res['colonnes']} colonnes (Score: {res['score']:.1f}% - {res['nb_mots']} mots)")
    print(f"Message: {res['message']}")
    print("-" * 80)