import io

# ouvrir un fichier lamiaword pour ecrire dessus 
# w:write r:read
fichier = io.open("lamia.word", "w")

fichier.write("Bonjour tous le monde comment vous allez le vie est difficile ces jour ci je narrive plus a suivre j'ai juste envie de laisser tomber ")
fichier.close()
fichier = io.open("lamia.word", "r")
contenu = fichier.read()
print("Contenu du fichier :", contenu)
fichier.close()