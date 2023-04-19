def pointDeRencontre(v1, v2, distance):
    #Calcul simplifié pour trouver le temps
    temps = distance / (v1 + v2)
    #Calcul simplifié pour trouver le point de rencontre 
    positionRencontre = v1 * temps
   

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))

