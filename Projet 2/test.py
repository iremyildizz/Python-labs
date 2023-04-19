from random import randint, randrange

def creerMolecule(x, y, dx, dy, rayon):
    #TODO 3.1.1 Créer le dictionnaire pour représenter une molécule
    molecule = {"x" : x, "y" : y, "dx" : dx, "dy" : dy, "rayon" : rayon}
    return molecule

def moleculesSeTouche(mol_1, mol_2):
    #TODO 3.1.2 Implémenter la formule pour vérifier si deux molécules se touche
    # Renvoi vrai si les molécules se touchent, faux si non
    d = (((mol_1["x"] - mol_2["x"]) ** 2) + ((mol_1["y"] - mol_2["y"]) ** 2)) ** 1/2
    if mol_1["rayon"] != mol_2["rayon"]:
        if mol_1["rayon"] + mol_2["rayon"] >= d:
            return True
    else:
        return False

def creerListMolecules(hauteur,xmin,xmax,nbMolecules):
    #TODO 3.1.5 Remplir la liste de molécule comme déctrit dans le README
    # vous pouvez utiliser rayon = randrange(10,30,2) et randint pour x,y,dx,dy
    molecules = []
    for i in range (nbMolecules):
        rayon = randrange(10,30,2)
        x = randint((xmin + rayon), (xmax - rayon))
        dx = randrange(10,30,2)#à demander#à demander#à demander
        y = randint(rayon, hauteur - rayon)
        dy = randrange(10,30,2) #à demander#à demander#à demander
        molecules.append(creerMolecule(x, y, dx, dy, rayon))
    return molecules

# def deplacerMolecule(mol):
#     #TODO 3.1.3 Faire le déplacement de la molécule
#     mol['x'], mol['y'] = (x + dx) , (y + dy)
#     return mol

def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    listeDroit = creerListMolecules(hauteur, 0, posParoi, nbMoleculesD)
    listeGauche = creerListMolecules(hauteur, posParoi, largeur, nbMoleculesG)
    reservoir = {"droit" : listeDroit, "gauche" : listeGauche}

    return reservoir 

def inverseDirMolecules(reservoir):
#TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
# Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    for i in range(len(reservoir["droit"])):
        print((reservoir["droit"][i]["x"]))


hauteur = 1000
largeur = 1000
posParoi = largeur/2
nbMoleculesG = 5
nbMoleculesD = 5

reservoir = creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD)

inverseDirMolecules(reservoir)