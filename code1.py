def dechiffrer_message(message, num_col):    #faire la methode pour trouver le nombre de ligen aussi faireune fct chiffremnt
    tableau = []
    for i in range(len(message)):
        tableau.append(message[i])
    for col in range(num_col):  # Pour chaque colonne (0, 1, 2, 3)
        for ligne in range(num_col):  # Pour chaque ligne (0, 1, 2, 3)
            index = ligne * num_col + col  # Calculer la position dans le tableau
            if index < len(tableau):  # Vérifier qu'on ne dépasse pas
                print(tableau[index], end='')
    print() 

# Appel de la fonction
dechiffrer_message("CMTELE AENBU")


