import math
import os
import re

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

def verifier_sens_avance(message):
    """Vérifie si le message a du sens avec plusieurs critères"""
    message_lower = message.lower()
    score_total = 0
    
    # 1. Mots français très courants (30 points max)
    mots_courants = ['le', 'la', 'les', 'de', 'du', 'un', 'une', 'des', 'et', 'est', 'dans', 
                     'pour', 'que', 'qui', 'avec', 'par', 'sur', 'ce', 'cette', 'il', 'elle',
                     'vous', 'nous', 'je', 'tu', 'se', 'son', 'sa', 'ses', 'leur', 'leurs',
                     'avoir', 'être', 'faire', 'dire', 'aller', 'voir', 'pouvoir', 'vouloir']
    
    mots_trouves = sum(1 for mot in mots_courants if f' {mot} ' in f' {message_lower} ')
    score_mots = min((mots_trouves / 10) * 30, 30)  # Max 30 points
    
    # 2. Fréquence des lettres françaises (25 points max)
    lettres_communes = ['e', 'a', 's', 't', 'i', 'n', 'r', 'u', 'l', 'o']
    freq_lettres = sum(message_lower.count(lettre) for lettre in lettres_communes)
    score_lettres = min((freq_lettres / len(message)) * 100, 25)
    
    # 3. Présence d'espaces réguliers (20 points max)
    nb_espaces = message.count(' ')
    if len(message) > 0:
        ratio_espaces = nb_espaces / len(message)
        if 0.10 < ratio_espaces < 0.20:  # Espaces entre 10% et 20%
            score_espaces = 20
        else:
            score_espaces = ratio_espaces * 50
    else:
        score_espaces = 0
    
    # 4. Absence de séquences bizarres (15 points max)
    # Pénaliser les répétitions de consonnes
    pattern_bizarre = re.findall(r'[bcdfghjklmnpqrstvwxz]{4,}', message_lower)
    score_coherence = 15 - min(len(pattern_bizarre) * 5, 15)
    
    # 5. Structure de phrase (10 points max)
    # Majuscules en début, ponctuation
    score_structure = 0
    if message and message[0].isupper():
        score_structure += 5
    if any(p in message for p in ['.', '!', '?', ',']):
        score_structure += 5
    
    score_total = score_mots + score_lettres + score_espaces + score_coherence + score_structure
    
    details = {
        'mots': score_mots,
        'lettres': score_lettres,
        'espaces': score_espaces,
        'coherence': score_coherence,
        'structure': score_structure
    }
    
    return score_total, details

# Tester toutes les colonnes et noter les meilleures
print("=== ANALYSE AUTOMATIQUE AVANCÉE ===\n")
resultats = []

for num_col in range(2, min(len(message) + 1, 100)):  # Limiter à 100 colonnes max
    message_dechiffre = dechiffrer_message(message, num_col)
    score, details = verifier_sens_avance(message_dechiffre)
    
    resultats.append({
        'colonnes': num_col,
        'score': score,
        'details': details,
        'message': message_dechiffre
    })

# Trier par score décroissant
resultats.sort(key=lambda x: x['score'], reverse=True)

# Afficher les 3 meilleurs résultats avec détails
print("TOP 3 DES RÉSULTATS LES PLUS PROBABLES:\n")
for i, res in enumerate(resultats[:3], 1):
    print(f"#{i} - {res['colonnes']} colonnes")
    print(f"Score global: {res['score']:.1f}/100")
    print(f"  • Mots courants: {res['details']['mots']:.1f}/30")
    print(f"  • Fréquence lettres: {res['details']['lettres']:.1f}/25")
    print(f"  • Espaces: {res['details']['espaces']:.1f}/20")
    print(f"  • Cohérence: {res['details']['coherence']:.1f}/15")
    print(f"  • Structure: {res['details']['structure']:.1f}/10")
    print(f"Message: {res['message'][:100]}...")  # Afficher les 100 premiers caractères
    print("=" * 80)

# Afficher le meilleur résultat complet
print("\n🎯 MEILLEUR RÉSULTAT (score le plus élevé):\n")
meilleur = resultats[0]
print(f"Nombre de colonnes: {meilleur['colonnes']}")
print(f"Score: {meilleur['score']:.1f}/100")
print(f"\nMessage complet:\n{meilleur['message']}")