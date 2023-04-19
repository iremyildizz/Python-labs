# -*- coding: utf-8 -*-
# Nom_du_fichier: Molecule.py
# Creer le      : 
# Creer par     : 
# Version num   : 
# Modifier le   : 

from random import randint, randrange

def creerMolecule(x, y, dx, dy, rayon):
    #TODO 3.1.1 Créer le dictionnaire pour représenter une molécule
    molecule = {"x" : x, "y" : y, "dx" : dx, "dy" : dy, "rayon" : rayon}
    return molecule


def moleculesSeTouche(mol_1, mol_2):
    #TODO 3.1.2 Implémenter la formule pour vérifier si deux molécules se touche
    # Renvoi vrai si les molécules se touchent, faux si non
    moleculeTemplate = {"x" : 0, "y" : 0, "dx" : 0, "dy" : 0, "rayon" : 0}
    if mol_1.keys() != moleculeTemplate.keys() or mol_2.keys() != moleculeTemplate.keys():
        print("Erreur les molecules sont pas des dictionnaire molecule.")
        return

    d = (((mol_1["x"] - mol_2["x"]) ** 2) + ((mol_1["y"] - mol_2["y"]) ** 2)) ** (1/2)
    if mol_1["rayon"] + mol_2["rayon"] >= d:
        return True
    else:
        return False


def deplacerMolecule(mol):
    #TODO 3.1.3 Faire le déplacement de la molécule
    moleculeTemplate = {"x" : 0, "y" : 0, "dx" : 0, "dy" : 0, "rayon" : 0}
    if mol.keys() != moleculeTemplate.keys():
        print("Erreur la molecule n'est pas de dictionnaire molecule.")
        return

    mol['x'], mol['y'] = (mol["x"] + mol["dx"]) , (mol["y"] + mol["dy"])
    return mol

    
#####################################################
# Donner
#####################################################
def ajusteDirApresCollision(mol_1, mol_2):
    deltaX = mol_2['x'] - mol_1['x']
    dVx = 0

    if (deltaX == 0.0):
        dVy = mol_2['y'] - mol_1['y']
    else:
        r = (mol_2['y'] - mol_1['y']) / deltaX
        dVx = (mol_2['dx'] - mol_1['dx'] + (mol_2['dy'] - mol_1['dy']) * r) / (1 + r * r)
        dVy = r * dVx

    mol_1['dx'] += dVx
    mol_1['dy'] += dVy
    mol_2['dx'] -= dVx
    mol_2['dy'] -= dVy

    return mol_1, mol_2

def creerListMolecules(hauteur,xmin,xmax,nbMolecules):
    #TODO 3.1.5 Remplir la liste de molécule comme déctrit dans le README
    # vous pouvez utiliser rayon = randrange(10,30,2) et randint pour x,y,dx,dy
    molecules = []
    for i in range (nbMolecules):
        rayon = randrange(10,30,2)
        x = randint(xmin + rayon, xmax - rayon)
        dx = randrange(10,30,2)#à demander#à demander#à demander
        y = randint(rayon, hauteur - rayon)
        dy = randrange(10,30,2) #à demander#à demander#à demander
        molecules.append(creerMolecule(x, y, dx, dy, rayon))
    return molecules

def inverseDirMolecule(mol, paroiG, paroiD, hauteur):
    moleculeTemplate = {"x" : 0, "y" : 0, "dx" : 0, "dy" : 0, "rayon" : 0}
    if mol.keys() != moleculeTemplate.keys():
        print("Erreur la molecule n'est pas de dictionnaire molecule.")
        return
    #TODO 3.1.6 Implémenter la fonction décrite dans le README
    # inverseDirMolecule inverse la direction de la molécule
    # Cette fonction reçoit en entrer quatre paramètres:
    # la molécule les parois gauche et droit du chaque côté du réservoir et la hauteurdu reservoir.
    # Si la molécule touche une des parois du réservoir un faut la reposition à la limite
    # du réservoir et inverser sa direction en vitesse.

    # Si la molécule touche la paroi gauche du réservoir en x
    
        # Repositionner la molécule et changer sa direction dx
    if mol["x"] - mol["rayon"] <= paroiG:
        mol["dx"] = -mol["dx"]
        mol["x"] = paroiG + mol["rayon"]

    # Si la molécule touche la paroi droite du réservoir en x

        # Repositionner la molécule et changer sa direction dx
    if mol["x"] + mol["rayon"] >= paroiD:
        mol["dx"] = -mol["dx"]
        mol["x"] = paroiD - mol["rayon"]


    # Si la molécule touche la paroi gauche du réservoir en y

        # Repositionner la molécule et changer sa direction dy
    if mol["y"] + mol["rayon"] >= hauteur:
        mol["dy"] = -mol["dy"]
        mol["y"] = hauteur - mol["rayon"]

    # Si la molécule touche la paroi droite du réservoir en y

        # Repositionner la molécule et changer sa direction dy
    if mol["y"] - mol ["rayon"] <= 0:
        mol["dy"] = -mol["dy"]
        mol["y"] = mol["rayon"]

    return mol

if __name__ == '__main__':
    # Test creerMolecule
    x, y, dx, dy, rayon = 5, 2, -3, 4, 5
    mol = creerMolecule(x, y, dx, dy, rayon)
    text = "La position de la molecule est ({},{}), sa vitesse est ({},{}) "
    text += "et son rayon est {}"
    
    print(text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    # Test moleculesSeTouche
    
    mol_1  = creerMolecule(x, y, dx, dy, rayon)
    mol_2  = mol_1
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
       
    mol_2  = creerMolecule(x, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon/4)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+2*rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    # Test deplacerMolecule
    
    old_text = "Avant le deplacement \n\t" + text
    print(old_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    mol = deplacerMolecule(mol)
    new_text = "Apres le deplacement \n\t" + text
    print(new_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))

    
