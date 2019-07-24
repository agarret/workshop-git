
# Ajouter votre dependance ici :
from aureliengarret import ag
from thomasottone import to
from isaacnewton import icn
from alberteinstein import ae

# Ajouter votre variable dans la liste ici :
users = [
    ag, 
    to,
    icn,
    ae
]


print("Merci aux utilisateurs suivants d'avoir testés git : ")
print(*users, sep = "\n") 
