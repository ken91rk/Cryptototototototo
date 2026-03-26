import os # ajouter ce package 

# ouvrir un fichier
with open('message4.txt', 'r', encoding="utf-8") as file:
    message = file.read() # enregiste le contenu dans message

# on peut ensuite utiliser message
print(message)

def crypter(message, key):
    message_crypté=""
    for i in range(len(message)):
            lettre = message[i]
            nombre = ord(lettre) + key
            nouvelle_lettre = chr(nombre)
            message_crypté += nouvelle_lettre
    return message_crypté



"""print(crypter("Je suis Keninho 91 !", 5))"""
def est_paire(position):
    if position % 2 == 0:  
        return True
    else:
        return False


def decrypter(message, key):
    message_decrypté = ""
    for i in range(len(message)):
        lettre = message[i]
        if est_paire(i) == True:
            nombre = ord(lettre) - key[0]  # On soustrait au lieu d'additionner
            nouvelle_lettre = chr(nombre)
            message_decrypté += nouvelle_lettre
        else:
            nombre = ord(lettre) - key[1]  # On soustrait au lieu d'additionner
            nouvelle_lettre = chr(nombre)
            message_decrypté += nouvelle_lettre
    return message_decrypté

# chr("")
Liste_pair = []
Liste_impaire = []
for i in range(len(message)):
    if i == 0 or est_paire(i) == True:
        Liste_pair.append(ord(message[i]))
    else:
        Liste_impaire.append(ord(message[i]))

        


key_paire = min(Liste_pair) - ord("\n")
key_impaire = min(Liste_impaire) - ord("\n")
key=[key_paire, key_impaire]




for cle in range(key_impaire-5, key_impaire+5):
    resultat = decrypter(message, [key_paire, cle])
    if "Joël" in resultat:
        print(f"Clé {cle}: {resultat}")

for cle in range(key_paire-5, key_paire+5):
    resultat = decrypter(message, [cle, key_impaire])
    if "Joël" in resultat:
        print(f"Clé {cle}: {resultat}")
    

        

# m ~ 10 + cle


""" 
- créer une liste de mots les plus utiliser
- mettre le code sur message 2
"""
