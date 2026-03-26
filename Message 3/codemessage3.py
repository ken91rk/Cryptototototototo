import os # ajouter ce package 

# ouvrir un fichier
with open('message3.txt', 'r', encoding="utf-8") as file:
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



def decrypter(message, key):
    message_decrypté = ""
    for i in range(len(message)):
        lettre = message[i]
        nombre = ord(lettre) - key  # On soustrait au lieu d'additionner
        nouvelle_lettre = chr(nombre)
        message_decrypté += nouvelle_lettre
    return message_decrypté

# chr("")
m = min([ord(c) for c in message]) - ord("\n")
# m ~ 10 + cle
for cle in range(m-5, m+5):
    resultat = decrypter(message, cle)
    if "Joël" in resultat:
        print(f"Clé {cle}: {resultat}")

""" 
- créer une liste de mots les plus utiliser
- mettre le code sur message 2
"""
