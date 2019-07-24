
# Ajouter votre dependance ici :
from aureliengarret import ag
from thomasottone import to
from alberteinstein import ae

# Ajouter votre variable dans la liste ici :
users = [
    ag, 
    to,
    ae
]


print("Merci aux utilisateurs suivants d'avoir testés git : ")
print(*users, sep = "\n") 
