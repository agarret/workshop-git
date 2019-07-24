
# Ajouter votre dependance ici :
from aureliengarret import ag
from thomasottone import to

# Ajouter votre variable dans la liste ici :
users = [
    ag, 
    to
]


print("Merci aux utilisateurs suivants d'avoir testés git : ")
print(*users, sep = "\n") 
