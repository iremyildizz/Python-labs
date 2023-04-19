# Initialisation des variables 
NOMBREDEJOURPARANNE = 365
capital = 2600 # en dollars
tauxAnnuelPremier = 0.045 # pourcentage / 100 
tauxPeriodiquePremier = tauxAnnuelPremier / NOMBREDEJOURPARANNE
tauxAnnuelDeuxieme = 0.10 # pourcentage / 100
tauxPeriodiqueDeuxieme = tauxAnnuelDeuxieme / NOMBREDEJOURPARANNE
fraisFixe = 60 # en dollars

def capitalPlacement(capitalDepart, nombreJours,tauxPeriodique , frais = 0):
    return capitalDepart - frais + (capitalDepart - frais) * tauxPeriodique * nombreJours

# Calcul du montant du capital avec le premier placement au 100ème jour de l'année 
capitalAvecPremierPlacement = capitalPlacement(capital, 100, tauxPeriodiquePremier)

# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année 
capitalAvecDeuxiemePlacement = capitalPlacement(capital, 300, tauxPeriodiqueDeuxieme, fraisFixe)

# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le Deuxieme
def nbDeJours(capitalDepart):
    nbJours = 1

    while capitalPlacement(capitalDepart, nbJours, tauxPeriodiquePremier) > capitalPlacement(capitalDepart, nbJours,tauxPeriodiqueDeuxieme, fraisFixe):
        nbJours += 1
    
    return nbJours

nombreDeJours = nbDeJours(capital)

# Affichage des valeurs calculées
print("Montant du capital avec le premier placement au 100ème jour : " + str(capitalAvecPremierPlacement) + " dollars")
print("Montant du capital avec le deuxième placement au 300ème jour : " + str(capitalAvecDeuxiemePlacement) + " dollars")
print(str(nombreDeJours) + " jours")