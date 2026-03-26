import math
import os # ajouter ce package 

# ouvrir un fichier
with open('message1.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregiste le contenu dans message

# on peut ensuite utiliser message
print(message)

def trouver_nb_lignes(message, num_col):
    """Trouve le nombre de lignes sachant le nombre de colonnes"""
    nb_cases = len(message)  # Nombre total de caractères (avec espaces)
    num_ligne = math.ceil(nb_cases / num_col)  # nb_col × nb_ligne = nb_cases
    
    return num_ligne

def dechiffrer_message(message, num_col):
    # Calculer le nombre de lignes
    num_ligne = trouver_nb_lignes(message, num_col)
    print(f"Dimensions: {num_ligne} lignes x {num_col} colonnes")
    
    tableau = []
    for i in range(len(message)):
        tableau.append(message[i])
    
    for col in range(num_col):
        for ligne in range(num_ligne):
            index = ligne * num_col + col
            if index < len(tableau):
                print(tableau[index], end='')
    print()

# Appel de la fonction
dechiffrer_message(message, 77)