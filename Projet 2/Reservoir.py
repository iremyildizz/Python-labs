# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      : 
# Creer par     : 
# Version num   : 
# Modifier le   : 

import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule


def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    listeGauche = creerListMolecules(hauteur, 0, posParoi, nbMoleculesG)
    listeDroit = creerListMolecules(hauteur, posParoi, largeur, nbMoleculesD)

    lCG = [0] * int(nbMoleculesG * (nbMoleculesG - 1) / 2)
    lCD = [0] * int(nbMoleculesD * (nbMoleculesD - 1) / 2)

    reservoir = {"mD" : listeDroit, "mG" : listeGauche, "h" : hauteur, "l" : largeur, "posPar" : posParoi, "lCG": lCG, "lCD" : lCD}

    return reservoir 


def colision(reservoir):
    #TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir
    reservoirTemplate = {"mD" : 0, "mG" : 0, "h" : 0, "l" : 0, "posPar" : 0, "lCG": 0, "lCD" : 0}
    if reservoir.keys() != reservoirTemplate.keys():
        print("Erreur le reservoir n'est pas de dictionnaire reservoir.")
        return

    listeCote = [reservoir["mD"], reservoir["mG"]]
    listeColisionsCotes = [reservoir["lCD"], reservoir["lCG"]]

    for n in range (len(listeCote)):
        colisionIndex = 0
        for i in range (len(listeCote[n]) - 1):
            for j in range (i + 1, (len(listeCote[n]))):
                if moleculesSeTouche(listeCote[n][i], listeCote[n][j]) == True:
                    ajusteDirApresCollision(listeCote[n][i],listeCote[n][j])
                    listeColisionsCotes[n][colisionIndex] = 1
                else:
                    listeColisionsCotes[n][colisionIndex] = 0
                colisionIndex += 1

    return reservoir


def inverseDirMolecules(reservoir):
    #TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    reservoirTemplate = {"mD" : 0, "mG" : 0, "h" : 0, "l" : 0, "posPar" : 0, "lCG": 0, "lCD" : 0}
    if reservoir.keys() != reservoirTemplate.keys():
        print("Erreur le reservoir n'est pas de dictionnaire reservoir.")
        return

    for i in range(len(reservoir["mD"])):
        inverseDirMolecule((reservoir["mD"])[i], reservoir["posPar"], reservoir["l"], reservoir["h"])

    for i in range(len(reservoir["mG"])):
        inverseDirMolecule((reservoir["mG"])[i], 0, reservoir["posPar"],  reservoir["h"])
        
    return reservoir

def getTemperature(reservoir, cote):
#     #TODO 3.2.4 Calcule la température de chaque côté du réservoir.
#     # Utiliser la formule dans le Readme
    reservoirTemplate = {"mD" : 0, "mG" : 0, "h" : 0, "l" : 0, "posPar" : 0, "lCG": 0, "lCD" : 0}
    if reservoir.keys() != reservoirTemplate.keys():
        print("Erreur le reservoir n'est pas de dictionnaire reservoir.")
        return

    nomReservoir = ""
    if cote == "Gauche":
        nomReservoir = "mG"
    else:
        nomReservoir = "mD" 

    N = len(reservoir[nomReservoir])
    masse = 1
    E = 0
    for i in range (N):
        E += (1/2) * masse * (((reservoir[nomReservoir][i]["dx"]) ** 2 + (reservoir[nomReservoir][i]["dy"]) ** 2) ** (1/2))** 2

    temperature = E / N
    
    return temperature



# Donner
#####################################################
def affichage(reservoir, ax):
    reservoirTemplate = {"mD" : 0, "mG" : 0, "h" : 0, "l" : 0, "posPar" : 0, "lCG": 0, "lCD" : 0}
    if reservoir.keys() != reservoirTemplate.keys():
        print("Erreur le reservoir n'est pas de dictionnaire reservoir.")
        return

    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()
    ax.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10)
    ax.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    ax.title.set_text(txt.format(getTemperature(reservoir, "Gauche"), getTemperature(reservoir, "Droit")))

    for k in [['mG', 'ro'], ['mD', 'go']]:
        for i in range(len(reservoir[k[0]])):
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy'])) / 60, 0.2), 1)
            ax.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha=inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])

    plt.pause(0.01)
    clear_output() 
    

def deplacerMolecules(reservoir, ax):
    reservoirTemplate = {"mD" : 0, "mG" : 0, "h" : 0, "l" : 0, "posPar" : 0, "lCG": 0, "lCD" : 0}
    if reservoir.keys() != reservoirTemplate.keys():
        print("Erreur le reservoir n'est pas de dictionnaire reservoir.")
        return

    # TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette function recoit comme parametre un objet de type reservoire est execute les etapes suivantes:
    # 1) Inverser la direction des molecules du reservoir
    inverseDirMolecules(reservoir)
    # 2) Afficher les molecules
    affichage(reservoir, ax)
    # 3) Determination des colision des molecules
    colision(reservoir)

    return reservoir

if __name__ == '__main__':
    hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD = 2000, 2000, 1300, 30, 30
    reservoir = creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot()
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir, ax)
        ax.clear()
