# Initilisation des variables 
capitalInitial = 300000 # en dollars
tauxAnnuel = 0.08 # pourcentage / 100 

# Calcul du capital au bout de 20 années 
def capitalTotale(capital, nbAnnees):
    for i in range(nbAnnees):
        capital += capital * tauxAnnuel 
    return capital

capitalFinale = capitalTotale(capitalInitial, 20)

# Affichage du capital au bout de 20 années 
print("Capital au bout de 20 années : " + str(capitalFinale))