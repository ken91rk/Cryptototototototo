import os # ajouter ce package 

# ouvrir un fichier
with open('message2.txt', 'r', encoding="utf-8") as file:
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

for cle in range(26, 46):
    resultat = decrypter(message, cle)
    print(f"Clé {cle}: {resultat}")

"""LA BONNE CLE EST 38 !!!!!!!"""